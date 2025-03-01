---
comments: True
---

# Monotonic Stack

- [x] [739. Daily Temperatures](https://leetcode.cn/problems/daily-temperatures/) (Medium)
- [ ] [1475. Final Prices With a Special Discount in a Shop](https://leetcode.cn/problems/final-prices-with-a-special-discount-in-a-shop/) (Easy)
- [x] [496. Next Greater Element I](https://leetcode.cn/problems/next-greater-element-i/) (Easy)
- [x] [503. Next Greater Element II](https://leetcode.cn/problems/next-greater-element-ii/) (Medium)
- [ ] [1019. Next Greater Node In Linked List](https://leetcode.cn/problems/next-greater-node-in-linked-list/) (Medium)
- [ ] [962. Maximum Width Ramp](https://leetcode.cn/problems/maximum-width-ramp/) (Medium)
- [x] [853. Car Fleet](https://leetcode.cn/problems/car-fleet/) (Medium)
- [x] [901. Online Stock Span](https://leetcode.cn/problems/online-stock-span/) (Medium)
- [ ] [1124. Longest Well-Performing Interval](https://leetcode.cn/problems/longest-well-performing-interval/) (Medium)
- [ ] [1793. Maximum Score of a Good Subarray](https://leetcode.cn/problems/maximum-score-of-a-good-subarray/) (Hard)
- [x] [456. 132 Pattern](https://leetcode.cn/problems/132-pattern/) (Medium)
- [ ] [3113. Find the Number of Subarrays Where Boundary Elements Are Maximum](https://leetcode.cn/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/) (Hard)
- [ ] [2866. Beautiful Towers II](https://leetcode.cn/problems/beautiful-towers-ii/) (Medium)
- [ ] [1944. Number of Visible People in a Queue](https://leetcode.cn/problems/number-of-visible-people-in-a-queue/) (Hard)
- [ ] [2454. Next Greater Element IV](https://leetcode.cn/problems/next-greater-element-iv/) (Hard)
- [ ] [1130. Minimum Cost Tree From Leaf Values](https://leetcode.cn/problems/minimum-cost-tree-from-leaf-values/) (Medium)
- [ ] [2289. Steps to Make Array Non-decreasing](https://leetcode.cn/problems/steps-to-make-array-non-decreasing/) (Medium)
- [ ] [1776. Car Fleet II](https://leetcode.cn/problems/car-fleet-ii/) (Hard)
- [ ] [3221. Maximum Array Hopping Score II](https://leetcode.cn/problems/maximum-array-hopping-score-ii/) (Medium)
- [ ] [1966. Binary Searchable Numbers in an Unsorted Array](https://leetcode.cn/problems/binary-searchable-numbers-in-an-unsorted-array/) (Medium)
- [ ] [2832. Maximal Range That Each Element Is Maximum in It](https://leetcode.cn/problems/maximal-range-that-each-element-is-maximum-in-it/) (Medium)
- [ ] [2282. Number of People That Can Be Seen in a Grid](https://leetcode.cn/problems/number-of-people-that-can-be-seen-in-a-grid/) (Medium)

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

## 1475. Final Prices With a Special Discount in a Shop

-   [LeetCode](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/) | [LeetCode CH](https://leetcode.cn/problems/final-prices-with-a-special-discount-in-a-shop/) (Easy)
-   Tags: array, stack, monotonic stack

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

## 1019. Next Greater Node In Linked List

-   [LeetCode](https://leetcode.com/problems/next-greater-node-in-linked-list/) | [LeetCode CH](https://leetcode.cn/problems/next-greater-node-in-linked-list/) (Medium)
-   Tags: array, linked list, stack, monotonic stack

## 962. Maximum Width Ramp

-   [LeetCode](https://leetcode.com/problems/maximum-width-ramp/) | [LeetCode CH](https://leetcode.cn/problems/maximum-width-ramp/) (Medium)
-   Tags: array, two pointers, stack, monotonic stack

## 853. Car Fleet

-   [LeetCode](https://leetcode.com/problems/car-fleet/) | [LeetCode CH](https://leetcode.cn/problems/car-fleet/) (Medium)
-   Tags: array, stack, sorting, monotonic stack

```python title="853. Car Fleet - Python Solution"
--8<-- "0853_car_fleet.py"
```

## 901. Online Stock Span

-   [LeetCode](https://leetcode.com/problems/online-stock-span/) | [LeetCode CH](https://leetcode.cn/problems/online-stock-span/) (Medium)
-   Tags: stack, design, monotonic stack, data stream
-   Design a class `StockSpanner` to return the number of consecutive days (including the current day) the price of the stock has been less than or equal to the current price.

```python title="901. Online Stock Span - Python Solution"
--8<-- "0901_online_stock_span.py"
```

## 1124. Longest Well-Performing Interval

-   [LeetCode](https://leetcode.com/problems/longest-well-performing-interval/) | [LeetCode CH](https://leetcode.cn/problems/longest-well-performing-interval/) (Medium)
-   Tags: array, hash table, stack, monotonic stack, prefix sum

## 1793. Maximum Score of a Good Subarray

-   [LeetCode](https://leetcode.com/problems/maximum-score-of-a-good-subarray/) | [LeetCode CH](https://leetcode.cn/problems/maximum-score-of-a-good-subarray/) (Hard)
-   Tags: array, two pointers, binary search, stack, monotonic stack

## 456. 132 Pattern

-   [LeetCode](https://leetcode.com/problems/132-pattern/) | [LeetCode CH](https://leetcode.cn/problems/132-pattern/) (Medium)
-   Tags: array, binary search, stack, monotonic stack, ordered set

```python title="456. 132 Pattern - Python Solution"
--8<-- "0456_132_pattern.py"
```

## 3113. Find the Number of Subarrays Where Boundary Elements Are Maximum

-   [LeetCode](https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/) | [LeetCode CH](https://leetcode.cn/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/) (Hard)
-   Tags: array, binary search, stack, monotonic stack

## 2866. Beautiful Towers II

-   [LeetCode](https://leetcode.com/problems/beautiful-towers-ii/) | [LeetCode CH](https://leetcode.cn/problems/beautiful-towers-ii/) (Medium)
-   Tags: array, stack, monotonic stack

## 1944. Number of Visible People in a Queue

-   [LeetCode](https://leetcode.com/problems/number-of-visible-people-in-a-queue/) | [LeetCode CH](https://leetcode.cn/problems/number-of-visible-people-in-a-queue/) (Hard)
-   Tags: array, stack, monotonic stack

## 2454. Next Greater Element IV

-   [LeetCode](https://leetcode.com/problems/next-greater-element-iv/) | [LeetCode CH](https://leetcode.cn/problems/next-greater-element-iv/) (Hard)
-   Tags: array, binary search, stack, sorting, heap priority queue, monotonic stack

## 1130. Minimum Cost Tree From Leaf Values

-   [LeetCode](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/) | [LeetCode CH](https://leetcode.cn/problems/minimum-cost-tree-from-leaf-values/) (Medium)
-   Tags: array, dynamic programming, stack, greedy, monotonic stack

## 2289. Steps to Make Array Non-decreasing

-   [LeetCode](https://leetcode.com/problems/steps-to-make-array-non-decreasing/) | [LeetCode CH](https://leetcode.cn/problems/steps-to-make-array-non-decreasing/) (Medium)
-   Tags: array, linked list, stack, monotonic stack

## 1776. Car Fleet II

-   [LeetCode](https://leetcode.com/problems/car-fleet-ii/) | [LeetCode CH](https://leetcode.cn/problems/car-fleet-ii/) (Hard)
-   Tags: array, math, stack, heap priority queue, monotonic stack

## 3221. Maximum Array Hopping Score II

-   [LeetCode](https://leetcode.com/problems/maximum-array-hopping-score-ii/) | [LeetCode CH](https://leetcode.cn/problems/maximum-array-hopping-score-ii/) (Medium)
-   Tags: array, stack, greedy, monotonic stack

## 1966. Binary Searchable Numbers in an Unsorted Array

-   [LeetCode](https://leetcode.com/problems/binary-searchable-numbers-in-an-unsorted-array/) | [LeetCode CH](https://leetcode.cn/problems/binary-searchable-numbers-in-an-unsorted-array/) (Medium)
-   Tags: array, binary search

## 2832. Maximal Range That Each Element Is Maximum in It

-   [LeetCode](https://leetcode.com/problems/maximal-range-that-each-element-is-maximum-in-it/) | [LeetCode CH](https://leetcode.cn/problems/maximal-range-that-each-element-is-maximum-in-it/) (Medium)
-   Tags: array, stack, monotonic stack

## 2282. Number of People That Can Be Seen in a Grid

-   [LeetCode](https://leetcode.com/problems/number-of-people-that-can-be-seen-in-a-grid/) | [LeetCode CH](https://leetcode.cn/problems/number-of-people-that-can-be-seen-in-a-grid/) (Medium)
-   Tags: array, stack, matrix, monotonic stack
