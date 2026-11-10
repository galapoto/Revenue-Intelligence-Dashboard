# Executive brief — NovaTech Revenue Intelligence

**Audience:** Sarah Chen, VP Revenue Operations (fictional course business case). **Evidence recorded:** 3 Nov 2026. **System:** Amazon QuickSuite.

## Business problem
Monday reporting required manual pulls from Marketing, CRM and Support sources. The goal was a self-service management view joining metrics at meaningful levels and enabling natural-language Q&A without confusing correlation with causation.

## Work completed in the course environment
- Three CSV datasets (Marketing **2,240 rows**, CRM **499 rows**, Support **3,000 rows**) imported into SPICE.
- Type checks, calculated fields (campaign ROI, time to close, support resolution duration) and join preview.
- Three-sheet published dashboard: **Marketing Funnel**, **Sales Pipeline**, **Customer Health**.
- A published `NovaTech Revenue Intelligence` Topic with relevant sources and grounding instructions.
- Screenshot-backed Q&A comparison and written recommendations.
- An **85-row account-grain unified output preview** is documented; a verified cross-domain production join is **not established**.

## Four findings and their limits
| Domain | Observed dashboard value | Decision implication |
|---|---|---|
| Marketing | 2,240 distinct leads; campaign response leaders include NovaPulse Launch **35.21%**, Digital Retarget **34.84%**, Q3 Growth Sprint **32.93%** | Validate campaign attribution and ROI definitions before reallocating spend |
| Sales | **$707,201** displayed closed-won value: Central **$274,285**, West **$248,243**, East **$184,673** | Central leads recorded regional performance; do not infer cause |
| Sales quality | 315 Won + 184 Lost stage entries = **499**, while opportunities are **496 distinct IDs** | Displayed **63.51%** win rate uses 315/496; stage duplication/history needs reconciliation |
| Support | 3,000 rows, **2,996 distinct tickets**, **85 accounts** | Investigate duplicate identifiers, severity definitions and missing resolution fields |

## What AI added — and what it did not
The published Topic and prior generic Quick Chat responses agreed on three repeated KPIs: 2,240 leads, $707,201 won revenue and 2,996 unique tickets. That is evidence of **consistent responses in those examples**, not proof that creating a Topic improved model accuracy. Cross-domain answers disclosed unverified joins and causal claims rather than inventing direct links.

## Recommended next steps
1. Reconcile opportunity ID grain (496) against stage entries (499) before endorsing win rate.
2. Validate marketing cost/revenue attribution and campaign response formulas at row level.
3. Assess support duplicate IDs and resolution semantics.
4. Verify account-level join keys and visual use of the unified dataset before claiming customer-journey analytics.
5. Preserve original screenshots, raw file version hashes and before/after Topic evidence.

**No real employer or customer data is disclosed.** Findings summarize the author's prior screenshot-based coursework; raw CSV data were not supplied to this public repository.
