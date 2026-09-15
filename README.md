# MCP Capability Drift Quarantine

An Intelligent Contract that blocks MCP server releases when their real tool capabilities exceed the security envelope previously approved by an organization.

Verified Studionet deployment: [`0xEC35892545763B02Dd404846eB53848890d41137`](https://explorer-studio.genlayer.com/address/0xEC35892545763B02Dd404846eB53848890d41137). See the [v4 live evidence](docs/studionet-v4-evidence.md).

## Why GenLayer

GitHub raw version-tag paths establish release locators while owner-locked SHA-256 commitments establish exact manifest identity. Deterministic code validates the fetched bytes, schema and commitments. It cannot reliably decide whether a natural-language tool description or input schema quietly adds payments, external communication, sensitive-data access, writes, execution, wildcard scope or removes meaningful human confirmation. GenLayer validators independently acquire both releases and reach strict consensus on six bounded boolean findings. The contract—not the model—derives `SAFE_UPDATE` or `CAPABILITY_DRIFT` and enforces rollout.

## Evidence chain

1. The owner registers an MCP server identity, canonical GitHub repository, accepted baseline version, exact baseline-manifest SHA-256, manifest path, security policy and a separate deployment controller.
2. A candidate specifies its version, exact candidate-manifest SHA-256 and exact rollout action digest.
3. Validators fetch `raw.githubusercontent.com/{repo}/refs/tags/v{version}/{path}` directly; callers cannot supply arbitrary evidence URLs.
4. Validators recompute SHA-256 from every fetched byte and require exact equality with the locked baseline and candidate commitments before parsing or judgment.
5. Exact manifest identity and strict structure are checked before semantic comparison. Tagged paths and complete manifest SHA-256 values bind the receipt.
6. Only `SAFE_UPDATE` can be consumed by the registered controller before expiry, for the exact revision and action digest. Consumption atomically promotes the candidate to the new baseline once.

The contract proves the exact committed bytes fetched from each tagged manifest path and adjudicated. It does not prove tag immutability, complete repository-tree inclusion, or that implementation code faithfully matches the manifest. Production deployment tooling must independently bind its artifact digest to the action digest before consuming authorization.

## Local release gate

```powershell
python scripts/verify_local.py
```

Constructor arguments: none. Live testing requires a public GitHub repository with `vX.Y.Z` tags, matching manifests and their independently computed SHA-256 commitments. The owner performs registry setup; test wallet A can assess and prove outsider rejection, while controller wallet B proves wrong-digest rejection, valid one-time consumption and replay rejection.
