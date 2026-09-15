# Threat model

## Protected assets

- Organization-approved MCP capability baseline.
- Rollout authorization bound to package, versions, policy, controller and action.
- Immutable audit history for positive, negative and unresolved assessments.

## Adversaries

- Candidate publisher presenting a benign description while adding dangerous effects.
- Caller substituting server, version, repository, manifest or rollout action.
- Prompt injection embedded in tool descriptions or schemas.
- Mutable branch, deceptive/missing version tag, truncated tree or changed raw content.
- Wrong controller, stale policy, expired ticket and replay attacker.

## Controls

- Fixed GitHub API and raw origins constructed by the contract.
- Version-tag-derived exact commit, not a claimant-declared commit or URL.
- Commit→complete tree→regular blob verification and complete-byte hashes.
- Exact schemas, bounds and identity repetition.
- Six boolean consensus surface; deterministic verdict and reason.
- Fail-closed `UNRESOLVED`, revision-aware recovery, controller binding and single-use baseline promotion.
