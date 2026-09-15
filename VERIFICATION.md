# Verification record

Verified locally on 2026-09-15.

- Direct Mode: `25 passed`.
- GenVM lint: `3 checks passed`.
- GenVM validation: `10 methods` (`4 view`, `6 write`), no constructor arguments.
- Architecture check: passed.
- Exact contract source bytes: `15,634`.
- Exact contract SHA-256: `b326c5f2218fc93096efd19a7c2aa9129dcca5c18948076de2ef68d4dc8e26da`.

## Covered invariants

- Owner-only registry and candidate creation; duplicate package rejection.
- GitHub version-tag resolution and exact commit/tree/blob binding.
- GitHub commit/tree/blob identity, complete-tree and exact-byte verification.
- Old and new manifests cannot be swapped between version identities.
- Malformed, unavailable, truncated, mismatched and oversized evidence fails closed.
- Model cannot change package/version identity, response schema or boolean types.
- Hidden payment capability produces a non-authorizing quarantine result.
- Only the exact controller/action/revision can consume a safe authorization.
- Policy changes, expiry, baseline races and replay do not mutate protected state.
- Only unresolved acquisition/model failure is revision-aware retryable.

## Remaining live gates

Deployment `0xB50a27D4Cb640487975fCE89c22000938773304b` is superseded because version 1 depended on npm Registry metadata. Deployment `0x638C6349D8b6C57C241ef95d66f384c28e02837B` is superseded because live registration exposed GenVM's decimal `str(Address)` representation for method arguments. Version 3 normalizes sender and Address arguments through one canonical lowercase 20-byte hex function and includes a direct regression test. Redeploy the exact version-3 source before live testing.
