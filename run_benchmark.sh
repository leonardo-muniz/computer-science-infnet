#!/usr/bin/bash

set -euo pipefail

PROJECT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

DATA_DIR="$PROJECT_ROOT/data"
RESULTS_DIR="$PROJECT_ROOT/results"
SRC_DIR="$PROJECT_ROOT/src"
LOG_DIR="$PROJECT_ROOT/logs"

mkdir -p \
    "$DATA_DIR" \
    "$RESULTS_DIR" \
    "$SRC_DIR" \
    "$LOG_DIR"

echo "==================================="
echo " Linux Benchmark Project"
echo "==================================="

echo
echo "[1/4] Generating filesystem dataset..."

python3 - "$DATA_DIR/file_list.txt" <<'PY'
import os
import sys

output = sys.argv[1]
count = 0

with open(output, "w", encoding="utf-8") as file:
    for root, directories, filenames in os.walk("/", followlinks=False):
        directories.sort()
        for filename in sorted(filenames):
            file.write(os.path.join(root, filename))
            file.write("\n")
            count += 1
            if count == 10_000:
                break
        if count == 10_000:
            break
PY

FILE_COUNT=$(wc -l < "$DATA_DIR/file_list.txt")

echo "Files found: $FILE_COUNT"

if [ "$FILE_COUNT" -lt 5000 ]; then
    echo "WARNING: Dataset contains fewer than 5000 files."
fi

echo
echo "[2/4] Running sorting benchmark..."

python3 "$SRC_DIR/sorting_benchmark.py" \
    | tee "$LOG_DIR/sorting.log"

echo
echo "[3/4] Running data structures benchmark..."

python3 "$SRC_DIR/data_structures_benchmark.py" \
    | tee "$LOG_DIR/structures.log"

echo
echo "[4/4] Generated artifacts"

echo
echo "Dataset:"
echo "  $DATA_DIR/file_list.txt"

echo
echo "Results:"
echo "  $RESULTS_DIR/sorting_results.csv"
echo "  $RESULTS_DIR/structures_results.csv"

echo
echo "Logs:"
echo "  $LOG_DIR/sorting.log"
echo "  $LOG_DIR/structures.log"

echo
echo "Done."