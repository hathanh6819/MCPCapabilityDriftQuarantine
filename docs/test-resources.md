# Test resources

Direct Mode mocks authoritative transport responses, not verdict-only contract behavior. Each test executes the real contract and supplies bounded GitHub tag-resolution, commit, tree and raw responses plus model output at the nondeterministic boundary.

Before Studionet testing, publish immutable GitHub tags `v1.0.0`, `v1.1.0` and `v1.2.0` at their corresponding commits. Each commit must contain `mcp-tools.json`. Use one capability-preserving candidate and one adversarial hidden-payment release. Record tag resolution, raw response sizes, full commit IDs, tree IDs, blob SHA-1 values, manifest SHA-256 values, finalized transactions and before/after state.
