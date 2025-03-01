---
comments: True
---

# House Robber

- [x] [198. House Robber](https://leetcode.cn/problems/house-robber/) (Medium)
- [x] [740. Delete and Earn](https://leetcode.cn/problems/delete-and-earn/) (Medium)
- [ ] [2320. Count Number of Ways to Place Houses](https://leetcode.cn/problems/count-number-of-ways-to-place-houses/) (Medium)
- [x] [213. House Robber II](https://leetcode.cn/problems/house-robber-ii/) (Medium)
- [ ] [3186. Maximum Total Damage With Spell Casting](https://leetcode.cn/problems/maximum-total-damage-with-spell-casting/) (Medium)

## 198. House Robber

-   [LeetCode](https://leetcode.com/problems/house-robber/) | [LeetCode CH](https://leetcode.cn/problems/house-robber/) (Medium)

-   Tags: array, dynamic programming
-   Return the maximum amount of money that can be robbed from the houses. No two adjacent houses can be robbed.

-   `dp[n]` stores the maximum amount of money that can be robbed from the first `n` houses.
-   Formula: `dp[n] = max(dp[n - 1], dp[n - 2] + nums[n])`.
    -   Skip: `dp[n]` → `dp[n - 1]`
    -   Rob: `dp[n]` → `dp[n - 2] + nums[n]`
-   Initialize `dp[0] = nums[0]` and `dp[1] = max(nums[0], nums[1])`.
-   Return `dp[-1]`.
-   Example: `nums = [2, 7, 9, 3, 1]`

|  n  | `nums[n]` | `dp[n-2]` | `dp[n-1]` | `dp[n-2] + nums[n]` | `dp[n]` |
| :-: | :-------: | :-------: | :-------: | :-----------------: | :-----: |
|  0  |     2     |     -     |     2     |          -          |    2    |
|  1  |     7     |     -     |     7     |          -          |    7    |
|  2  |     9     |     2     |     7     |         11          |   11    |
|  3  |     3     |     7     |    11     |         10          |   11    |
|  4  |     1     |    11     |    11     |         12          |   12    |

```python title="198. House Robber - Python Solution"
--8<-- "0198_house_robber.py"
```

```cpp title="198. House Robber - C++ Solution"
--8<-- "cpp/0198_house_robber.cc"
```

## 740. Delete and Earn

-   [LeetCode](https://leetcode.com/problems/delete-and-earn/) | [LeetCode CH](https://leetcode.cn/problems/delete-and-earn/) (Medium)

-   Tags: array, hash table, dynamic programming

```python title="740. Delete and Earn - Python Solution"
--8<-- "0740_delete_and_earn.py"
```

## 2320. Count Number of Ways to Place Houses

-   [LeetCode](https://leetcode.com/problems/count-number-of-ways-to-place-houses/) | [LeetCode CH](https://leetcode.cn/problems/count-number-of-ways-to-place-houses/) (Medium)

-   Tags: dynamic programming

## 213. House Robber II

-   [LeetCode](https://leetcode.com/problems/house-robber-ii/) | [LeetCode CH](https://leetcode.cn/problems/house-robber-ii/) (Medium)

-   Tags: array, dynamic programming
-   Return the maximum amount of money that can be robbed from the houses arranged in a circle.
-   Circular → Linear: `nums[0]` and `nums[-1]` cannot be robbed together.
-   Rob from `0` to `n - 2`

|  n  | `nums[n]` | `dp[n-2]` | `dp[n-1]` | `dp[n-2] + nums[n]` | `dp[n]` |
| :-: | :-------: | :-------: | :-------: | :-----------------: | :-----: |
|  0  |     2     |     -     |     2     |          -          |    2    |
|  1  |     7     |     -     |     7     |          -          |    7    |
|  2  |     9     |     2     |     7     |         11          |   11    |
|  3  |     3     |     7     |    11     |         10          |   11    |

-   Rob from `1` to `n - 1`

|  n  | `nums[n]` | `dp[n-2]` | `dp[n-1]` | `dp[n-2] + nums[n]` | `dp[n]` |
| :-: | :-------: | :-------: | :-------: | :-----------------: | :-----: |
|  1  |     7     |     -     |     -     |          -          |    7    |
|  2  |     9     |     -     |     7     |          -          |    9    |
|  3  |     3     |     7     |     9     |         10          |   10    |
|  4  |     1     |     9     |    10     |         10          |   10    |

```python title="213. House Robber II - Python Solution"
--8<-- "0213_house_robber_ii.py"
```

## 3186. Maximum Total Damage With Spell Casting

-   [LeetCode](https://leetcode.com/problems/maximum-total-damage-with-spell-casting/) | [LeetCode CH](https://leetcode.cn/problems/maximum-total-damage-with-spell-casting/) (Medium)

-   Tags: array, hash table, two pointers, binary search, dynamic programming, sorting, counting
