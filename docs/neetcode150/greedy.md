---
comments: True
---

# Greedy

- [x] [53. Maximum Subarray](https://leetcode.cn/problems/maximum-subarray/) (Medium)
- [x] [55. Jump Game](https://leetcode.cn/problems/jump-game/) (Medium)
- [x] [45. Jump Game II](https://leetcode.cn/problems/jump-game-ii/) (Medium)
- [x] [134. Gas Station](https://leetcode.cn/problems/gas-station/) (Medium)
- [x] [846. Hand of Straights](https://leetcode.cn/problems/hand-of-straights/) (Medium)
- [x] [1899. Merge Triplets to Form Target Triplet](https://leetcode.cn/problems/merge-triplets-to-form-target-triplet/) (Medium)
- [x] [763. Partition Labels](https://leetcode.cn/problems/partition-labels/) (Medium)
- [x] [678. Valid Parenthesis String](https://leetcode.cn/problems/valid-parenthesis-string/) (Medium)

## 53. Maximum Subarray

-   [LeetCode](https://leetcode.com/problems/maximum-subarray/) | [LeetCode CH](https://leetcode.cn/problems/maximum-subarray/) (Medium)
-   Tags: array, divide and conquer, dynamic programming

```python title="53. Maximum Subarray"
--8<-- "0053_maximum_subarray.py"
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

```python title="55. Jump Game"
--8<-- "0055_jump_game.py"
```

## 45. Jump Game II

-   [LeetCode](https://leetcode.com/problems/jump-game-ii/) | [LeetCode CH](https://leetcode.cn/problems/jump-game-ii/) (Medium)
-   Tags: array, dynamic programming, greedy
-   Return the minimum number of jumps to reach the last index.

<iframe width="560" height="315" src="https://www.youtube.com/embed/dJ7sWiOoK7g?si=3kc-pp4rs3Dk7Jqk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

```python title="45. Jump Game II"
--8<-- "0045_jump_game_ii.py"
```

## 134. Gas Station

-   [LeetCode](https://leetcode.com/problems/gas-station/) | [LeetCode CH](https://leetcode.cn/problems/gas-station/) (Medium)
-   Tags: array, greedy

```python title="134. Gas Station"
--8<-- "0134_gas_station.py"
```

## 846. Hand of Straights

-   [LeetCode](https://leetcode.com/problems/hand-of-straights/) | [LeetCode CH](https://leetcode.cn/problems/hand-of-straights/) (Medium)
-   Tags: array, hash table, greedy, sorting

```python title="846. Hand of Straights"
--8<-- "0846_hand_of_straights.py"
```

## 1899. Merge Triplets to Form Target Triplet

-   [LeetCode](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) | [LeetCode CH](https://leetcode.cn/problems/merge-triplets-to-form-target-triplet/) (Medium)
-   Tags: array, greedy

```python title="1899. Merge Triplets to Form Target Triplet"
--8<-- "1899_merge_triplets_to_form_target_triplet.py"
```

## 763. Partition Labels

-   [LeetCode](https://leetcode.com/problems/partition-labels/) | [LeetCode CH](https://leetcode.cn/problems/partition-labels/) (Medium)
-   Tags: hash table, two pointers, string, greedy

```python title="763. Partition Labels"
--8<-- "0763_partition_labels.py"
```

## 678. Valid Parenthesis String

-   [LeetCode](https://leetcode.com/problems/valid-parenthesis-string/) | [LeetCode CH](https://leetcode.cn/problems/valid-parenthesis-string/) (Medium)
-   Tags: string, dynamic programming, stack, greedy

```python title="678. Valid Parenthesis String"
--8<-- "0678_valid_parenthesis_string.py"
```
