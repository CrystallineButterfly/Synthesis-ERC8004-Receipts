# Live readiness

- **Project:** ReceiptsMesh Reputation Market
- **Track:** Agents With Receipts
- **Latest verification:** `verified`
- **Execution mode:** `offline_prepared`
- **Generated at:** `2026-03-19T03:52:11+00:00`

## Trust boundaries

- **ERC-8004 Receipts** — `contract_call` — Anchor identity, task receipts, and reputation updates.
- **Olas** — `rest_json` — Hire and serve marketplace requests with receipts.
- **PayWithLocus** — `rest_json` — Create bounded subaccounts and controlled spend flows.
- **ENS** — `contract_call` — Publish human-readable coordination and identity receipts.
- **Bond.credit** — `rest_json` — Journal bounded trades and credit-profile updates.
- **OpenServ** — `rest_json` — Dispatch jobs and expose swarm service endpoints.
- **Bankr Gateway** — `rest_json` — Route inference through cost-aware model selection.

## Offline-ready partner paths

- **ERC-8004 Receipts** — prepared_contract_call
- **ENS** — prepared_contract_call

## Live-only partner blockers

- **Olas**: OLAS_API_KEY, OLAS_REQUEST_URL — https://docs.olas.network/
- **PayWithLocus**: LOCUS_API_KEY, LOCUS_PAYMENT_URL — https://docs.locus.finance/
- **Bond.credit**: GMX_ORDER_URL, BOND_CREDIT_PROFILE_URL — https://bond.credit/
- **OpenServ**: OPENSERV_API_KEY, OPENSERV_AGENT_URL — https://docs.openserv.ai/
- **Bankr Gateway**: BANKR_API_KEY, BANKR_CHAT_COMPLETIONS_URL, BANKR_MODEL — https://bankr.bot/

## Highest-sensitivity actions

- `bond_credit_credit_trade` — Bond.credit — Use Bond.credit for a bounded action in this repo.
- `bankr_gateway_compute_route` — Bankr Gateway — Use Bankr Gateway for a bounded action in this repo.

## Exact next steps

- Copy .env.example to .env and fill the required keys.
- Deploy the contract with forge script script/Deploy.s.sol --broadcast for ReceiptsMeshRegistry.
- Run python3 scripts/run_agent.py to produce a dry run for receipts_mesh.
- Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
- Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
