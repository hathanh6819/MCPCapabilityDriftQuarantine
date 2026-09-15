# MCP Capability Drift Quarantine

An Intelligent Contract that blocks MCP server releases when their real tool capabilities exceed the security envelope previously approved by an organization.

## Why GenLayer

GitHub version tags, commits, trees and blobs establish release identity. Deterministic code validates schemas and byte commitments. It cannot reliably decide whether a natural-language tool description or input schema quietly adds payments, external communication, sensitive-data access, writes, execution, wildcard scope or removes meaningful human confirmation. GenLayer validators independently acquire both releases and reach strict consensus on six bounded boolean findings. The contract—not the model—derives `SAFE_UPDATE` or `CAPABILITY_DRIFT` and enforces rollout.

## Evidence chain

1. The owner registers an MCP server identity, canonical GitHub repository, accepted baseline version, manifest path, security policy and a separate deployment controller.
2. A candidate specifies only its version and exact rollout action digest.
3. Validators resolve `v{version}` through GitHub's canonical commits endpoint; callers cannot supply commit hashes or evidence URLs.
4. Validators verify each resolved Git commit and complete tree, locate the regular manifest blob, fetch the raw bytes and recompute Git blob SHA-1 and size.
5. Exact manifest identity and structure are checked before semantic comparison. Complete manifest SHA-256 values bind the receipt.
6. Only `SAFE_UPDATE` can be consumed by the registered controller before expiry, for the exact revision and action digest. Consumption atomically promotes the candidate to the new baseline once.

The contract proves the exact tagged manifest that was adjudicated. It does not prove implementation code faithfully matches the manifest or hash a deployable package. Production deployment tooling must independently bind its artifact digest to the action digest before consuming authorization.

## Local release gate

```powershell
python scripts/verify_local.py
```

Constructor arguments: none. Live testing requires a public GitHub repository with immutable `vX.Y.Z` tags and matching manifests.
