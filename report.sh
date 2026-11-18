#!/usr/bin/env bash

set -euo pipefail

PROJECT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

python3 - "$PROJECT_ROOT" <<'PY'
import csv
import sys
from pathlib import Path

root = Path(sys.argv[1])
results = root / "results"
report_dir = root / "report"
report_dir.mkdir(exist_ok=True)


def read_results(path):
    with path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def markdown_table(rows):
    if not rows:
        return "_No results available._\n"

    columns = list(rows[0])
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]
    lines.extend(
        "| " + " | ".join(row[column] for column in columns) + " |"
        for row in rows
    )
    return "\n".join(lines) + "\n"


sorting = read_results(results / "sorting_results.csv")
structures = read_results(results / "structures_results.csv")

report = report_dir / "benchmark_report.md"
with report.open("w", encoding="utf-8") as file:
    file.write("# Benchmark Report\n\n")
    file.write("## Dataset\n\n")
    file.write(f"Total records: {sorting[0]['records']}\n\n")
    file.write("## Sorting Algorithms\n\n")
    file.write(markdown_table(sorting))
    file.write("\n## Data Structures\n\n")
    file.write(markdown_table(structures))

print(f"Report generated: {report}")
PY

echo
echo "Report generated in report/"
