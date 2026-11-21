# Linux Filesystem Sorting and Data Structures Benchmark

An experimental benchmark that uses local Linux filesystem paths to evaluate three classical sorting algorithms and three fundamental data structures.

## Overview

The project generates a dataset containing file paths, runs the benchmarks on that dataset, and exports the measurements as CSV and Markdown reports.

The experiments measure:

- Bubble Sort, Selection Sort, and Insertion Sort execution time.
- Comparison and swap counts for sorting algorithms.
- Memory usage during sorting and data structure operations.
- Hashtable, Stack, and Queue loading and insertion/removal performance.
- Selected file paths at fixed positions in the dataset.

---

## Dataset

`run_benchmark.sh` walks `/` and stores absolute file paths in `data/file_list.txt`.

The dataset is always limited to **10,000 records**. This keeps the quadratic sorting benchmarks practical to run on a local machine.

Example entries:

```text
/bin/bash
/bin/ls
/etc/hosts
/usr/bin/python3
```

The list is regenerated each time `run_benchmark.sh` is executed.

---

## Project Structure

```text
.
├── README.md
├── run_benchmark.sh          # Generate data and run both benchmarks
├── report.sh                 # Generate the Markdown benchmark report
├── data/
│   └── file_list.txt         # Generated filesystem dataset
├── src/
│   ├── dataset.py            # Shared dataset loader
│   ├── sorting_benchmark.py  # Sorting implementations and benchmark
│   └── data_structures_benchmark.py
├── results/
│   ├── sorting_results.csv
│   └── structures_results.csv
├── logs/
│   ├── sorting.log
│   └── structures.log
└── report/
    └── benchmark_report.md
```

---

## Sorting Algorithms

| Algorithm | Best case | Average case | Worst case |
| --- | ---: | ---: | ---: |
| Bubble Sort | O(n²) | O(n²) | O(n²) |
| Selection Sort | O(n²) | O(n²) | O(n²) |
| Insertion Sort | O(n) | O(n²) | O(n²) |

The sorting benchmark runs each algorithm five times and records:

- Average execution time.
- Average peak memory usage measured with `tracemalloc`.
- Comparison count.
- Swap or shift count.
- Number of records processed.

---

## Data Structures

### Hashtable

Implemented with Python's built-in dictionary, with integer keys mapped to file paths.

### Stack

Implemented with a Python list. The benchmark evaluates loading, insertion at the end, and removal from the end.

### Queue

Implemented with `collections.deque`. The benchmark evaluates loading, insertion at the end, and removal from the beginning.

For each structure, the benchmark records:

- Dataset loading time and peak memory usage.
- Insertion time and peak memory usage.
- Removal time and peak memory usage.
- File paths located at positions 1, 100, 1,000, 5,000, and the last available position.

---

## Requirements

- Linux
- Python 3.10 or newer
- Bash

The benchmarks use only the Python standard library.

---

## Running the Project

Make the scripts executable and run the complete benchmark:

```bash
chmod +x run_benchmark.sh report.sh
./run_benchmark.sh
```

The runner:

1. Creates the `data`, `results`, `logs`, and `src` directories.
2. Generates at most 10,000 filesystem file paths.
3. Runs the sorting benchmark.
4. Runs the data structures benchmark.
5. Saves logs and CSV results.

To run an individual benchmark:

```bash
python3 src/sorting_benchmark.py
python3 src/data_structures_benchmark.py
```

Direct execution defaults to at most 10,000 records.

---

## Record Limit

Both Python benchmarks support the `BENCHMARK_MAX_RECORDS` environment variable.

```bash
# Benchmark 2,000 records
BENCHMARK_MAX_RECORDS=2000 ./run_benchmark.sh

# Use all records in data/file_list.txt
BENCHMARK_MAX_RECORDS=0 ./run_benchmark.sh
```

Setting the limit to `0` allows the entire current dataset to be used. Positive values are passed to the shared dataset loader and truncated safely.

> Warning: using a large dataset with Bubble Sort or Selection Sort can take a very long time because both have quadratic worst-case and average-case complexity.

---

## Generating the Report

After the benchmarks produce both CSV files, generate `report/benchmark_report.md`:

```bash
./report.sh
```

The report script uses only Python's standard library and does not require pandas or matplotlib.

---

## Output Files

| Output | Description |
| --- | --- |
| `data/file_list.txt` | Absolute filesystem paths, capped at 10,000 lines |
| `results/sorting_results.csv` | Sorting time, memory, comparisons, and swaps |
| `results/structures_results.csv` | Data structure load and operation measurements |
| `logs/sorting.log` | Sorting benchmark console output |
| `logs/structures.log` | Data structure benchmark console output |
| `report/benchmark_report.md` | Markdown summary of the CSV results |

---

## Author

Leonardo Muniz — Software Engineering / Computer Science

---

## License

This repository is intended for educational and research purposes.
