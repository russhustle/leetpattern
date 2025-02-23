---
comments: True
---

# Two Pointers

## 125. Valid Palindrome

-   [LeetCode](https://leetcode.com/problems/valid-palindrome/) | [LeetCode CH](https://leetcode.cn/problems/valid-palindrome/) (Easy)

```python
--8<-- "0125_valid_palindrome.py"
```

## 167. Two Sum II -   Input Array Is Sorted

- [LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [LeetCode CH](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/) (Medium)

```python
--8<-- "0167_two_sum_ii_input_array_is_sorted.py"
```

## 15. 3Sum

-   [LeetCode](https://leetcode.com/problems/3sum/) | [LeetCode CH](https://leetcode.cn/problems/3sum/) (Medium)

```python
--8<-- "0015_3sum.py"
```

## 11. Container With Most Water

-   [LeetCode](https://leetcode.com/problems/container-with-most-water/) | [LeetCode CH](https://leetcode.cn/problems/container-with-most-water/) (Medium)
-   Return the maximum area of water that can be trapped between the vertical lines.

![11](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg){width=300px}

```python
--8<-- "0011_container_with_most_water.py"
```

## 42. Trapping Rain Water

-   [LeetCode](https://leetcode.com/problems/trapping-rain-water/) | [LeetCode CH](https://leetcode.cn/problems/trapping-rain-water/) (Hard)
-   ![42](../assets/0042.png)
-   Method 1: Dynamic Programing

| index                           | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  |
| :------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| value                           | 0   | 1   | 0   | 2   | 1   | 0   | 1   | 3   | 2   | 1   | 2   | 1   |
| `maxLeft`                       | 0   | 0   | 1   | 1   | 2   | 2   | 2   | 2   | 3   | 3   | 3   | 3   |
| `maxRight`                      | 3   | 3   | 3   | 3   | 3   | 3   | 3   | 2   | 2   | 2   | 1   | 0   |
| `hold = min(maxLeft, maxRight)` | 0   | 0   | 1   | 1   | 2   | 2   | 2   | 2   | 2   | 2   | 1   | 0   |
| `trap = max(0, hold - value)`   | 0   | 0   | 1   | 0   | 1   | 2   | 1   | 0   | 0   | 1   | 0   | 0   |

So, In total we have trap `1 + 1 + 2 + 1 + 1 = 6` water.

-   Method 2: Left Right Pointers, because we always need to care about the minimum of left right maximum numbers. So, we can use two pointers to keep track of the left and right maximum numbers.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZI2z5pq0TqA?si=OEYg01dbmzvmtIwZ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

```python
--8<-- "0042_trapping_rain_water.py"
```
