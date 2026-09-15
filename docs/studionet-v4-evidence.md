# Studionet v4 evidence

Verified on 2026-09-15 against [`0xEC35892545763B02Dd404846eB53848890d41137`](https://explorer-studio.genlayer.com/address/0xEC35892545763B02Dd404846eB53848890d41137). Deployed readback reported protocol version 4, owner `0xa365f55a3bf352767bc5c5739ffddaee8fcf3a19`, custody false and authority `GitHub raw tagged manifest + locked SHA-256`.

| Check | Transaction | Final return / state |
|---|---|---|
| Register digest-bound server | [`0xf96e4f...fe647`](https://explorer-studio.genlayer.com/tx/0xf96e4fc8c8c58fb887ad24f8ea6877481cac9e94efcc7c62b49c9007dacfe647) | Server 1; baseline `1.0.0`; controller B stored as canonical hex |
| Propose safe `1.1.0` | [`0xdcb206...1ecb9`](https://explorer-studio.genlayer.com/tx/0xdcb2060b811e0b4421ac14ab9cbc2c657c735057c3866dbb5103897c76c1ecb9) | Request 1, revision 1, `PENDING` |
| Wallet A assesses safe update | [`0x3d6874...66672`](https://explorer-studio.genlayer.com/tx/0x3d6874658aa3ebfd250b54652f126b47574f3d85fba78848b61228625be66672) | `SAFE_UPDATE`; fetched baseline/candidate digests match locked digests |
| Wallet A attempts consume | [`0xa40763...7106d`](https://explorer-studio.genlayer.com/tx/0xa407638d10a4e0fab916cd336c33302b9d5710762949aec97a2dd964f677106d) | `ONLY_DEPLOYMENT_CONTROLLER`; request unchanged |
| Wallet B supplies wrong action digest | [`0xb8008f...93a0ff`](https://explorer-studio.genlayer.com/tx/0xb8008ffe425fa16c3fb05d598324ac42a93a000724c43d9e65ff5f2c2293a0ff) | `ACTION_DIGEST_MISMATCH`; state unchanged |
| Wallet B consumes exact authorization | [`0x648b45...aa3791`](https://explorer-studio.genlayer.com/tx/0x648b45fa6ef911bbd98f47f34eb67634c6ba9e210d6e35dd9457ebc9f9aa3791) | `ROLLOUT_AUTHORIZATION_CONSUMED`; version and digest atomically advance to `1.1.0` |
| Wallet B replays exact authorization | [`0x835bb3...35139`](https://explorer-studio.genlayer.com/tx/0x835bb31f9091a7d57cb7979bc08cce7e1c99bbe71a81620f525fb0dec4035139) | `AUTHORIZATION_ALREADY_CONSUMED` |
| Propose hidden-payment `1.2.0` | [`0xf74d72...bb528`](https://explorer-studio.genlayer.com/tx/0xf74d729b127d88670e363ae83bb1438d8c2b44335ebb7477c950d2b604cbb528) | Request 2 bound to baseline `1.1.0` |
| Wallet A assesses capability expansion | [`0x684273...6ba1f`](https://explorer-studio.genlayer.com/tx/0x68427335705d0f01bcb92bf1fa91a70ad2e8aa07348ef5a4eebed36eaad6ba1f) | `CAPABILITY_DRIFT`; exact digests recorded; evidence digest `sha256:fc1489c75881f6ce3db30757354c242e626d5e36e07859663a4a5661d9df5c17` |
| Wallet B attempts exact conflict consume | [`0xab9b7f...4c83f`](https://explorer-studio.genlayer.com/tx/0xab9b7f066e0ebe7bd2cea076a7215fbab27c11c62a123892df3e74753274c83f) | `NOT_AUTHORIZED`; request and server byte-equivalent; baseline remains `1.1.0` |

## Final state

- Server baseline version: `1.1.0`.
- Server baseline digest: `sha256:0ef94d89ef0bb0a5b115904913425757cd0d2dadf25dfb471d89aa878d14fbca`.
- Request 1: `SAFE_UPDATE`, revision 2, consumed once.
- Request 2: `CAPABILITY_DRIFT`, revision 2, never consumed.
- Test wallet A: `0x1D283b45974B0be9630DFD1deC6A62a9B72B2760`.
- Controller wallet B: `0xf96Cf822F9f4e76956AB9fAAa22B3BdCD7b10aD6`.

Historical v3 transactions demonstrate fail-closed recovery under upstream GitHub REST unavailability, but v4 removes that REST dependency and its successful first-pass raw-tag assessments are the current deployment evidence.
