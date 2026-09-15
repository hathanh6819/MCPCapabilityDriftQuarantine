# Proof obligation and state model

## Claim

The candidate MCP release does not materially expand the accepted baseline capability envelope under the registered policy.

## Falsifiers

A new or broadened write, execute, payment, external communication, sensitive-data access, wildcard scope, removed confirmation, incomplete inventory, mismatched server/version/tag/commit/tree/blob identity, malformed evidence or validator disagreement prevents rollout authorization.

## Boundary

The contract judges an exact tagged MCP tool manifest. It does not prove implementation code faithfully implements that declaration, scan a deployable package, execute the MCP server, deploy software or move funds. An integrating controller must bind the actual artifact to the registered action digest and consume the exact authorization before rollout.

## Lifecycle

`REGISTERED BASELINE → PENDING CANDIDATE → SAFE_UPDATE | CAPABILITY_DRIFT | UNRESOLVED`

- Only `UNRESOLVED` is retryable at the exact current revision.
- Negative semantic results are terminal.
- Policy revision changes invalidate previously issued authorization.
- Successful consume promotes the candidate version to baseline atomically.
- Failed and replayed consumption cannot mutate request or baseline state.
