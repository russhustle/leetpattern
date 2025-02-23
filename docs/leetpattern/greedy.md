---
comments: True
---

# Greedy

## 455. Assign Cookies

-   [LeetCode](https://leetcode.com/problems/assign-cookies/) | [LeetCode CH](https://leetcode.cn/problems/assign-cookies/) (Easy)
-   Tags: array, two pointers, greedy, sorting
-   Return the maximum number of your content children that can be satisfied.

```python
--8<-- "0455_assign_cookies.py"
```

## 1005. Maximize Sum Of Array After K Negations

-   [LeetCode](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/) | [LeetCode CH](https://leetcode.cn/problems/maximize-sum-of-array-after-k-negations/) (Easy)
-   Tags: array, greedy, sorting
-   Return the maximum sum of the array after changing at most `k` elements.

```python
--8<-- "1005_maximize_sum_of_array_after_k_negations.py"
```

## 860. Lemonade Change

-   [LeetCode](https://leetcode.com/problems/lemonade-change/) | [LeetCode CH](https://leetcode.cn/problems/lemonade-change/) (Easy)
-   Tags: array, greedy
-   Return `True` if and only if you can provide every customer with correct change.

```python
--8<-- "0860_lemonade_change.py"
```

## 2037. Minimum Number of Moves to Seat Everyone

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-moves-to-seat-everyone/) (Easy)
-   Tags: array, greedy, sorting, counting sort
-   Return the minimum number of moves needed to seat everyone.

```python
--8<-- "2037_minimum_number_of_moves_to_seat_everyone.py"
```

## 376. Wiggle Subsequence

-   [LeetCode](https://leetcode.com/problems/wiggle-subsequence/) | [LeetCode CH](https://leetcode.cn/problems/wiggle-subsequence/) (Medium)
-   Tags: array, dynamic programming, greedy
-   Return the length of the longest wiggle subsequence.
-   `up[n]` stores the length of the longest wiggle subsequence ending at `n` with a rising wiggle.
-   `down[n]` stores the length of the longest wiggle subsequence ending at `n` with a falling wiggle.
-   Initialize `up[0] = 1` and `down[0] = 1`.
-   Example: `nums = [1, 7, 4, 9, 2, 5]`

| `nums[n]` | `nums[n-1]` | `up[n-1]` | `down[n-1]` | `up[n]` | `down[n]` |
| :-------: | :---------: | :-------: | :---------: | :-----: | :-------: |
|     1     |      -      |     -     |      -      |    1    |     1     |
|     7     |      1      |     1     |      1      |    2    |     1     |
|     4     |      7      |     2     |      1      |    2    |     3     |
|     9     |      4      |     2     |      3      |    4    |     3     |
|     2     |      9      |     4     |      3      |    4    |     5     |
|     5     |      2      |     4     |      5      |    6    |     5     |

```python
--8<-- "0376_wiggle_subsequence.py"
```

## 738. Monotone Increasing Digits

-   [LeetCode](https://leetcode.com/problems/monotone-increasing-digits/) | [LeetCode CH](https://leetcode.cn/problems/monotone-increasing-digits/) (Medium)
-   Tags: math, greedy
-   Return the largest number that is less than or equal to `n` with monotone increasing digits.

```python
--8<-- "0738_monotone_increasing_digits.py"
```

## 122. Best Time to Buy and Sell Stock II

-   [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | [LeetCode CH](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/) (Medium)
-   Tags: array, dynamic programming, greedy
-   Return the maximum profit you can achieve.

```python
--8<-- "0122_best_time_to_buy_and_sell_stock_ii.py"
```

## 714. Best Time to Buy and Sell Stock with Transaction Fee

-   [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) | [LeetCode CH](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) (Medium)
-   Tags: array, dynamic programming, greedy
-   Return the maximum profit you can achieve with the given transaction fee.

```python
--8<-- "0714_best_time_to_buy_and_sell_stock_with_transaction_fee.py"
```

## 135. Candy

-   [LeetCode](https://leetcode.com/problems/candy/) | [LeetCode CH](https://leetcode.cn/problems/candy/) (Hard)
-   Tags: array, greedy
-   Return the minimum number of candies you must give.

```python
--8<-- "0135_candy.py"
```

## 406. Queue Reconstruction by Height

-   [LeetCode](https://leetcode.com/problems/queue-reconstruction-by-height/) | [LeetCode CH](https://leetcode.cn/problems/queue-reconstruction-by-height/) (Medium)
-   Tags: array, binary indexed tree, segment tree, sorting
-   Reconstruct the queue.

```python
--8<-- "0406_queue_reconstruction_by_height.py"
```

## 3075. Maximize Happiness of Selected Children

-   [LeetCode](https://leetcode.com/problems/maximize-happiness-of-selected-children/) | [LeetCode CH](https://leetcode.cn/problems/maximize-happiness-of-selected-children/) (Medium)
-   Tags: array, greedy, sorting

```python
--8<-- "3075_maximize_happiness_of_selected_children.py"
```

## 945. Minimum Increment to Make Array Unique

-   [LeetCode](https://leetcode.com/problems/minimum-increment-to-make-array-unique/) | [LeetCode CH](https://leetcode.cn/problems/minimum-increment-to-make-array-unique/) (Medium)
-   Tags: array, greedy, sorting, counting

```python
--8<-- "0945_minimum_increment_to_make_array_unique.py"
```

## 53. Maximum Subarray

-   [LeetCode](https://leetcode.com/problems/maximum-subarray/) | [LeetCode CH](https://leetcode.cn/problems/maximum-subarray/) (Medium)
-   Tags: array, divide and conquer, dynamic programming

```python
--8<-- "0053_maximum_subarray.py"
```

## 134. Gas Station

-   [LeetCode](https://leetcode.com/problems/gas-station/) | [LeetCode CH](https://leetcode.cn/problems/gas-station/) (Medium)
-   Tags: array, greedy

```python
--8<-- "0134_gas_station.py"
```

## 968. Binary Tree Cameras

-   [LeetCode](https://leetcode.com/problems/binary-tree-cameras/) | [LeetCode CH](https://leetcode.cn/problems/binary-tree-cameras/) (Hard)
-   Tags: dynamic programming, tree, depth first search, binary tree

```python
--8<-- "0968_binary_tree_cameras.py"
```

## 1589. Maximum Sum Obtained of Any Permutation

-   [LeetCode](https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/) | [LeetCode CH](https://leetcode.cn/problems/maximum-sum-obtained-of-any-permutation/) (Medium)
-   Tags: array, greedy, sorting, prefix sum

```python
--8<-- "1589_maximum_sum_obtained_of_any_permutation.py"
```
