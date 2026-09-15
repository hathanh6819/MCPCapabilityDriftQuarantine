# Two-wallet Studionet audit

The deployer/owner is used only for registry setup and candidate creation. Never place any private key in this repository.

## Identities

- Test wallet A: permissionless validator caller and unauthorized rollout caller.
- Test wallet B: the registered deployment controller.

## Owner setup

Register server 1 with baseline `1.0.0`, baseline digest `sha256:14d0bf1689060ca1a8512403fe09a9e472f72bf213f03d5f4871737563a2a4ae`, path `mcp-tools.json`, repository `hathanh6819/MCPCapabilityDriftFixtures`, the locked policy, and wallet B as controller.

Create the safe request for `1.1.0` with candidate digest `sha256:0ef94d89ef0bb0a5b115904913425757cd0d2dadf25dfb471d89aa878d14fbca`. After it is consumed, create the drift request for `1.2.0` with candidate digest `sha256:147965faeab6dffef5b7796fbfacbf15974171b8d29e4767235d165f92ed2616`.

## Safe request

1. Wallet A calls `assess_update(request_id, 1)`. Expect `SAFE_UPDATE`, revision 2, both actual digests equal their locked commitments, and a non-empty evidence digest.
2. Wallet A calls `consume_rollout(request_id, 2, action_digest)`. Expect `ONLY_DEPLOYMENT_CONTROLLER` with byte-for-byte unchanged request and server state.
3. Wallet B calls consume with a wrong digest. Expect `ACTION_DIGEST_MISMATCH` and unchanged state.
4. Wallet B calls consume with the exact digest. Expect `ROLLOUT_AUTHORIZATION_CONSUMED`; baseline version and baseline digest advance atomically.
5. Wallet B repeats the exact call. Expect `AUTHORIZATION_ALREADY_CONSUMED` and unchanged state.

## Drift request

1. Wallet A calls `assess_update(request_id, 1)`. Expect `CAPABILITY_DRIFT`, revision 2 and a non-empty evidence digest binding the payment finding.
2. Wallet B calls consume with the exact digest. Expect `NOT_AUTHORIZED`; baseline and request remain unchanged.

## Recovery

Use a deliberately unavailable tag in a separate request. Assessment must produce `UNRESOLVED` with no evidence digest and no authorization. After restoring the source, call `retry_unresolved(request_id, current_revision)` and reassess with that same revision. A stale revision must return `STALE_REVISION` without mutation.
