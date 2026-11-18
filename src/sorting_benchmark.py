from pathlib import Path
from dataset import load_dataset
from dataclasses import dataclass
import copy
import csv
import os
import statistics
import time
import tracemalloc

RESULTS = Path(__file__).resolve().parent.parent / "results" / "sorting_results.csv"

RUNS = 5
DEFAULT_MAX_RECORDS = 10_000


@dataclass
class SortMetrics:
    comparisons: int = 0
    swaps: int = 0


def bubble_sort(data):
    metrics = SortMetrics()

    n = len(data)

    for i in range(n):
        for j in range(n - i - 1):

            metrics.comparisons += 1

            if data[j] > data[j + 1]:
                metrics.swaps += 1
                data[j], data[j + 1] = data[j + 1], data[j]

    return metrics


def selection_sort(data):
    metrics = SortMetrics()

    n = len(data)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):

            metrics.comparisons += 1

            if data[j] < data[min_idx]:
                min_idx = j

        if min_idx != i:
            metrics.swaps += 1
            data[i], data[min_idx] = data[min_idx], data[i]

    return metrics


def insertion_sort(data):
    metrics = SortMetrics()

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0:

            metrics.comparisons += 1

            if data[j] > key:
                metrics.swaps += 1
                data[j + 1] = data[j]
                j -= 1
            else:
                break

        data[j + 1] = key

    return metrics


def benchmark(name, algorithm, dataset):

    times = []
    peaks = []
    comparisons = []
    swaps = []

    for _ in range(RUNS):

        data = copy.deepcopy(dataset)

        tracemalloc.start()

        start = time.perf_counter()

        metrics = algorithm(data)

        end = time.perf_counter()

        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        times.append(end - start)
        peaks.append(peak)
        comparisons.append(metrics.comparisons)
        swaps.append(metrics.swaps)

    return {
        "algorithm": name,
        "records": len(dataset),
        "avg_time_seconds": statistics.mean(times),
        "avg_memory_bytes": statistics.mean(peaks),
        "comparisons": statistics.mean(comparisons),
        "swaps": statistics.mean(swaps),
    }


def save_results(results):

    RESULTS.parent.mkdir(exist_ok=True)

    with open(RESULTS, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "algorithm",
                "records",
                "avg_time_seconds",
                "avg_memory_bytes",
                "comparisons",
                "swaps",
            ],
        )

        writer.writeheader()
        writer.writerows(results)


def main():

    max_records = int(os.environ.get("BENCHMARK_MAX_RECORDS", DEFAULT_MAX_RECORDS))
    dataset = load_dataset(None if max_records == 0 else max_records)

    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
    ]

    results = []

    print(f"\nDataset carregado: {len(dataset)} arquivos\n")

    for name, algorithm in algorithms:

        result = benchmark(name, algorithm, dataset)

        results.append(result)

        print(f"{name}")
        print(f"Tempo médio: {result['avg_time_seconds']:.6f}s")
        print(f"Memória média: {result['avg_memory_bytes']/1024:.2f} KB")
        print(f"Comparações: {int(result['comparisons'])}")
        print(f"Trocas: {int(result['swaps'])}")
        print()

    save_results(results)

    print(f"Resultados salvos em: {RESULTS}")


if __name__ == "__main__": main()