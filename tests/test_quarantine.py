import hashlib,json
from pathlib import Path
import pytest

CONTRACT="contracts/mcp_capability_drift_quarantine.py"
PACKAGE="acme-mcp"; REPO="acme/acme-mcp"; OLD="1.0.0"; NEW="1.1.0"; PATH="mcp-tools.json"
OLD_COMMIT="1"*40; NEW_COMMIT="2"*40; OLD_TREE="3"*40; NEW_TREE="4"*40
CONTROLLER="0x2222222222222222222222222222222222222222"; DIGEST="sha256:"+"a"*64
POLICY="Only existing read-only tools are permitted. External actions, payments, writes, execution and reduced confirmation are prohibited."

def deploy(dd): return dd(CONTRACT)
def setup(c):
    assert c.register_server(PACKAGE,REPO,OLD,PATH,POLICY,CONTROLLER)==1
    assert c.propose_update(1,NEW,DIGEST,86400)==1
def manifest(version,tools=None):
    if tools is None: tools=[{"name":"search_docs","description":"Search public product documentation.","input_schema":{"type":"object","properties":{"query":{"type":"string"}}},"effect":"read","requires_confirmation":False}]
    return json.dumps({"server":PACKAGE,"version":version,"tools":tools},sort_keys=True,separators=(",",":"))
def blob(body):
    raw=body.encode();return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\x00"+raw).hexdigest()
def mock_sources(vm,old_body=None,new_body=None,registry_status=200,bad_repo=False,truncated=False,bad_blob=False):
    old_body=old_body or manifest(OLD);new_body=new_body or manifest(NEW)
    for version,commit,tree,body in ((OLD,OLD_COMMIT,OLD_TREE,old_body),(NEW,NEW_COMMIT,NEW_TREE,new_body)):
        meta={"name":PACKAGE,"version":version,"gitHead":commit,"repository":{"url":"https://github.com/"+("evil/repo" if bad_repo else REPO)+".git"},"dist":{"integrity":"sha512-valid-integrity-value"}}
        vm.mock_web(r"registry\.npmjs\.org/"+PACKAGE+r"/"+version.replace(".",r"\."),{"status":registry_status,"body":json.dumps(meta)})
        vm.mock_web(r"/git/commits/"+commit,{"status":200,"body":json.dumps({"sha":commit,"tree":{"sha":tree}})})
        b=blob(body) if not bad_blob else "f"*40
        vm.mock_web(r"/git/trees/"+tree,{"status":200,"body":json.dumps({"sha":tree,"truncated":truncated,"tree":[{"path":PATH,"mode":"100644","type":"blob","sha":b,"size":len(body.encode())}]})})
        vm.mock_web(r"raw\.githubusercontent\.com/"+REPO+r"/"+commit,{"status":200,"body":body})
def mock_model(vm,safe=True,**updates):
    value={"package":PACKAGE,"old_version":OLD,"new_version":NEW,"tool_inventory_complete":True,"effects_within_approved_scope":safe,"data_access_not_expanded":safe,"external_actions_not_expanded":safe,"human_confirmation_preserved":safe,"material_capability_drift":not safe};value.update(updates)
    vm.mock_llm(r"Compare an approved MCP capability baseline",json.dumps(value))

def test_architecture_shape():
    source=Path(CONTRACT).read_text(encoding="utf-8")
    for token in ("registry.npmjs.org","/git/commits/","/git/trees/","raw.githubusercontent.com","hashlib.sha1","hashlib.sha256","strict_eq"):assert token in source
    assert "evidence_url" not in source and "payable" not in source
    compile(source,CONTRACT,"exec")

@pytest.mark.parametrize("field,value",[("package","Bad Package"),("repo","bad"),("version","latest"),("path","../x"),("policy","short"),("controller","0x0000000000000000000000000000000000000000")])
def test_invalid_server_does_not_mutate(direct_deploy,field,value):
    c=deploy(direct_deploy);args={"package":PACKAGE,"repository":REPO,"baseline_version":OLD,"manifest_path":PATH,"policy":POLICY,"deployment_controller":CONTROLLER};keys={"repo":"repository","version":"baseline_version","path":"manifest_path","controller":"deployment_controller"};args[keys.get(field,field)]=value
    assert isinstance(c.register_server(**args),str);assert c.get_counts()=={"server_count":0,"request_count":0}

def test_only_owner_and_duplicate_package(direct_deploy,direct_vm,direct_bob):
    c=deploy(direct_deploy)
    with direct_vm.prank(direct_bob):assert c.register_server(PACKAGE,REPO,OLD,PATH,POLICY,CONTROLLER)=="ONLY_OWNER"
    assert c.register_server(PACKAGE,REPO,OLD,PATH,POLICY,CONTROLLER)==1
    assert c.register_server(PACKAGE,REPO,OLD,PATH,POLICY,CONTROLLER)=="PACKAGE_ALREADY_REGISTERED"

def test_safe_update_consumes_once_and_advances_baseline(direct_deploy,direct_vm):
    c=deploy(direct_deploy);setup(c);mock_sources(direct_vm);mock_model(direct_vm,True)
    assert c.assess_update(1,1)=="SAFE_UPDATE";r=c.get_request(1);assert r["revision"]==2 and len(r["evidence_digest"])==71
    before=c.get_request(1);assert c.consume_rollout(1,2,DIGEST)=="ONLY_DEPLOYMENT_CONTROLLER";assert c.get_request(1)==before
    with direct_vm.prank(CONTROLLER):
        assert c.consume_rollout(1,2,"sha256:"+"b"*64)=="ACTION_DIGEST_MISMATCH"
        assert c.consume_rollout(1,2,DIGEST)=="ROLLOUT_AUTHORIZATION_CONSUMED"
        assert c.consume_rollout(1,2,DIGEST)=="AUTHORIZATION_ALREADY_CONSUMED"
    assert c.get_server(1)["baseline_version"]==NEW and c.get_request(1)["consumed"] is True

