---
comments: True
---

# Backtracking with Duplicates

- [x] [90. Subsets II](https://leetcode.cn/problems/subsets-ii/) (Medium)
- [x] [40. Combination Sum II](https://leetcode.cn/problems/combination-sum-ii/) (Medium)
- [x] [491. Non-decreasing Subsequences](https://leetcode.cn/problems/non-decreasing-subsequences/) (Medium)
- [x] [47. Permutations II](https://leetcode.cn/problems/permutations-ii/) (Medium)
- [ ] [1079. Letter Tile Possibilities](https://leetcode.cn/problems/letter-tile-possibilities/) (Medium)

## 90. Subsets II

-   [LeetCode](https://leetcode.com/problems/subsets-ii/) | [LeetCode CH](https://leetcode.cn/problems/subsets-ii/) (Medium)

-   Tags: array, backtracking, bit manipulation

```python title="90. Subsets II - Python Solution"
from typing import List


def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    path, result = [], []
    nums.sort()

    def backtracking(startIndex):
        if path not in result:
            result.append(path[:])

        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            backtracking(i + 1)
            path.pop()

    backtracking(startIndex=0)

    return result


print(subsetsWithDup([1, 2, 2]))
# [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

```

## 40. Combination Sum II

-   [LeetCode](https://leetcode.com/problems/combination-sum-ii/) | [LeetCode CH](https://leetcode.cn/problems/combination-sum-ii/) (Medium)

-   Tags: array, backtracking

```python title="40. Combination Sum II - Python Solution"
from typing import List


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    result, path = [], []
    candidates.sort()

    def backtracking(total, start):
        if total == target:
            result.append(path[:])
            return None

        for i in range(start, len(candidates)):

            if i > start and candidates[i] == candidates[i - 1]:
                continue

            if total + candidates[i] > target:
                break

            total += candidates[i]
            path.append(candidates[i])
            backtracking(total, i + 1)
            total -= candidates[i]
            path.pop()

    backtracking(0, 0)

    return result


print(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
# [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

```

## 491. Non-decreasing Subsequences

-   [LeetCode](https://leetcode.com/problems/non-decreasing-subsequences/) | [LeetCode CH](https://leetcode.cn/problems/non-decreasing-subsequences/) (Medium)

-   Tags: array, hash table, backtracking, bit manipulation

```python title="491. Non-decreasing Subsequences - Python Solution"
from typing import List


def findSubsequences(nums: List[int]) -> List[List[int]]:
    path, result = [], []

    def backtracking(startIndex):
        if len(path) > 1:
            result.append(path[:])

        used = set()
        for i in range(startIndex, len(nums)):

            if (path and nums[i] < path[-1]) or nums[i] in used:
                continue

            used.add(nums[i])
            path.append(nums[i])
            backtracking(i + 1)
            path.pop()

    backtracking(0)

    return result


print(findSubsequences([4, 6, 7, 7]))
# [[4, 6], [4, 6, 7], [4, 6, 7, 7], [4, 7], [4, 7, 7], [6, 7], [6, 7, 7], [7, 7]]

```

## 47. Permutations II

-   [LeetCode](https://leetcode.com/problems/permutations-ii/) | [LeetCode CH](https://leetcode.cn/problems/permutations-ii/) (Medium)

-   Tags: array, backtracking, sorting

```python title="47. Permutations II - Python Solution"
from typing import List


def permuteUnique(nums: List[int]) -> List[List[int]]:
    nums.sort()
    path, result = [], []
    used = [False for _ in range(len(nums))]

    def backtracking():
        if len(path) == len(nums):
            result.append(path[:])

        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue

            used[i] = True
            path.append(nums[i])
            backtracking()
            path.pop()
            used[i] = False

    backtracking()

    return result


print(permuteUnique([1, 1, 2]))
# [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

```

## 1079. Letter Tile Possibilities

-   [LeetCode](https://leetcode.com/problems/letter-tile-possibilities/) | [LeetCode CH](https://leetcode.cn/problems/letter-tile-possibilities/) (Medium)

-   Tags: hash table, string, backtracking, counting
