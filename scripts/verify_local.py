from __future__ import annotations
import hashlib,subprocess,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/"contracts"/"mcp_capability_drift_quarantine.py"
def run(args):
    print("\n$ "+" ".join(args),flush=True);subprocess.run(args,cwd=ROOT,check=True)
run([sys.executable,"-m","pytest","-q","-p","no:cacheprovider"])
run([sys.executable,"-X","utf8","-m","genvm_linter.cli","check",str(SOURCE.relative_to(ROOT))])
text=SOURCE.read_text(encoding="utf-8")
required=("raw.githubusercontent.com","/refs/tags/v","baseline_manifest_digest","candidate_manifest_digest","hashlib.sha256","strict_eq")
assert all(token in text for token in required)
assert all(token not in text for token in ("api.github.com","hashlib.sha1","/git/trees/"))
assert "payable" not in text
body=SOURCE.read_bytes();print("architecture_check=PASS");print("source_bytes="+str(len(body)));print("source_sha256="+hashlib.sha256(body).hexdigest())
