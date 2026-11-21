"""
Exercise 01
Find the largest unique number.

Naive solution:
    Time Complexity: O(n²)

Optimized solution:
    Time Complexity: O(n)

Author: Seu Nome
"""

from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Metrics:
    comparisons: int = 0
    accesses: int = 0


def largest_unique_quadratic(numbers: list[int]):
    metrics = Metrics()

    largest = None

    for i in range(len(numbers)):

        count = 0

        for j in range(len(numbers)):
            metrics.comparisons += 1

            if numbers[i] == numbers[j]:
                count += 1

        if count == 1:
            if largest is None or numbers[i] > largest:
                largest = numbers[i]

    return largest, metrics


def largest_unique_hash(numbers: list[int]):
    metrics = Metrics()

    freq = defaultdict(int)

    for n in numbers:
        metrics.accesses += 1
        freq[n] += 1

    largest = None

    for n, count in freq.items():
        metrics.accesses += 1

        if count == 1:
            if largest is None or n > largest:
                largest = n

    return largest, metrics


def main():

    data = [5, 7, 3, 7, 9, 5, 11, 8, 8]

    result1, m1 = largest_unique_quadratic(data)
    result2, m2 = largest_unique_hash(data)

    print("\nQuadratic:")
    print("Result:", result1)
    print("Comparisons:", m1.comparisons)

    print("\nHash Table:")
    print("Result:", result2)
    print("Accesses:", m2.accesses)


if __name__ == "__main__":
    main()