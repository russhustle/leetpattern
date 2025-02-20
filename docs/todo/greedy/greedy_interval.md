---
comments: true
---

# Greedy Algorithm - Interval Problems

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRcWpkNKTljkt5q5wZLRdeHwdpFNUJKNyOFbEGT3uoM6FO1b6_-N8pqaosF-jLOiJioOu7zbtJehCM0/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## LeetCode Problems

1. 0055 - [Jump Game](https://leetcode.com/problems/jump-game/) | [跳跃游戏](https://leetcode.cn/problems/jump-game/) (Medium)
2. 0045 - [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | [跳跃游戏 II](https://leetcode.cn/problems/jump-game-ii/) (Hard)
3. 0452 - [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | [用最少数量的箭引爆气球](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/) (Medium)
4. 0435 - [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | [无重叠区间](https://leetcode.cn/problems/non-overlapping-intervals/) (Medium)
5. 0763 - [Partition Labels](https://leetcode.com/problems/partition-labels/) | [划分字母区间](https://leetcode.cn/problems/partition-labels/) (Medium)
6. 0056 - [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | [合并区间](https://leetcode.cn/problems/merge-intervals/) (Medium)

## 55. Jump Game

-   Return `True` if you can reach the last index, otherwise `False`.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Yan0cv2cLy8?si=musT5NViPicljg7x" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

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

<iframe width="560" height="315" src="https://www.youtube.com/embed/dJ7sWiOoK7g?si=3kc-pp4rs3Dk7Jqk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

```python
--8<-- "0045_jump_game_ii.py"
```

## 452. Minimum Number of Arrows to Burst Balloons

-   Return the minimum number of arrows.

<iframe width="560" height="315" src="https://www.youtube.com/embed/lPmkKnvNPrw?si=P0rkcvTOxRGoFpkG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

-   Differece between two versions
    1. Start from 1: if there is no overlap, we add one more arrow.
    2. Start from the number of balloons: if there is overlap, we need to reduce one arrow.

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
