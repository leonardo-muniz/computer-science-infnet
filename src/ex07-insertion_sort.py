"""
Exercise 07

Insertion Sort

Best Case:
    O(n)

Worst Case:
    O(n²)
"""

from dataclasses import dataclass


@dataclass
class Metrics:
    comparisons: int = 0
    shifts: int = 0


def insertion_sort(data):

    metrics = Metrics()

    for i in range(1, len(data)):

        key = data[i]

        j = i - 1

        while j >= 0:

            metrics.comparisons += 1

            if data[j] > key:

                metrics.shifts += 1

                data[j + 1] = data[j]

                j -= 1

            else:
                break

        data[j + 1] = key

    return data, metrics


def main():

    values = [9, 8, 7, 6, 5]

    sorted_values, metrics = (
        insertion_sort(values)
    )

    print(sorted_values)
    print(metrics)


if __name__ == "__main__":
    main()