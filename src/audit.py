"""Small, stdlib-only CSV audit for data-quality evidence (portfolio extension)."""
import argparse
import csv
import json
from collections import Counter
from pathlib import Path


def inspect_csv(path, id_column, numeric_columns=()):
    """Audit row count, duplicate business IDs, blanks and non-numeric fields."""
    with Path(path).open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = reader.fieldnames or []
        required = [id_column, *numeric_columns]
        unknown = [column for column in required if column not in columns]
        if unknown:
            raise ValueError("Missing required columns: " + ", ".join(unknown))
        seen = Counter()
        rows = 0
        blank_ids = 0
        invalid_numeric = Counter()
        for row in reader:
            rows += 1
            identifier = (row.get(id_column) or "").strip()
            if identifier:
                seen[identifier] += 1
            else:
                blank_ids += 1
            for column in numeric_columns:
                value = (row.get(column) or "").strip()
                if value:
                    try:
                        float(value)
                    except ValueError:
                        invalid_numeric[column] += 1
    return {
        "rows": rows,
        "id_column": id_column,
        "distinct_nonblank_ids": len(seen),
        "duplicate_id_rows": sum(count - 1 for count in seen.values()),
        "blank_ids": blank_ids,
        "invalid_numeric": dict(invalid_numeric),
    }


def reconcile_stage_counts(won_stage_rows, lost_stage_rows, distinct_opportunities):
    """Flag stage-grain vs distinct-opportunity-grain mismatch explicitly."""
    if distinct_opportunities <= 0 or min(won_stage_rows, lost_stage_rows) < 0:
        raise ValueError("Expected nonnegative stage counts and positive distinct IDs")
    stage_rows = won_stage_rows + lost_stage_rows
    return {
        "stage_rows": stage_rows,
        "distinct_opportunities": distinct_opportunities,
        "excess_stage_rows": stage_rows - distinct_opportunities,
        "displayed_style_win_rate_pct": round(100 * won_stage_rows / distinct_opportunities, 2),
        "stage_count_win_rate_pct": round(100 * won_stage_rows / stage_rows, 2),
        "needs_reconciliation": stage_rows != distinct_opportunities,
    }


def main():
    parser = argparse.ArgumentParser(description="Audit a local CSV; does not upload any data")
    parser.add_argument("csv_path")
    parser.add_argument("--id-column", required=True)
    parser.add_argument("--numeric-column", action="append", default=[])
    args = parser.parse_args()
    print(json.dumps(inspect_csv(args.csv_path, args.id_column, args.numeric_column), indent=2))


if __name__ == "__main__":
    main()
