---
comments: true
---

# Greedy Algorithm - Interval Problems

## LeetCode Problems

1. 0055 - [Jump Game](https://leetcode.com/problems/jump-game/) | [跳跃游戏](https://leetcode.cn/problems/jump-game/) (Medium)
2. 0045 - [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | [跳跃游戏 II](https://leetcode.cn/problems/jump-game-ii/) (Hard)
3. 0452 - [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | [用最少数量的箭引爆气球](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/) (Medium)
4. 0435 - [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | [无重叠区间](https://leetcode.cn/problems/non-overlapping-intervals/) (Medium)
5. 0763 - [Partition Labels](https://leetcode.com/problems/partition-labels/) | [划分字母区间](https://leetcode.cn/problems/partition-labels/) (Medium)
6. 0056 - [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | [合并区间](https://leetcode.cn/problems/merge-intervals/) (Medium)

## 55. Jump Game

-   Return `True` if you can reach the last index, otherwise `False`.

```python
--8<-- "0055_jump_game.py"
```

-   Example: `[2, 3, 1, 1, 4, 1, 2, 0, 0]`

| Index | Value | Index + Value | Max Reach | Max Reach >= Last Index |
| :---: | :---: | :-----------: | :-------: | :---------------------: |
|   0   |   2   |       2       |     2     |          False          |
|   1   |   3   |       4       |     4     |          False          |
|   2   |   1   |       3       |     4     |          False          |
|   3   |   1   |       4       |     4     |          False          |
|   4   |   4   |       8       |     8     |          True           |
|   5   |   1   |       6       |     8     |          True           |
|   6   |   2   |       8       |     8     |          True           |
|   7   |   0   |       7       |     8     |          True           |
|   8   |   0   |       8       |     8     |          True           |

## 45. Jump Game II

-   Return the minimum number of jumps to reach the last index.

```python
--8<-- "0045_jump_game_ii.py"
```

## 452. Minimum Number of Arrows to Burst Balloons

```python
--8<-- "0452_minimum_number_of_arrows_to_burst_balloons.py"
```

## 435. Non-overlapping Intervals

```python
--8<-- "0435_non_overlapping_intervals.py"
```

## 763. Partition Labels

```python
--8<-- "0763_partition_labels.py"
```

## 56. Merge Intervals

```python
--8<-- "0056_merge_intervals.py"
```
