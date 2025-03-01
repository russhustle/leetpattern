---
comments: True
---

# Stack Monotonic

- [x] [739. Daily Temperatures](https://leetcode.cn/problems/daily-temperatures/) (Medium)
- [x] [496. Next Greater Element I](https://leetcode.cn/problems/next-greater-element-i/) (Easy)
- [x] [503. Next Greater Element II](https://leetcode.cn/problems/next-greater-element-ii/) (Medium)
- [x] [84. Largest Rectangle in Histogram](https://leetcode.cn/problems/largest-rectangle-in-histogram/) (Hard)
- [x] [85. Maximal Rectangle](https://leetcode.cn/problems/maximal-rectangle/) (Hard)
- [x] [42. Trapping Rain Water](https://leetcode.cn/problems/trapping-rain-water/) (Hard)
- [x] [901. Online Stock Span](https://leetcode.cn/problems/online-stock-span/) (Medium)
- [x] [316. Remove Duplicate Letters](https://leetcode.cn/problems/remove-duplicate-letters/) (Medium)
- [x] [456. 132 Pattern](https://leetcode.cn/problems/132-pattern/) (Medium)
- [x] [2281. Sum of Total Strength of Wizards](https://leetcode.cn/problems/sum-of-total-strength-of-wizards/) (Hard)

## 739. Daily Temperatures

-   [LeetCode](https://leetcode.com/problems/daily-temperatures/) | [LeetCode CH](https://leetcode.cn/problems/daily-temperatures/) (Medium)

-   Tags: array, stack, monotonic stack
-   Return an array `res` such that `res[i]` is the number of days you have to wait after the `ith` day to get a warmer temperature.

| Index | Temp | > stack last | stack                           | result    |
| ----- | ---- | ------------ | ------------------------------- | --------- |
| 0     | 73   | False        | `[ [73, 0] ]`                   | 1 - 0 = 1 |
| 1     | 74   | True         | `[ [74, 1] ]`                   | 2 - 1 = 1 |
| 2     | 75   | True         | `[ [75, 2] ]`                   | 6 - 2 = 4 |
| 3     | 71   | False        | `[ [75, 2], [71, 3] ]`          | 5 - 3 = 2 |
| 4     | 69   | False        | `[ [75, 2], [71, 3], [69, 4] ]` | 5 - 4 = 1 |
| 5     | 72   | True         | `[ [75, 2], [72, 5] ]`          | 6 - 5 = 1 |
| 6     | 76   | True         | `[ [76, 6] ]`                   | 0         |
| 7     | 73   | False        | `[[76, 6], [73, 7]]`            | 0         |

```python title="739. Daily Temperatures - Python Solution"
--8<-- "0739_daily_temperatures.py"
```

## 496. Next Greater Element I

-   [LeetCode](https://leetcode.com/problems/next-greater-element-i/) | [LeetCode CH](https://leetcode.cn/problems/next-greater-element-i/) (Easy)

-   Tags: array, hash table, stack, monotonic stack

```python title="496. Next Greater Element I - Python Solution"
--8<-- "0496_next_greater_element_i.py"
```

## 503. Next Greater Element II

-   [LeetCode](https://leetcode.com/problems/next-greater-element-ii/) | [LeetCode CH](https://leetcode.cn/problems/next-greater-element-ii/) (Medium)

-   Tags: array, stack, monotonic stack

```python title="503. Next Greater Element II - Python Solution"
--8<-- "0503_next_greater_element_ii.py"
```

## 84. Largest Rectangle in Histogram

-   [LeetCode](https://leetcode.com/problems/largest-rectangle-in-histogram/) | [LeetCode CH](https://leetcode.cn/problems/largest-rectangle-in-histogram/) (Hard)

-   Tags: array, stack, monotonic stack

```python title="84. Largest Rectangle in Histogram - Python Solution"
--8<-- "0084_largest_rectangle_in_histogram.py"
```

## 85. Maximal Rectangle

-   [LeetCode](https://leetcode.com/problems/maximal-rectangle/) | [LeetCode CH](https://leetcode.cn/problems/maximal-rectangle/) (Hard)

-   Tags: array, dynamic programming, stack, matrix, monotonic stack
-   Return the area of the largest rectangle that can be formed within a rectangle of 1's.

![0085](https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg){width=300px}

```python title="85. Maximal Rectangle - Python Solution"
--8<-- "0085_maximal_rectangle.py"
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

## 901. Online Stock Span

-   [LeetCode](https://leetcode.com/problems/online-stock-span/) | [LeetCode CH](https://leetcode.cn/problems/online-stock-span/) (Medium)

-   Tags: stack, design, monotonic stack, data stream
-   Design a class `StockSpanner` to return the number of consecutive days (including the current day) the price of the stock has been less than or equal to the current price.

```python title="901. Online Stock Span - Python Solution"
--8<-- "0901_online_stock_span.py"
```

## 316. Remove Duplicate Letters

-   [LeetCode](https://leetcode.com/problems/remove-duplicate-letters/) | [LeetCode CH](https://leetcode.cn/problems/remove-duplicate-letters/) (Medium)

-   Tags: string, stack, greedy, monotonic stack

```python title="316. Remove Duplicate Letters - Python Solution"
--8<-- "0316_remove_duplicate_letters.py"
```

## 456. 132 Pattern

-   [LeetCode](https://leetcode.com/problems/132-pattern/) | [LeetCode CH](https://leetcode.cn/problems/132-pattern/) (Medium)

-   Tags: array, binary search, stack, monotonic stack, ordered set

```python title="456. 132 Pattern - Python Solution"
--8<-- "0456_132_pattern.py"
```

## 2281. Sum of Total Strength of Wizards

-   [LeetCode](https://leetcode.com/problems/sum-of-total-strength-of-wizards/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-total-strength-of-wizards/) (Hard)

-   Tags: array, stack, monotonic stack, prefix sum

```python title="2281. Sum of Total Strength of Wizards - Python Solution"
--8<-- "2281_sum_of_total_strength_of_wizards.py"
```
