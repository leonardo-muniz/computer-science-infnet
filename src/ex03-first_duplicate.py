"""
Exercise 03

First duplicate value.

Complexity:
    O(n)
"""

def first_duplicate(values: list[str]):

    visited = {}

    for value in values:

        if value in visited:
            return value

        visited[value] = True

    return None


def main():

    data = [
        "apple",
        "orange",
        "banana",
        "grape",
        "banana",
        "pear"
    ]

    print(first_duplicate(data))


if __name__ == "__main__":
    main()