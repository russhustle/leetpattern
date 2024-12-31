---
comments: true
---

# Binary Search

![bs_memes](../imgs/binary_search_memes.png){width=300px}

-   Binary search is a search algorithm that finds the position of a target value within a sorted array.
-   Prerequisites: sorted array
    -   **We need to sort the array before applying binary search if it is not sorted.**
-   Time Complexity: $O(\log{N})$
-   Space Complexity: $O(1)$

## LeetCode Problems

1. 0704 - [Binary Search](https://leetcode.com/problems/binary-search/) (Easy)
2. 0035 - [Search Insert Position](https://leetcode.com/problems/search-insert-position/) (Easy)
3. 0278 - [First Bad Version](https://leetcode.com/problems/first-bad-version/) (Easy)
4. 0034 - [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) (Medium)
5. 0367 - [Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/) (Easy)
6. 0875 - [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) (Medium)
7. 1011 - [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) (Medium)
8. 0378 - [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) (Medium)

## 704. Binary Search

-   Implement binary search algorithm.

=== "Python"

    ```python
    --8<-- "0704_binary_search.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0704_binary_search.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0704_binary_search.ts"
    ```

## 35. Search Insert Position

-   Return the index of the target if it is found. If not, return the index where it would be if it were inserted in order.

=== "Python"

    ```python
    --8<-- "0035_search_insert_position.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0035_search_insert_position.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0035_search_insert_position.ts"
    ```

## 278. First Bad Version

-   Find the first bad version given a function `isBadVersion`.

=== "Python"

    ```python
    --8<-- "0278_first_bad_version.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0278_first_bad_version.cc"
    ```

## 34. Find First and Last Position of Element in Sorted Array

-   Find the starting and ending position of a given target value in a sorted array.

=== "Python"

    ```python
    --8<-- "0034_find_first_and_last_position_of_element_in_sorted_array.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0034_find_first_and_last_position_of_element_in_sorted_array.cc"
    ```

## 367. Valid Perfect Square

-   Determine if a positive integer is a perfect square without using any built-in library function.

=== "Python"

    ```python
    --8<-- "0367_valid_perfect_square.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0367_valid_perfect_square.cc"
    ```

## 875. Koko Eating Bananas

-   Koko loves to eat bananas. She wants to eat all the bananas within `H` hours. Each pile has a number of bananas. The `i-th` pile has `piles[i]` bananas. Return the minimum integer `K` such that she can eat all the bananas within `H` hours.

=== "Python"

    ```python
    --8<-- "0875_koko_eating_bananas.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0875_koko_eating_bananas.cc"
    ```

## 1011. Capacity To Ship Packages Within D Days

-   A conveyor belt has packages that must be shipped from one port to another within `D` days. The `i-th` package has a weight of `weights[i]`. Each day, we load the ship with packages on the conveyor belt. The ship will be loaded with packages up to its capacity. The ship will not be loaded beyond its capacity. Return the least weight capacity of the ship.

=== "Python"

    ```python
    --8<-- "1011_capacity_to_ship_packages_within_d_days.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/1011_capacity_to_ship_packages_within_d_days.cc"
    ```

## 378. Kth Smallest Element in a Sorted Matrix

-   Given an `n x n` matrix where each of the rows and columns are sorted in ascending order, return the `k-th` smallest element in the matrix.

=== "Python"

    ```python
    --8<-- "0378_kth_smallest_element_in_a_sorted_matrix.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0378_kth_smallest_element_in_a_sorted_matrix.cc"
    ```

## Appendix

### Binary Search Template

Three ways to implement binary search

1. `[left, right]` ← Most common
2. `[left, right)`
3. Recursive

```python
--8<-- "template/binary_search.py"
```

### bisect Usage [To be updated]

```python
--8<-- "template/bisect_usage.py"
```
