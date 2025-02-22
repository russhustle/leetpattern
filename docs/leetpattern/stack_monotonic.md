---
comments: True
---

# Stack Monotonic

## 739. Daily Temperatures

-   [LeetCode](https://leetcode.com/problems/daily-temperatures/) | [LeetCode CH](https://leetcode.cn/problems/daily-temperatures/) (Medium)
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

```python
--8<-- "0739_daily_temperatures.py"
```

## 496. Next Greater Element I

-   [LeetCode](https://leetcode.com/problems/next-greater-element-i/) | [LeetCode CH](https://leetcode.cn/problems/next-greater-element-i/) (Easy)

```python
--8<-- "0496_next_greater_element_i.py"
```

## 503. Next Greater Element II

-   [LeetCode](https://leetcode.com/problems/next-greater-element-ii/) | [LeetCode CH](https://leetcode.cn/problems/next-greater-element-ii/) (Medium)

```python
--8<-- "0503_next_greater_element_ii.py"
```

## 84. Largest Rectangle in Histogram

-   [LeetCode](https://leetcode.com/problems/largest-rectangle-in-histogram/) | [LeetCode CH](https://leetcode.cn/problems/largest-rectangle-in-histogram/) (Hard)

```python
--8<-- "0084_largest_rectangle_in_histogram.py"
```

## 85. Maximal Rectangle

-   [LeetCode](https://leetcode.com/problems/maximal-rectangle/) | [LeetCode CH](https://leetcode.cn/problems/maximal-rectangle/) (Hard)
-   Return the area of the largest rectangle that can be formed within a rectangle of 1's.

![0085](https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg){width=300px}

```python
--8<-- "0085_maximal_rectangle.py"
```

## 42. Trapping Rain Water

-   [LeetCode](https://leetcode.com/problems/trapping-rain-water/) | [LeetCode CH](https://leetcode.cn/problems/trapping-rain-water/) (Hard)

```python
--8<-- "0042_trapping_rain_water.py"
```

## 901. Online Stock Span

-   [LeetCode](https://leetcode.com/problems/online-stock-span/) | [LeetCode CH](https://leetcode.cn/problems/online-stock-span/) (Medium)
-   Design a class `StockSpanner` to return the number of consecutive days (including the current day) the price of the stock has been less than or equal to the current price.

```python
--8<-- "0901_online_stock_span.py"
```

## 316. Remove Duplicate Letters

-   [LeetCode](https://leetcode.com/problems/remove-duplicate-letters/) | [LeetCode CH](https://leetcode.cn/problems/remove-duplicate-letters/) (Medium)

```python
--8<-- "0316_remove_duplicate_letters.py"
```

## 456. 132 Pattern

-   [LeetCode](https://leetcode.com/problems/132-pattern/) | [LeetCode CH](https://leetcode.cn/problems/132-pattern/) (Medium)

```python
--8<-- "0456_132_pattern.py"
```

## 2281. Sum of Total Strength of Wizards

-   [LeetCode](https://leetcode.com/problems/sum-of-total-strength-of-wizards/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-total-strength-of-wizards/) (Hard)

```python
--8<-- "2281_sum_of_total_strength_of_wizards.py"
```
