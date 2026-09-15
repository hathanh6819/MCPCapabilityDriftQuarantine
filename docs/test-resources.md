# Test resources

Direct Mode mocks authoritative transport responses, not verdict-only contract behavior. Each test executes the real contract and supplies bounded raw GitHub tagged-manifest responses plus model output at the nondeterministic boundary.

Before Studionet testing, publish GitHub tags `v1.0.0`, `v1.1.0` and `v1.2.0`. Each tag must expose `mcp-tools.json`. Independently compute and lock each complete manifest SHA-256 before assessment. Use one capability-preserving candidate and one adversarial hidden-payment release. Record tagged raw URLs, response sizes, manifest SHA-256 values, finalized transactions and before/after state. A moved tag fails closed unless its bytes still match the locked digest; this mechanism does not claim complete Git-tree integrity.
