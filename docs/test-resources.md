# Test resources

Direct Mode mocks authoritative transport responses, not verdict-only contract behavior. Each test executes the real contract and supplies bounded npm metadata, GitHub commit/tree/raw responses and model output at the nondeterministic boundary.

Before Studionet testing, publish two real npm versions and corresponding immutable GitHub commits. Each version must expose `gitHead`, repository identity and `dist.integrity`; each commit must contain `mcp-tools.json`. Use one capability-preserving candidate and separate adversarial releases for a hidden payment/write/confirmation change. Record raw response sizes, full commit IDs, tree IDs, blob SHA-1 values, manifest SHA-256 values, finalized transactions and before/after state.
