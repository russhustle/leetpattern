---
comments: True
---

# Intervals

- [x] [55. Jump Game](https://leetcode.cn/problems/jump-game/) (Medium)
- [x] [45. Jump Game II](https://leetcode.cn/problems/jump-game-ii/) (Medium)
- [x] [452. Minimum Number of Arrows to Burst Balloons](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/) (Medium)
- [x] [435. Non-overlapping Intervals](https://leetcode.cn/problems/non-overlapping-intervals/) (Medium)
- [x] [763. Partition Labels](https://leetcode.cn/problems/partition-labels/) (Medium)
- [x] [56. Merge Intervals](https://leetcode.cn/problems/merge-intervals/) (Medium)

## 55. Jump Game

-   [LeetCode](https://leetcode.com/problems/jump-game/) | [LeetCode CH](https://leetcode.cn/problems/jump-game/) (Medium)

-   Tags: array, dynamic programming, greedy
-   Return `True` if you can reach the last index, otherwise `False`.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Yan0cv2cLy8?si=musT5NViPicljg7x" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

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

```python title="55. Jump Game - Python Solution"
--8<-- "0055_jump_game.py"
```

```cpp title="55. Jump Game - C++ Solution"
--8<-- "cpp/0055_jump_game.cc"
```

## 45. Jump Game II

-   [LeetCode](https://leetcode.com/problems/jump-game-ii/) | [LeetCode CH](https://leetcode.cn/problems/jump-game-ii/) (Medium)

-   Tags: array, dynamic programming, greedy
-   Return the minimum number of jumps to reach the last index.

<iframe width="560" height="315" src="https://www.youtube.com/embed/dJ7sWiOoK7g?si=3kc-pp4rs3Dk7Jqk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

```python title="45. Jump Game II - Python Solution"
--8<-- "0045_jump_game_ii.py"
```

## 452. Minimum Number of Arrows to Burst Balloons

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/) (Medium)

-   Tags: array, greedy, sorting
-   Return the minimum number of arrows.

<iframe width="560" height="315" src="https://www.youtube.com/embed/lPmkKnvNPrw?si=P0rkcvTOxRGoFpkG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

-   Differece between two versions
    1. Start from 1: if there is no overlap, we add one more arrow.
    2. Start from the number of balloons: if there is overlap, we need to reduce one arrow.

```python title="452. Minimum Number of Arrows to Burst Balloons - Python Solution"
--8<-- "0452_minimum_number_of_arrows_to_burst_balloons.py"
```

## 435. Non-overlapping Intervals

-   [LeetCode](https://leetcode.com/problems/non-overlapping-intervals/) | [LeetCode CH](https://leetcode.cn/problems/non-overlapping-intervals/) (Medium)

-   Tags: array, dynamic programming, greedy, sorting

```python title="435. Non-overlapping Intervals - Python Solution"
--8<-- "0435_non_overlapping_intervals.py"
```

## 763. Partition Labels

-   [LeetCode](https://leetcode.com/problems/partition-labels/) | [LeetCode CH](https://leetcode.cn/problems/partition-labels/) (Medium)

-   Tags: hash table, two pointers, string, greedy

```python title="763. Partition Labels - Python Solution"
--8<-- "0763_partition_labels.py"
```

## 56. Merge Intervals

-   [LeetCode](https://leetcode.com/problems/merge-intervals/) | [LeetCode CH](https://leetcode.cn/problems/merge-intervals/) (Medium)

-   Tags: array, sorting
-   Merge all overlapping intervals.

<iframe width="560" height="315" src="https://www.youtube.com/embed/44H3cEC2fFM?si=J-Jr_Fg2eDse3-de" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

```python title="56. Merge Intervals - Python Solution"
--8<-- "0056_merge_intervals.py"
```
