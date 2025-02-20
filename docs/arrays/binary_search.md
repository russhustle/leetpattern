---
comments: true
---

# Binary Search

![bs_memes](../imgs/binary_search_memes.png){width=300px}

-   Binary search is a search algorithm that finds the position of a target value within a sorted array.
-   Prerequisites: sorted array
    -   **We need to sort the array before applying binary search if it is not sorted.**
-   Time Complexity: O(logN)
-   Space Complexity: O(1)

```python title="template/binary_search.py"
--8<-- "template/binary_search.py"
```

## LeetCode Problems

1. 0704 - [Binary Search](https://leetcode.com/problems/binary-search/) | [二分查找](https://leetcode.cn/problems/binary-search/) (Easy)
2. 0035 - [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | [搜索插入位置](https://leetcode.cn/problems/search-insert-position/) (Easy)
3. 0278 - [First Bad Version](https://leetcode.com/problems/first-bad-version/) | [第一个错误的版本](https://leetcode.cn/problems/first-bad-version/) (Easy)
4. 0034 - [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | [在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/) (Medium)
5. 0367 - [Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/) | [有效的完全平方数](https://leetcode.cn/problems/valid-perfect-square/) (Easy)
6. 0875 - [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | [爱吃香蕉的珂珂](https://leetcode.cn/problems/koko-eating-bananas/) (Medium)
7. 1011 - [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | [在 D 天内送达包裹的能力](https://leetcode.cn/problems/capacity-to-ship-packages-within-d-days/) (Medium)
8. 0378 - [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | [有序矩阵中第 K 小的元素](https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/) (Medium)

## 367. Valid Perfect Square

=== "Python"

    ```python
    --8<-- "0367_valid_perfect_square.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0367_valid_perfect_square.cc"
    ```

## 875. Koko Eating Bananas

=== "Python"

    ```python
    --8<-- "0875_koko_eating_bananas.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0875_koko_eating_bananas.cc"
    ```

## 1011. Capacity To Ship Packages Within D Days

=== "Python"

    ```python
    --8<-- "1011_capacity_to_ship_packages_within_d_days.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/1011_capacity_to_ship_packages_within_d_days.cc"
    ```

## 378. Kth Smallest Element in a Sorted Matrix

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
