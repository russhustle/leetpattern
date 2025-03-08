---
comments: True
---

# Merge Intervals

- [x] [56. Merge Intervals](https://leetcode.cn/problems/merge-intervals/) (Medium)
- [x] [57. Insert Interval](https://leetcode.cn/problems/insert-interval/) (Medium)
- [x] [55. Jump Game](https://leetcode.cn/problems/jump-game/) (Medium)
- [x] [763. Partition Labels](https://leetcode.cn/problems/partition-labels/) (Medium)
- [ ] [3169. Count Days Without Meetings](https://leetcode.cn/problems/count-days-without-meetings/) (Medium)
- [ ] [2580. Count Ways to Group Overlapping Ranges](https://leetcode.cn/problems/count-ways-to-group-overlapping-ranges/) (Medium)
- [ ] [3394. Check if Grid can be Cut into Sections](https://leetcode.cn/problems/check-if-grid-can-be-cut-into-sections/) (Medium)
- [ ] [2963. Count the Number of Good Partitions](https://leetcode.cn/problems/count-the-number-of-good-partitions/) (Hard)
- [ ] [2584. Split the Array to Make Coprime Products](https://leetcode.cn/problems/split-the-array-to-make-coprime-products/) (Hard)
- [ ] [616. Add Bold Tag in String](https://leetcode.cn/problems/add-bold-tag-in-string/) (Medium) 👑
- [ ] [758. Bold Words in String](https://leetcode.cn/problems/bold-words-in-string/) (Medium) 👑
- [ ] [3323. Minimize Connected Groups by Inserting Interval](https://leetcode.cn/problems/minimize-connected-groups-by-inserting-interval/) (Medium) 👑
- [ ] [759. Employee Free Time](https://leetcode.cn/problems/employee-free-time/) (Hard) 👑
- [ ] [2655. Find Maximal Uncovered Ranges](https://leetcode.cn/problems/find-maximal-uncovered-ranges/) (Medium) 👑

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

## 57. Insert Interval

-   [LeetCode](https://leetcode.com/problems/insert-interval/) | [LeetCode CH](https://leetcode.cn/problems/insert-interval/) (Medium)

-   Tags: array

```python title="57. Insert Interval - Python Solution"
--8<-- "0057_insert_interval.py"
```

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

## 763. Partition Labels

-   [LeetCode](https://leetcode.com/problems/partition-labels/) | [LeetCode CH](https://leetcode.cn/problems/partition-labels/) (Medium)

-   Tags: hash table, two pointers, string, greedy

```python title="763. Partition Labels - Python Solution"
--8<-- "0763_partition_labels.py"
```

## 3169. Count Days Without Meetings

-   [LeetCode](https://leetcode.com/problems/count-days-without-meetings/) | [LeetCode CH](https://leetcode.cn/problems/count-days-without-meetings/) (Medium)

-   Tags: array, sorting

## 2580. Count Ways to Group Overlapping Ranges

-   [LeetCode](https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/) | [LeetCode CH](https://leetcode.cn/problems/count-ways-to-group-overlapping-ranges/) (Medium)

-   Tags: array, sorting

## 3394. Check if Grid can be Cut into Sections

-   [LeetCode](https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/) | [LeetCode CH](https://leetcode.cn/problems/check-if-grid-can-be-cut-into-sections/) (Medium)

-   Tags: array, sorting

## 2963. Count the Number of Good Partitions

-   [LeetCode](https://leetcode.com/problems/count-the-number-of-good-partitions/) | [LeetCode CH](https://leetcode.cn/problems/count-the-number-of-good-partitions/) (Hard)

-   Tags: array, hash table, math, combinatorics

## 2584. Split the Array to Make Coprime Products

-   [LeetCode](https://leetcode.com/problems/split-the-array-to-make-coprime-products/) | [LeetCode CH](https://leetcode.cn/problems/split-the-array-to-make-coprime-products/) (Hard)

-   Tags: array, hash table, math, number theory

## 616. Add Bold Tag in String

-   [LeetCode](https://leetcode.com/problems/add-bold-tag-in-string/) | [LeetCode CH](https://leetcode.cn/problems/add-bold-tag-in-string/) (Medium)

-   Tags: array, hash table, string, trie, string matching

## 758. Bold Words in String

-   [LeetCode](https://leetcode.com/problems/bold-words-in-string/) | [LeetCode CH](https://leetcode.cn/problems/bold-words-in-string/) (Medium)

-   Tags: array, hash table, string, trie, string matching

## 3323. Minimize Connected Groups by Inserting Interval

-   [LeetCode](https://leetcode.com/problems/minimize-connected-groups-by-inserting-interval/) | [LeetCode CH](https://leetcode.cn/problems/minimize-connected-groups-by-inserting-interval/) (Medium)

-   Tags: array, binary search, sliding window, sorting

## 759. Employee Free Time

-   [LeetCode](https://leetcode.com/problems/employee-free-time/) | [LeetCode CH](https://leetcode.cn/problems/employee-free-time/) (Hard)

-   Tags: array, sorting, heap priority queue

## 2655. Find Maximal Uncovered Ranges

-   [LeetCode](https://leetcode.com/problems/find-maximal-uncovered-ranges/) | [LeetCode CH](https://leetcode.cn/problems/find-maximal-uncovered-ranges/) (Medium)

-   Tags: array, sorting
