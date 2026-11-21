"""
Exercise 06

Selection Sort

Time Complexity:
    O(n²)

Space Complexity:
    O(1)
"""

from dataclasses import dataclass


@dataclass
class Metrics:
    comparisons: int = 0
    swaps: int = 0


def selection_sort(data: list[int]):

    metrics = Metrics()

    n = len(data)

    for i in range(n):

        min_idx = i

        for j in range(i + 1, n):

            metrics.comparisons += 1

            if data[j] < data[min_idx]:
                min_idx = j

        if min_idx != i:

            metrics.swaps += 1

            data[i], data[min_idx] = (
                data[min_idx],
                data[i]
            )

    return data, metrics


def main():

    values = [64, 25, 12, 22, 11]

    sorted_values, metrics = (
        selection_sort(values)
    )

    print(sorted_values)
    print(metrics)


if __name__ == "__main__":
    main()