# 0x1E. Search Algorithms

Welcome to my project on Search Algorithms, a key milestone in my journey through the ALX Software Engineering program!

## Learning Objectives

By the end of this project, I am able to explain the following concepts clearly and confidently:

- What a search algorithm is
- What a linear search is
- What a binary search is
- How to choose the best search algorithm based on specific needs

## Requirements

- **General:**
  - Editors used: `vi`, `vim`, `emacs`
  - Compilation: All files were compiled on Ubuntu 20.04 LTS using `gcc`, with the options `-Wall -Werror -Wextra -pedantic -std=gnu89`
  - File Format: All files end with a new line
  - A `README.md` file at the root of the project directory is mandatory
  - Code Style: Code follows the Betty style, checked with `betty-style.pl` and `betty-doc.pl`
  - No global variables were used
  - No more than 5 functions per file
  - Only the `printf` function from the standard library was used; other functions like `strdup`, `malloc`, etc., were not used
  - Prototype Declarations: All function prototypes are included in the header file `search_algos.h`, and the header file is include guarded

## Tasks

### 0. Linear search (mandatory)

- **Prototype:** `int linear_search(int *array, size_t size, int value);`
- This function searches for a value in an array of integers using the linear search algorithm.
- It prints each value checked during the search.
- It returns the first index where the value is located or `-1` if the value is not present or the array is `NULL`.

### 1. Binary search (mandatory)

- **Prototype:** `int binary_search(int *array, size_t size, int value);`
- This function searches for a value in a sorted array of integers using the binary search algorithm.
- Assumes that the array is sorted in ascending order.
- Prints the array being searched each time it changes.
- Returns the index where the value is located or `-1` if the value is not present or the array is `NULL`.

### 2. Big O #0 (mandatory)

- Determine the time complexity (worst case) of a linear search in an array of size `n`.

### 3. Big O #1 (mandatory)

- Determine the space complexity (worst case) of an iterative linear search algorithm in an array of size `n`.

### 4. Big O #2 (mandatory)

- Determine the time complexity (worst case) of a binary search in an array of size `n`.

### 5. Big O #3 (mandatory)

- Determine the space complexity (worst case) of a binary search in an array of size `n`.

### 6. Big O #4 (mandatory)

- Determine the space complexity of the function `allocate_map(int n, int m)`.

### 7. Jump search (advanced)

- **Prototype:** `int jump_search(int *array, size_t size, int value);`
- This function searches for a value in a sorted array of integers using the jump search algorithm.
- Assumes that the array is sorted in ascending order.
- Uses the square root of the array size as the jump step.
- Prints each value checked during the search.
- Returns the first index where the value is located or `-1` if the value is not present or the array is `NULL`.

## Repository

- **GitHub Repository:** `alx-low_level_programming`
- **Directory:** `0x1E-search_algorithms`
