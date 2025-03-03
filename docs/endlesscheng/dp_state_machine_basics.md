---
comments: True
---

# DP State Machine Basics

- [ ] [3259. Maximum Energy Boost From Two Drinks](https://leetcode.cn/problems/maximum-energy-boost-from-two-drinks/) (Medium)
- [ ] [2222. Number of Ways to Select Buildings](https://leetcode.cn/problems/number-of-ways-to-select-buildings/) (Medium)
- [ ] [1567. Maximum Length of Subarray With Positive Product](https://leetcode.cn/problems/maximum-length-of-subarray-with-positive-product/) (Medium)
- [x] [2708. Maximum Strength of a Group](https://leetcode.cn/problems/maximum-strength-of-a-group/) (Medium)
- [ ] [2826. Sorting Three Groups](https://leetcode.cn/problems/sorting-three-groups/) (Medium)
- [ ] [2786. Visit Array Positions to Maximize Score](https://leetcode.cn/problems/visit-array-positions-to-maximize-score/) (Medium)
- [ ] [1911. Maximum Alternating Subsequence Sum](https://leetcode.cn/problems/maximum-alternating-subsequence-sum/) (Medium)
- [x] [376. Wiggle Subsequence](https://leetcode.cn/problems/wiggle-subsequence/) (Medium)
- [x] [1186. Maximum Subarray Sum with One Deletion](https://leetcode.cn/problems/maximum-subarray-sum-with-one-deletion/) (Medium)

## 3259. Maximum Energy Boost From Two Drinks

-   [LeetCode](https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/) | [LeetCode CH](https://leetcode.cn/problems/maximum-energy-boost-from-two-drinks/) (Medium)

-   Tags: array, dynamic programming

## 2222. Number of Ways to Select Buildings

-   [LeetCode](https://leetcode.com/problems/number-of-ways-to-select-buildings/) | [LeetCode CH](https://leetcode.cn/problems/number-of-ways-to-select-buildings/) (Medium)

-   Tags: string, dynamic programming, prefix sum

## 1567. Maximum Length of Subarray With Positive Product

-   [LeetCode](https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/) | [LeetCode CH](https://leetcode.cn/problems/maximum-length-of-subarray-with-positive-product/) (Medium)

-   Tags: array, dynamic programming, greedy

## 2708. Maximum Strength of a Group

-   [LeetCode](https://leetcode.com/problems/maximum-strength-of-a-group/) | [LeetCode CH](https://leetcode.cn/problems/maximum-strength-of-a-group/) (Medium)

-   Tags: array, dynamic programming, backtracking, greedy, bit manipulation, sorting, enumeration

```python title="2708. Maximum Strength of a Group - Python Solution"
--8<-- "2708_maximum_strength_of_a_group.py"
```

## 2826. Sorting Three Groups

-   [LeetCode](https://leetcode.com/problems/sorting-three-groups/) | [LeetCode CH](https://leetcode.cn/problems/sorting-three-groups/) (Medium)

-   Tags: array, binary search, dynamic programming

## 2786. Visit Array Positions to Maximize Score

-   [LeetCode](https://leetcode.com/problems/visit-array-positions-to-maximize-score/) | [LeetCode CH](https://leetcode.cn/problems/visit-array-positions-to-maximize-score/) (Medium)

-   Tags: array, dynamic programming

## 1911. Maximum Alternating Subsequence Sum

-   [LeetCode](https://leetcode.com/problems/maximum-alternating-subsequence-sum/) | [LeetCode CH](https://leetcode.cn/problems/maximum-alternating-subsequence-sum/) (Medium)

-   Tags: array, dynamic programming

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

```python title="376. Wiggle Subsequence - Python Solution"
--8<-- "0376_wiggle_subsequence.py"
```

## 1186. Maximum Subarray Sum with One Deletion

-   [LeetCode](https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/) | [LeetCode CH](https://leetcode.cn/problems/maximum-subarray-sum-with-one-deletion/) (Medium)

-   Tags: array, dynamic programming

```python title="1186. Maximum Subarray Sum with One Deletion - Python Solution"
--8<-- "1186_maximum_subarray_sum_with_one_deletion.py"
```
