# Revenue Intelligence Dashboard | Udacity + AWS QuickSuite

**Portfolio evidence — NovaTech Solutions (fictional B2B SaaS scenario)**

**Business problem:** Revenue Operations needs marketing, CRM and support information in one decision-support experience, instead of manually collecting Monday reports.

**What I built during the course (3 Nov 2026):** an Amazon QuickSuite three-sheet dashboard (Marketing Funnel, Sales Pipeline, Customer Health), field transformations, calculated metrics, an account-grain unified preview, a published Quick Chat Topic and an executive review. The documented screen captures and final brief are transcribed in [Course evidence](docs/course-evidence.md). Native QuickSuite assets are hosted separately; this repository does **not** recreate or prove live QuickSuite access.

### Observed QuickSuite results (not raw-data-validated)
| Marketing | CRM / sales | Support |
|---|---|---|
| 2,240 distinct leads | $707,201 displayed closed-won value | 3,000 imported rows / 2,996 distinct ticket IDs |
| Campaign-response ranking documented | 315 Won, 184 Lost stage entries vs 496 distinct opportunities | 85 monitored accounts |
| ROI interpretation requires validation | **Win-rate denominator not reconciled** | Duplicate ticket IDs require follow-up |

The displayed 63.51% win rate is 315 / 496; it is **not independently reconciled** to the 499 Won/Lost stage entries. No verified lead-to-sale or support-to-sale key is established. Do not interpret cross-domain patterns as causal.

### Recruiter walkthrough
1. Read [Executive brief](docs/executive-brief.md) — problem, approach, measured results and caveats.
2. Read [Course evidence / verification log](docs/course-evidence.md) — recorded source/Quick Chat outcomes and limitations.
3. Review [Data quality audit](src/audit.py) and [unit tests](tests/test_audit.py) — independently runnable quality checks. These are **post-course portfolio extensions**, not claimed as native QuickSuite ETL.
4. See [Evidence checklist](docs/evidence-checklist.md) for original screenshot/export items still to add.

### Local independent audit (Python standard library only)
```bash
python -m unittest discover -s tests -v
python src/audit.py path/to/export.csv --id-column ticket_id
```

Course project: Udacity *AWS Agentic AI Business Professional*. Amazon QuickSuite is a tool used in the course; the Udacity Nanodegree is **not an AWS-issued professional certification**.

**Evidence integrity:** Fictional course organization, real applicant coursework. Figures above are taken from a 3 November 2026 screenshot-based evidence log, not from a raw-data rerun. No source CSV or employer data is published.
