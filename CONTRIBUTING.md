# Contributing to APIsr

Only add a hosted free API with a replenishing quota or an ongoing public free
scope. Do not add a signup-credit balance, an expiring trial, scraped credentials,
or a service that requires a paid subscription for the claimed free access.

1. Read official pricing, quota, and licensing documentation. A GitHub list is a discovery source only.
2. Add the official evidence URL and review date. Distinguish requests from credits, rows, records, tokens, messages, and characters.
3. Record commercial-use restrictions and whether a payment method is explicitly required. Use `null` for unknown card requirements.
4. Preserve differences between free hosted APIs and open-source software needing paid compute.
5. Update JSON, CSV, the README table, category/total counts, and source ledger together.
6. Run `python scripts/validate.py`. A successful HTTP response does not prove the price.

Private API keys, OAuth secrets, session cookies, and PATs must never be committed.
Literal example keys are allowed only when the provider explicitly publishes
them for public use, with a source link and usage restrictions.

When the current free status is unclear, add the entry to
`data/excluded-and-unconfirmed.json`; do not inflate the reviewed catalog count.
