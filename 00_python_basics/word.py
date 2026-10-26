import csv
import math
from typing import Any, Dict, List, Optional


class ColumnSummary:
    """Stores statistical metadata for a single numeric column."""

    def __init__(self, name: str):
        self.name: str = name
        self.count: int = 0
        self.null_count: int = 0
        self.mean: float = 0.0
        self.std_dev: float = 0.0


class DataQualityAuditor:
    """Audits tabular datasets for missing values, schema violations, and statistical anomalies."""

    def __init__(self, expected_schema: Dict[str, type]):
        self.expected_schema: Dict[str, type] = expected_schema
        self.column_summaries: Dict[str, ColumnSummary] = {}
        self.audit_log: List[Dict[str, Any]] = []

    def _parse_row(self, row: Dict[str, str]) -> Dict[str, Any]:
        """Validates and coerces a single raw row against the expected schema."""
        parsed_row: Dict[str, Any] = {}
        for col, col_type in self.expected_schema.items():
            raw_val = row.get(col, "").strip()

            if not raw_val:
                parsed_row[col] = None
                continue

            try:
                parsed_row[col] = col_type(raw_val)
            except (ValueError, TypeError):
                parsed_row[col] = None  # Failed type casting flagged as null

        return parsed_row

    def _compute_numeric_statistics(self, parsed_data: List[Dict[str, Any]]) -> None:
        """Calculates mean and standard deviation for numeric columns."""
        for col, col_type in self.expected_schema.items():
            if col_type not in (int, float):
                continue

            summary = ColumnSummary(name=col)
            valid_vals = [
                row[col] for row in parsed_data if row[col] is not None
            ]

            summary.null_count = len(parsed_data) - len(valid_vals)
            summary.count = len(valid_vals)

            if valid_vals:
                summary.mean = sum(valid_vals) / len(valid_vals)
                variance = sum((x - summary.mean) ** 2 for x in valid_vals) / (
                    len(valid_vals) or 1
                )
                summary.std_dev = math.sqrt(variance)

            self.column_summaries[col] = summary

    def audit(self, records: List[Dict[str, str]]) -> Dict[str, Any]:
        """Runs full audit: schema check, null detection, and z-score anomaly flagging."""
        parsed_rows = [self._parse_row(r) for r in records]
        self._compute_numeric_statistics(parsed_rows)

        clean_records: List[Dict[str, Any]] = []
        flagged_records: List[Dict[str, Any]] = []

        for idx, row in enumerate(parsed_rows):
            row_issues: List[str] = []

            for col, val in row.items():
                if val is None:
                    row_issues.append(f"Missing/Invalid value in '{col}'")
                elif self.expected_schema[col] in (int, float):
                    stat = self.column_summaries[col]
                    if stat.std_dev > 0:
                        z_score = abs(val - stat.mean) / stat.std_dev
                        if z_score > 2.5:  # Anomaly threshold
                            row_issues.append(
                                f"Outlier in '{col}' (Value: {val}, Z: {z_score:.2f})"
                            )

            if row_issues:
                flagged_records.append(
                    {
                        "row_index": idx + 1,
                        "data": row,
                        "reasons": row_issues,
                    }
                )
            else:
                clean_records.append(row)

        return {
            "total_records": len(records),
            "clean_count": len(clean_records),
            "flagged_count": len(flagged_records),
            "flagged_details": flagged_records,
            "summaries": {
                c: {
                    "mean": round(s.mean, 2),
                    "std": round(s.std_dev, 2),
                    "nulls": s.null_count,
                }
                for c, s in self.column_summaries.items()
            },
        }