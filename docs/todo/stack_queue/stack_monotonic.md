---
comments: true
---

# Monotonic Stack

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSS-tpTUrdcW0wtv0M1cSS13EMvjXtyrIYh-__aENn5SoqIcbLXChE0ZyrzKMtr-GLh1dihhEJd4kBO/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## LeetCode Problems

1. 0739 - [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | [每日温度](https://leetcode.cn/problems/daily-temperatures/) (Medium)
2. 0496 - [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) | [下一个更大元素 I](https://leetcode.cn/problems/next-greater-element-i/) (Easy)
3. 0503 - [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) | [下一个更大元素 II](https://leetcode.cn/problems/next-greater-element-ii/) (Medium)
4. 0084 - [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | [柱状图中最大的矩形](https://leetcode.cn/problems/largest-rectangle-in-histogram/) (Hard)
5. 0085 - [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/) | [最大矩形](https://leetcode.cn/problems/maximal-rectangle/) (Hard)
6. 0042 - [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | [接雨水](https://leetcode.cn/problems/trapping-rain-water/) (Hard)
7. 0901 - [Online Stock Span](https://leetcode.com/problems/online-stock-span/) | [股票价格跨度](https://leetcode.cn/problems/online-stock-span/) (Medium)
8. 0316 - [Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/) | [去除重复字母](https://leetcode.cn/problems/remove-duplicate-letters/) (Medium)
9. 0456 - [132 Pattern](https://leetcode.com/problems/132-pattern/) | [132 模式](https://leetcode.cn/problems/132-pattern/) (Medium)
10. 2281 - [Sum of Total Strength of Wizards](https://leetcode.com/problems/sum-of-total-strength-of-wizards/) | [巫师的总力量和](https://leetcode.cn/problems/sum-of-total-strength-of-wizards/) (Hard)

## 739. Daily Temperatures

-   Return an array `res` such that `res[i]` is the number of days you have to wait after the `ith` day to get a warmer temperature.

```python
--8<-- "0739_daily_temperatures.py"
```

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

## 496. Next Greater Element I

```python
--8<-- "0496_next_greater_element_i.py"
```

## 503. Next Greater Element II

```python
--8<-- "0503_next_greater_element_ii.py"
```

## 84. Largest Rectangle in Histogram

```python
--8<-- "0084_largest_rectangle_in_histogram.py"
```

## 85. Maximal Rectangle

-   Return the area of the largest rectangle that can be formed within a rectangle of 1's.

![0085](https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg){width=300px}

```python
--8<-- "0085_maximal_rectangle.py"
```

## 42. Trapping Rain Water

```python
--8<-- "0042_trapping_rain_water.py"
```

## 901. Online Stock Span

-   Design a class `StockSpanner` to return the number of consecutive days (including the current day) the price of the stock has been less than or equal to the current price.

```python
--8<-- "0901_online_stock_span.py"
```

## 316. Remove Duplicate Letters

```python
--8<-- "0316_remove_duplicate_letters.py"
```

## 456. 132 Pattern

```python
--8<-- "0456_132_pattern.py"
```

## 2281. Sum of Total Strength of Wizards

```python
--8<-- "2281_sum_of_total_strength_of_wizards.py"
```
