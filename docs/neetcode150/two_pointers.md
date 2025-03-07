---
comments: True
---

# Two Pointers

- [x] [125. Valid Palindrome](https://leetcode.cn/problems/valid-palindrome/) (Easy)
- [x] [167. Two Sum II - Input Array Is Sorted](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/) (Medium)
- [x] [15. 3Sum](https://leetcode.cn/problems/3sum/) (Medium)
- [x] [11. Container With Most Water](https://leetcode.cn/problems/container-with-most-water/) (Medium)
- [x] [42. Trapping Rain Water](https://leetcode.cn/problems/trapping-rain-water/) (Hard)

## 125. Valid Palindrome

-   [LeetCode](https://leetcode.com/problems/valid-palindrome/) | [LeetCode CH](https://leetcode.cn/problems/valid-palindrome/) (Easy)

-   Tags: two pointers, string

```python title="125. Valid Palindrome - Python Solution"
--8<-- "0125_valid_palindrome.py"
```

## 167. Two Sum II - Input Array Is Sorted

-   [LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [LeetCode CH](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/) (Medium)

-   Tags: array, two pointers, binary search

```python title="167. Two Sum II - Input Array Is Sorted - Python Solution"
--8<-- "0167_two_sum_ii_input_array_is_sorted.py"
```

## 15. 3Sum

-   [LeetCode](https://leetcode.com/problems/3sum/) | [LeetCode CH](https://leetcode.cn/problems/3sum/) (Medium)

-   Tags: array, two pointers, sorting

```python title="15. 3Sum - Python Solution"
--8<-- "0015_3sum.py"
```

```cpp title="15. 3Sum - C++ Solution"
--8<-- "cpp/0015_3sum.cc"
```

## 11. Container With Most Water

-   [LeetCode](https://leetcode.com/problems/container-with-most-water/) | [LeetCode CH](https://leetcode.cn/problems/container-with-most-water/) (Medium)

-   Tags: array, two pointers, greedy
-   Return the maximum area of water that can be trapped between the vertical lines.

![11](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg){width=300px}

```python title="11. Container With Most Water - Python Solution"
--8<-- "0011_container_with_most_water.py"
```

## 42. Trapping Rain Water

-   [LeetCode](https://leetcode.com/problems/trapping-rain-water/) | [LeetCode CH](https://leetcode.cn/problems/trapping-rain-water/) (Hard)

-   Tags: array, two pointers, dynamic programming, stack, monotonic stack
-   ![42](../assets/0042.png)

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZI2z5pq0TqA?si=OEYg01dbmzvmtIwZ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

| Approach   | Time | Space |
| ---------- | ---- | ----- |
| DP         | O(N) | O(N)  |
| Left Right | O(N) | O(1)  |
| Monotonic  | O(N) | O(N)  |

```python title="42. Trapping Rain Water - Python Solution"
--8<-- "0042_trapping_rain_water.py"
```

```cpp title="42. Trapping Rain Water - C++ Solution"
--8<-- "cpp/0042_trapping_rain_water.cc"
```
