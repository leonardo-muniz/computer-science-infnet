from pathlib import Path
from dataset import load_dataset
from collections import deque
import csv
import os
import time
import tracemalloc

RESULTS = Path(__file__).resolve().parent.parent / "results" / "structures_results.csv"
DEFAULT_MAX_RECORDS = 10_000


def benchmark_structure(name, builder, dataset):

    tracemalloc.start()

    start = time.perf_counter()

    structure = builder(dataset)

    end = time.perf_counter()

    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return structure, {
        "structure": name,
        "load_time_seconds": end - start,
        "load_memory_bytes": peak,
    }


def build_hashtable(dataset): return {i: value for i, value in enumerate(dataset)}

def build_stack(dataset): return list(dataset)

def build_queue(dataset): return deque(dataset)

def lookup_positions(data):

    positions = [
        0,
        99,
        999,
        4999,
        len(data) - 1,
    ]

    result = {}

    for pos in positions:
        if pos < len(data):
            result[pos + 1] = data[pos]

    return result


def benchmark_operations(name, structure):

    results = {}

    # INSERT

    tracemalloc.start()

    start = time.perf_counter()

    if name == "Hashtable":
        structure[len(structure)] = "benchmark_insert"

    elif name == "Stack":
        structure.append("benchmark_insert")

    elif name == "Queue":
        structure.append("benchmark_insert")

    insert_time = time.perf_counter() - start

    _, insert_mem = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    # DELETE

    tracemalloc.start()

    start = time.perf_counter()

    if name == "Hashtable":
        del structure[max(structure.keys())]

    elif name == "Stack":
        structure.pop()

    elif name == "Queue":
        structure.popleft()

    delete_time = time.perf_counter() - start

    _, delete_mem = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    results["insert_time"] = insert_time
    results["insert_memory"] = insert_mem
    results["delete_time"] = delete_time
    results["delete_memory"] = delete_mem

    return results


def save_results(results):

    RESULTS.parent.mkdir(exist_ok=True)

    with open(RESULTS, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "structure",
                "load_time_seconds",
                "load_memory_bytes",
                "insert_time",
                "insert_memory",
                "delete_time",
                "delete_memory",
            ],
        )

        writer.writeheader()
        writer.writerows(results)


def main():

    max_records = int(os.environ.get("BENCHMARK_MAX_RECORDS", DEFAULT_MAX_RECORDS))
    dataset = load_dataset(None if max_records == 0 else max_records)

    structures = [
        ("Hashtable", build_hashtable),
        ("Stack", build_stack),
        ("Queue", build_queue),
    ]

    results = []

    print(f"\nDataset carregado: {len(dataset)} arquivos\n")

    for name, builder in structures:

        structure, metrics = benchmark_structure(
            name,
            builder,
            dataset,
        )

        if name == "Hashtable":
            access_data = [structure[i] for i in range(len(dataset))]
        else:
            access_data = list(structure)

        positions = lookup_positions(access_data)

        print(f"\n{name}")
        print("-" * 40)

        for position, file_name in positions.items():
            print(f"Posição {position}: {file_name}")

        operation_metrics = benchmark_operations(
            name,
            structure,
        )

        metrics.update(operation_metrics)

        results.append(metrics)

        print(
            f"Carga: {metrics['load_time_seconds']:.6f}s"
        )

        print(
            f"Memória: {metrics['load_memory_bytes']/1024:.2f} KB"
        )

        print(
            f"Inserção: {metrics['insert_time']:.9f}s"
        )

        print(
            f"Remoção: {metrics['delete_time']:.9f}s"
        )

    save_results(results)

    print(f"\nResultados salvos em: {RESULTS}")


if __name__ == "__main__": main()