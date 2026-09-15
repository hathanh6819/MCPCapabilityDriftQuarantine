# Verification record

Verified locally on 2026-09-15.

- Direct Mode: `24 passed`.
- GenVM lint: `3 checks passed`.
- GenVM validation: `10 methods` (`4 view`, `6 write`), no constructor arguments.
- Architecture check: passed.
- Exact contract source bytes: `16,300`.
- Exact contract SHA-256: `52273b8c15822d42d028bd0ba623ffcc418ff5d2ed1f5107668a569b486c709b`.

## Covered invariants

- Owner-only registry and candidate creation; duplicate package rejection.
- npm package/version/repository/gitHead/dist-integrity binding.
- GitHub commit/tree/blob identity, complete-tree and exact-byte verification.
- Old and new manifests cannot be swapped between version identities.
- Malformed, unavailable, truncated, mismatched and oversized evidence fails closed.
- Model cannot change package/version identity, response schema or boolean types.
- Hidden payment capability produces a non-authorizing quarantine result.
- Only the exact controller/action/revision can consume a safe authorization.
- Policy changes, expiry, baseline races and replay do not mutate protected state.
- Only unresolved acquisition/model failure is revision-aware retryable.

## Remaining live gates

The project is ready for deployment, not yet ready for submission. Before submission: deploy exact source, verify source parity and initial reads, publish real registry/GitHub test resources, execute canonical and adversarial Studionet paths, record finalized receipts and complete before/after readbacks, and prove one exact rollout consumption plus replay rejection.
