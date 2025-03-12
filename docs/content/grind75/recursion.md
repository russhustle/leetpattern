---
comments: True
---

# Recursion

- [x] [46. Permutations](https://leetcode.cn/problems/permutations/) (Medium)
- [x] [78. Subsets](https://leetcode.cn/problems/subsets/) (Medium)
- [x] [17. Letter Combinations of a Phone Number](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/) (Medium)

## 46. Permutations

-   [LeetCode](https://leetcode.com/problems/permutations/) | [LeetCode CH](https://leetcode.cn/problems/permutations/) (Medium)

-   Tags: array, backtracking

```python title="46. Permutations - Python Solution"
from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    path, result = [], []
    used = [False for _ in range(len(nums))]

    def backtracking():
        if len(path) == len(nums):
            result.append(path[:])

        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtracking()
            path.pop()
            used[i] = False

    backtracking()

    return result


print(permute([1, 2, 3]))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

```

## 78. Subsets

-   [LeetCode](https://leetcode.com/problems/subsets/) | [LeetCode CH](https://leetcode.cn/problems/subsets/) (Medium)

-   Tags: array, backtracking, bit manipulation

```python title="78. Subsets - Python Solution"
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    path, result = [], []

    def backtracking(startIndex):
        result.append(path[:])

        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            backtracking(i + 1)
            path.pop()

    backtracking(startIndex=0)

    return result


print(subsets([1, 2, 3]))
# [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

```

## 17. Letter Combinations of a Phone Number

-   [LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | [LeetCode CH](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/) (Medium)

-   Tags: hash table, string, backtracking

```python title="17. Letter Combinations of a Phone Number - Python Solution"
from typing import List


# Backtracking
def letterCombinations(digits: str) -> List[str]:
    letterMap = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz",
    }

    res = []

    def backtrack(idx, s):
        if idx == len(digits):
            res.append(s)
            return None

        digit = int(digits[idx])
        letters = letterMap[digit]

        for i in range(len(letters)):
            backtrack(idx + 1, s + letters[i])

    if len(digits) == 0:
        return res

    backtrack(0, "")

    return res


print(letterCombinations("23"))
# ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

```
