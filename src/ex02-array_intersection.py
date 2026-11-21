"""
Exercise 02
Array intersection using hash table.

Complexity:
    O(n + m)
"""

from dataclasses import dataclass


@dataclass
class Metrics:
    accesses: int = 0


def intersection(a: list[int], b: list[int]):

    metrics = Metrics()

    table = {}

    for item in a:
        metrics.accesses += 1
        table[item] = True

    result = []

    for item in b:

        metrics.accesses += 1

        if item in table:
            result.append(item)

    return result, metrics


def main():

    a = [1, 2, 3, 4, 5]
    b = [3, 4, 5, 6, 7]

    result, metrics = intersection(a, b)

    print("Intersection:", result)
    print("Accesses:", metrics.accesses)


if __name__ == "__main__":
    main()