# Verification record

Verified locally on 2026-09-15.

- Direct Mode: `24 passed`.
- GenVM lint: `3 checks passed`.
- GenVM validation: `10 methods` (`4 view`, `6 write`), no constructor arguments.
- Architecture check: passed.
- Exact contract source bytes: `13,984`.
- Exact contract SHA-256: `652febb6e216b4fdbdf46e208d4e5cd40ad12dabbf8082260929d325decab119`.

## Covered invariants

- Owner-only registry and candidate creation; duplicate package rejection.
- Fixed GitHub raw tagged-manifest acquisition with owner-locked SHA-256 commitments.
- Full fetched-byte hashing before parsing, semantic judgment or positive state.
- Old and new manifests cannot be swapped between version identities.
- Malformed, unavailable, digest-mismatched and oversized evidence fails closed.
- Model cannot change package/version identity, response schema or boolean types.
- Hidden payment capability produces a non-authorizing quarantine result.
- Only the exact controller/action/revision can consume a safe authorization.
- Policy changes, expiry, baseline races and replay do not mutate protected state.
- Only unresolved acquisition/model failure is revision-aware retryable.

## Remaining live gates

Deployments `0xB50a27D4Cb640487975fCE89c22000938773304b` (npm provenance), `0x638C6349D8b6C57C241ef95d66f384c28e02837B` (decimal Address representation) and `0xd201d2F97419270bEdB8318E0Da481d3255A37c3` (shared GitHub REST availability) are superseded. Version 4 uses only fixed raw GitHub tag paths plus locked full-content SHA-256 commitments. Redeploy the exact version-4 source before live testing.
