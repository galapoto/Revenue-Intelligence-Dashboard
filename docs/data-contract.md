# Suggested source audit contract (portfolio extension)

The original course's proprietary field dictionary and raw CSV files are **not included**. Do not assert these illustrative field names match Udacity starter files.

| Domain | Expected concept | Suggested key-level check |
|---|---|---|
| Marketing | campaign, lead ID, attributed revenue, spend | count distinct lead IDs; inspect duplicate rows; validate ROI numerator/denominator |
| CRM | opportunity ID, status history, close date, deal amount, region | separate **opportunity grain** from stage-history rows; compute won value only on defined terminal record |
| Support | ticket ID, account ID, priority, opened/closed dates | distinguish imported rows vs distinct ticket IDs; validate resolution-time formula |
| Unification | account identifier (if demonstrably shared) | aggregate each domain to account grain before join, then test key coverage |

Example audit command (replace columns with your actual CSV headers):

```bash
python src/audit.py support-export.csv --id-column ticket_id --numeric-column resolution_hours
```

**Privacy:** Audit runs locally and prints aggregate checks; no upload or external AI API. Never commit employer/client datasets or credentials.
