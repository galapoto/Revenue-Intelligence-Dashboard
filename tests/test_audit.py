import csv
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from audit import inspect_csv, reconcile_stage_counts


class AuditTests(unittest.TestCase):
    def test_duplicates_blanks_and_invalid_numeric(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "support.csv"
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=["ticket_id", "hours"])
                writer.writeheader()
                writer.writerows([
                    {"ticket_id": "T1", "hours": "12.5"},
                    {"ticket_id": "T1", "hours": "unknown"},
                    {"ticket_id": "T2", "hours": ""},
                    {"ticket_id": "", "hours": "3"},
                ])
            report = inspect_csv(path, "ticket_id", ["hours"])
            self.assertEqual(report["rows"], 4)
            self.assertEqual(report["distinct_nonblank_ids"], 2)
            self.assertEqual(report["duplicate_id_rows"], 1)
            self.assertEqual(report["blank_ids"], 1)
            self.assertEqual(report["invalid_numeric"], {"hours": 1})

    def test_missing_column_is_error(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "bad.csv"
            path.write_text("a,b\n1,2\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Missing required columns"):
                inspect_csv(path, "missing")

    def test_novatech_discrepancy(self):
        result = reconcile_stage_counts(315, 184, 496)
        self.assertEqual(result["stage_rows"], 499)
        self.assertEqual(result["excess_stage_rows"], 3)
        self.assertEqual(result["displayed_style_win_rate_pct"], 63.51)
        self.assertEqual(result["stage_count_win_rate_pct"], 63.13)
        self.assertTrue(result["needs_reconciliation"])

    def test_invalid_stage_counts(self):
        with self.assertRaises(ValueError):
            reconcile_stage_counts(-1, 12, 4)


if __name__ == "__main__":
    unittest.main()
