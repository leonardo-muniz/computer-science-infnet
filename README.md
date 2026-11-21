# TP2 - Algorithm Analysis and Data Structures

> Comparative study of algorithmic complexity, optimization techniques, hash tables, stacks, queues, and elementary sorting algorithms.

## Overview

This project was developed as part of the **TP2 (Teste de Performance 2)** assignment and focuses on the practical application of fundamental Computer Science concepts, including:

- Algorithm analysis
- Complexity evaluation using Big O notation
- Code optimization
- Hash tables
- Stacks
- Queues
- Sorting algorithms
- Instrumentation and performance measurement

The objective is not only to produce correct solutions but also to evaluate their efficiency, scalability, and computational cost.

---

## Learning Objectives

This project explores the relationship between theoretical complexity and observed behavior through a series of exercises involving:

- Identification of algorithmic bottlenecks
- Optimization of quadratic solutions
- Efficient use of hash tables
- Sequential processing with stacks and queues
- Sorting algorithm instrumentation
- Collision analysis in hash functions

---

## Repository Structure

```text
.
├── README.md
└── src/
    ├── ex01_unique_max.py
    ├── ex02_array_intersection.py
    ├── ex03_first_duplicate.py
    ├── ex04_missing_letter.py
    ├── ex05_first_non_repeated.py
    ├── ex06_selection_sort.py
    ├── ex07_insertion_sort.py
    ├── ex08_stack_vs_queue.md
    ├── ex09_stack.py
    ├── ex10_queue.py
    ├── ex11_reverse_string.py
    └── ex12_hash_analysis.md
```

---

## Exercises

### Exercise 01

#### Largest Unique Number

Comparison between:
- Quadratic solution using nested loops
- Optimized solution using a hash table

Metrics collected:
- Comparisons
- Hash accesses

Complexities:
- Quadratic Approach: O(n²)
- Hash Table Approach: O(n)

### Exercise 02

#### Array Intersection in Linear Time

Intersection between two arrays without using built-in set intersection operations.

Technique:
- Hash table lookup

Complexity:
- O(n + m)

### Exercise 03

#### First Duplicate Detection

Identification of the first duplicated value while preserving processing order.

Technique:
- Hash table for visited elements

Complexity:
- O(n)

### Exercise 04

#### Missing Alphabet Letter

Detection of a missing character in the English alphabet.

Requirements:
- Ignore punctuation
- Ignore whitespace
- Ignore case

Complexity:
- O(n)

### Exercise 05

#### First Non-Repeated Character

Frequency analysis while preserving original order.

Technique:
- Frequency counting
- Sequential verification

Complexity:
- O(n)

### Exercise 06

#### Selection Sort Analysis

Implementation of Selection Sort with instrumentation.

Collected metrics:
- Comparisons
- Swaps

Complexity:
- Best Case: O(n²)
- Average: O(n²)
- Worst Case: O(n²)

### Exercise 07

#### Insertion Sort Analysis

Implementation of Insertion Sort with instrumentation.

Collected metrics:
- Comparisons
- Shifts

Complexity:
- Best Case: O(n)
- Average: O(n²)
- Worst Case: O(n²)

### Exercise 08

#### Stack vs Queue

Technical justification for selecting the appropriate structure in a first-come-first-served processing system.

Topics covered:
- FIFO
- LIFO
- Operational complexity
- Real-world applications

### Exercise 09

#### Stack Implementation

Array-based stack implementation featuring:
- Fixed capacity
- Overflow handling
- Underflow handling
- State tracking

Operations:
- push()
- pop()

Complexity:
- O(1)

### Exercise 10

#### Queue Implementation

Circular queue implementation with explicit pointer management.

Features:
- Fixed capacity
- Front pointer
- Rear pointer
- FIFO validation

Operations:
- enqueue()
- dequeue()

Complexity:
- O(1)

### Exercise 11

#### String Reversal Using a Stack

String reversal without slicing or built-in reverse operations.

Technique:
- Explicit push/pop operations

Complexity:
- O(n)

### Exercise 12

#### Hash Function Analysis

Comparative analysis of three hash functions:
- h₁(k) = k mod M
- h₂(k) = (k × 7) mod M
- h₃(k) = k² mod M

Topics covered:
- Distribution quality
- Collision probability
- Bucket utilization
- Computational implications

---

## Complexity Summary

| Exercise	   | Main Complexity  |
| ------------ | ---------------- |
| Ex01 (Naive) | O(n²)            |
| Ex01 (Hash)  | O(n)             |
| Ex02         | O(n + m)         |
| Ex03         | O(n)             |
| Ex04         | O(n)             |
| Ex05         | O(n)             |
| Ex06         | O(n²)            |
| Ex07         | Best Case	O(n)  |
| Ex07         | Worst Case	O(n²) |
| Ex09         | O(1)             |
| Ex10         | O(1)             |
| Ex11         | O(n)             |

---

## Running the Code

Examples:

```shell
python3 src/ex01_unique_max.py
python3 src/ex06_selection_sort.py
python3 src/ex09_stack.py
```

---

## Key Concepts Demonstrated

- Algorithm optimization
- Asymptotic analysis
- Big O notation
- Hash table design
- Collision analysis
- Sorting algorithms
- Linear-time solutions
- Data structure implementation
- State management
- Performance instrumentation

---

## Academic Context

This repository was developed as part of a practical study on:
- Data Structures
- Algorithms
- Computational Complexity
- Performance Analysis

The emphasis of the project is on understanding the trade-offs between correctness, efficiency, and scalability.

---

## Author

Leonardo Muniz — Software Engineering / Computer Science

---

## License

This repository is intended for educational and academic purposes.