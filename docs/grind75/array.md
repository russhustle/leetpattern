---
comments: True
---

# Array

- [x] [1. Two Sum](https://leetcode.cn/problems/two-sum/) (Easy)
- [x] [121. Best Time to Buy and Sell Stock](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/) (Easy)
- [x] [169. Majority Element](https://leetcode.cn/problems/majority-element/) (Easy)
- [x] [217. Contains Duplicate](https://leetcode.cn/problems/contains-duplicate/) (Easy)
- [x] [57. Insert Interval](https://leetcode.cn/problems/insert-interval/) (Medium)
- [x] [15. 3Sum](https://leetcode.cn/problems/3sum/) (Medium)
- [x] [238. Product of Array Except Self](https://leetcode.cn/problems/product-of-array-except-self/) (Medium)
- [x] [39. Combination Sum](https://leetcode.cn/problems/combination-sum/) (Medium)
- [x] [56. Merge Intervals](https://leetcode.cn/problems/merge-intervals/) (Medium)
- [x] [75. Sort Colors](https://leetcode.cn/problems/sort-colors/) (Medium)
- [x] [11. Container With Most Water](https://leetcode.cn/problems/container-with-most-water/) (Medium)

## 1. Two Sum

-   [LeetCode](https://leetcode.com/problems/two-sum/) | [LeetCode CH](https://leetcode.cn/problems/two-sum/) (Easy)

-   Tags: array, hash table
-   Return the indices of the two numbers such that they add up to a specific target.

| Approach | Time Complexity | Space Complexity |
| :------: | :-------------: | :--------------: |
| Hashmap  |      O(n)       |       O(n)       |

```python title="1. Two Sum - Python Solution"
--8<-- "0001_two_sum.py"
```

```cpp title="1. Two Sum - C++ Solution"
--8<-- "cpp/0001_two_sum.cc"
```

## 121. Best Time to Buy and Sell Stock

-   [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | [LeetCode CH](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/) (Easy)

-   Tags: array, dynamic programming
-   Return the maximum profit that can be achieved from buying on one day and selling on another day.

```python title="121. Best Time to Buy and Sell Stock - Python Solution"
--8<-- "0121_best_time_to_buy_and_sell_stock.py"
```

```cpp title="121. Best Time to Buy and Sell Stock - C++ Solution"
--8<-- "cpp/0121_best_time_to_buy_and_sell_stock.cc"
```

## 169. Majority Element

-   [LeetCode](https://leetcode.com/problems/majority-element/) | [LeetCode CH](https://leetcode.cn/problems/majority-element/) (Easy)

-   Tags: array, hash table, divide and conquer, sorting, counting
-   Return the majority element in an array. The majority element is the element that appears more than `n // 2` times.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7pnhv842keE?si=fBYlNfKzdkiLgkF1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

| `num` | `count` | `res` |
| ----- | ------- | ----- |
| 2     | 1       | 2     |
| 2     | 2       | 2     |
| 1     | 1       | 2     |
| 1     | 0       | 2     |
| 1     | 1       | 1     |
| 2     | 0       | 1     |
| 2     | 1       | 2     |

```python title="169. Majority Element - Python Solution"
--8<-- "0169_majority_element.py"
```

## 217. Contains Duplicate

-   [LeetCode](https://leetcode.com/problems/contains-duplicate/) | [LeetCode CH](https://leetcode.cn/problems/contains-duplicate/) (Easy)

-   Tags: array, hash table, sorting
-   Return True if the array contains any duplicates, otherwise return False.

```python title="217. Contains Duplicate - Python Solution"
--8<-- "0217_contains_duplicate.py"
```

## 57. Insert Interval

-   [LeetCode](https://leetcode.com/problems/insert-interval/) | [LeetCode CH](https://leetcode.cn/problems/insert-interval/) (Medium)

-   Tags: array

```python title="57. Insert Interval - Python Solution"
--8<-- "0057_insert_interval.py"
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

## 238. Product of Array Except Self

-   [LeetCode](https://leetcode.com/problems/product-of-array-except-self/) | [LeetCode CH](https://leetcode.cn/problems/product-of-array-except-self/) (Medium)

-   Tags: array, prefix sum
-   Classic **Prefix Sum** problem
-   Return an array `output` such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

| Approach           | Time | Space |
| ------------------ | ---- | ----- |
| Prefix             | O(n) | O(n)  |
| Prefix (Optimized) | O(n) | O(1)  |

```python title="238. Product of Array Except Self - Python Solution"
--8<-- "0238_product_of_array_except_self.py"
```

```cpp title="238. Product of Array Except Self - C++ Solution"
--8<-- "cpp/0238_product_of_array_except_self.cc"
```

## 39. Combination Sum

-   [LeetCode](https://leetcode.com/problems/combination-sum/) | [LeetCode CH](https://leetcode.cn/problems/combination-sum/) (Medium)

-   Tags: array, backtracking

```python title="39. Combination Sum - Python Solution"
--8<-- "0039_combination_sum.py"
```

## 56. Merge Intervals

-   [LeetCode](https://leetcode.com/problems/merge-intervals/) | [LeetCode CH](https://leetcode.cn/problems/merge-intervals/) (Medium)

-   Tags: array, sorting
-   Merge all overlapping intervals.

<iframe width="560" height="315" src="https://www.youtube.com/embed/44H3cEC2fFM?si=J-Jr_Fg2eDse3-de" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

```python title="56. Merge Intervals - Python Solution"
--8<-- "0056_merge_intervals.py"
```

```cpp title="56. Merge Intervals - C++ Solution"
--8<-- "cpp/0056_merge_intervals.cc"
```

## 75. Sort Colors

-   [LeetCode](https://leetcode.com/problems/sort-colors/) | [LeetCode CH](https://leetcode.cn/problems/sort-colors/) (Medium)

-   Tags: array, two pointers, sorting

```python title="75. Sort Colors - Python Solution"
--8<-- "0075_sort_colors.py"
```

## 11. Container With Most Water

-   [LeetCode](https://leetcode.com/problems/container-with-most-water/) | [LeetCode CH](https://leetcode.cn/problems/container-with-most-water/) (Medium)

-   Tags: array, two pointers, greedy
-   Return the maximum area of water that can be trapped between the vertical lines.

![11](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg){width=300px}

```python title="11. Container With Most Water - Python Solution"
--8<-- "0011_container_with_most_water.py"
```

```cpp title="11. Container With Most Water - C++ Solution"
--8<-- "cpp/0011_container_with_most_water.cc"
```
