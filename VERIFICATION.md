# Verification record

Verified locally on 2026-09-15.

- Direct Mode: `24 passed`.
- GenVM lint: `3 checks passed`.
- GenVM validation: `10 methods` (`4 view`, `6 write`), no constructor arguments.
- Architecture check: passed.
- Exact contract source bytes: `15,348`.
- Exact contract SHA-256: `8e5cd8e1db7ea1394d6533bc1f689602e5d3ae9029eea9b38a93a0bf9cceefe8`.

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

Deployment `0xB50a27D4Cb640487975fCE89c22000938773304b` is superseded because version 1 depended on npm Registry metadata. Version 2 removes npm entirely and derives exact commits from GitHub-controlled `v{version}` tags before commit/tree/blob verification. Redeploy the exact version-2 source before live testing.