def test_hidden_payment_is_quarantined(direct_deploy,direct_vm):
    c=deploy(direct_deploy);setup(c)
    tools=json.loads(manifest(NEW))["tools"]+[{"name":"pay_vendor","description":"Send an autonomous USDC payment to a supplied recipient.","input_schema":{"type":"object"},"effect":"payment","requires_confirmation":False}]
    mock_sources(direct_vm,new_body=manifest(NEW,tools));mock_model(direct_vm,False)
    assert c.assess_update(1,1)=="CAPABILITY_DRIFT";before=c.get_request(1)
    with direct_vm.prank(CONTROLLER):assert c.consume_rollout(1,2,DIGEST)=="NOT_AUTHORIZED"
    assert c.get_request(1)==before and c.get_server(1)["baseline_version"]==OLD

def test_swapped_manifest_versions_fail_closed(direct_deploy,direct_vm):
    c=deploy(direct_deploy);setup(c);mock_sources(direct_vm,old_body=manifest(NEW),new_body=manifest(OLD))
    assert c.assess_update(1,1)=="UNRESOLVED";assert c.get_request(1)["reason"]=="MANIFEST_SCHEMA_OR_IDENTITY_INVALID"

@pytest.mark.parametrize("kwargs,reason",[({"registry_status":503},"REGISTRY_SOURCE_UNAVAILABLE_OR_OVERSIZED"),({"bad_repo":True},"REGISTRY_PROVENANCE_MISMATCH"),({"truncated":True},"TREE_INCOMPLETE_OR_MISMATCHED"),({"bad_blob":True},"BLOB_DIGEST_MISMATCH"),({"new_body":"not json"},"SOURCE_OR_MODEL_ERROR")])
def test_provenance_failures_are_unresolved(direct_deploy,direct_vm,kwargs,reason):
    c=deploy(direct_deploy);setup(c);mock_sources(direct_vm,**kwargs)
    assert c.assess_update(1,1)=="UNRESOLVED";r=c.get_request(1);assert r["reason"]==reason and r["evidence_digest"]=="" and not r["consumed"]

@pytest.mark.parametrize("updates",[{"package":"other"},{"new_version":"9.9.9"},{"extra":True},{"material_capability_drift":"false"}])
def test_model_cannot_change_identity_schema_or_types(direct_deploy,direct_vm,updates):
    c=deploy(direct_deploy);setup(c);mock_sources(direct_vm);mock_model(direct_vm,True,**updates)
    assert c.assess_update(1,1)=="UNRESOLVED";assert c.get_request(1)["evidence_digest"]==""

def test_unresolved_recovery_and_stale_revision(direct_deploy,direct_vm):
    c=deploy(direct_deploy);setup(c);mock_sources(direct_vm,registry_status=503);assert c.assess_update(1,1)=="UNRESOLVED"
    assert c.retry_unresolved(1,1)=="STALE_REVISION";assert c.retry_unresolved(1,2)=="PENDING"
    direct_vm.clear_mocks();mock_sources(direct_vm);mock_model(direct_vm,True);assert c.assess_update(1,2)=="SAFE_UPDATE";assert c.get_request(1)["revision"]==3

def test_policy_rotation_stales_authorization(direct_deploy,direct_vm):
    c=deploy(direct_deploy);setup(c);mock_sources(direct_vm);mock_model(direct_vm,True);c.assess_update(1,1)
    assert c.update_policy(1,POLICY+" New policy revision.")=="POLICY_UPDATED";before=c.get_request(1)
    with direct_vm.prank(CONTROLLER):assert c.consume_rollout(1,2,DIGEST)=="BASELINE_OR_POLICY_STALE"
    assert c.get_request(1)==before and c.get_server(1)["baseline_version"]==OLD

def test_parallel_safe_candidate_is_stale_after_first_baseline_promotion(direct_deploy,direct_vm):
    c=deploy(direct_deploy);assert c.register_server(PACKAGE,REPO,OLD,PATH,POLICY,CONTROLLER)==1
    assert c.propose_update(1,NEW,DIGEST,86400)==1;assert c.propose_update(1,NEW,"sha256:"+"c"*64,86400)==2
    mock_sources(direct_vm);mock_model(direct_vm,True);assert c.assess_update(1,1)=="SAFE_UPDATE";assert c.assess_update(2,1)=="SAFE_UPDATE"
    with direct_vm.prank(CONTROLLER):assert c.consume_rollout(1,2,DIGEST)=="ROLLOUT_AUTHORIZATION_CONSUMED"
    # Request 2 was bound to baseline 1.0.0 and cannot execute after request 1 promotes 1.1.0.
    before=c.get_request(2)
    with direct_vm.prank(CONTROLLER):assert c.consume_rollout(2,2,"sha256:"+"c"*64)=="BASELINE_OR_POLICY_STALE"
    assert c.get_request(2)==before

def test_expiry_blocks_without_mutation(direct_deploy,direct_vm):
    direct_vm.warp("2026-09-15T00:00:00Z");c=deploy(direct_deploy);setup(c);mock_sources(direct_vm);mock_model(direct_vm,True);c.assess_update(1,1);before=c.get_request(1)
    direct_vm.warp("2026-09-17T00:00:01Z")
    with direct_vm.prank(CONTROLLER):assert c.consume_rollout(1,2,DIGEST)=="AUTHORIZATION_EXPIRED"
    assert c.get_request(1)==before
