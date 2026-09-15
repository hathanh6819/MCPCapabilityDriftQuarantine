# MCP Capability Drift Quarantine

An Intelligent Contract that blocks MCP server releases when their real tool capabilities exceed the security envelope previously approved by an organization.

## Why GenLayer

npm and GitHub can establish package, version, commit, tree and blob identity. Deterministic code can validate schemas and byte commitments. It cannot reliably decide whether a natural-language tool description or input schema quietly adds payments, external communication, sensitive-data access, writes, execution, wildcard scope or removes meaningful human confirmation. GenLayer validators independently acquire both releases and reach strict consensus on six bounded boolean findings. The contract—not the model—derives `SAFE_UPDATE` or `CAPABILITY_DRIFT` and enforces rollout.

## Evidence chain

1. The owner registers an exact npm package, canonical GitHub repository, accepted baseline version, manifest path, security policy and a separate deployment controller.
2. A candidate specifies only its version and exact rollout action digest.
3. Validators fetch old and new version metadata directly from `registry.npmjs.org` and derive each `gitHead`, repository identity and published `dist.integrity`.
4. Validators fetch each GitHub commit and complete tree, locate the regular manifest blob, fetch the raw bytes and recompute Git blob SHA-1 and size.
5. Exact manifest identity and structure are checked before semantic comparison. Complete manifest SHA-256 values bind the receipt.
6. Only `SAFE_UPDATE` can be consumed by the registered controller before expiry, for the exact revision and action digest. Consumption atomically promotes the candidate to the new baseline once.

The contract does not claim to hash or unpack the npm tarball. `dist.integrity` proves the registry published an integrity commitment; GitHub commit/tree/blob verification proves the exact manifests actually adjudicated. Production deployment tooling must separately ensure the installed artifact matches the registry integrity before consuming the rollout authorization.

## Local release gate

```powershell
python scripts/verify_local.py
```

Constructor arguments: none. Do not deploy until public npm versions exist whose canonical metadata binds to a controlled GitHub fixture repository, or until a real package has explicitly authorized use for testing.
