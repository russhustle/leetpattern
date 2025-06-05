---
comments: True
---

# Backtracking

## Table of Contents

- [x] [17. Letter Combinations of a Phone Number](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/) (Medium)
- [x] [77. Combinations](https://leetcode.cn/problems/combinations/) (Medium)
- [x] [46. Permutations](https://leetcode.cn/problems/permutations/) (Medium)
- [x] [39. Combination Sum](https://leetcode.cn/problems/combination-sum/) (Medium)
- [ ] [52. N-Queens II](https://leetcode.cn/problems/n-queens-ii/) (Hard)
- [x] [22. Generate Parentheses](https://leetcode.cn/problems/generate-parentheses/) (Medium)
- [x] [79. Word Search](https://leetcode.cn/problems/word-search/) (Medium)

## 17. Letter Combinations of a Phone Number

-   [LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | [LeetCode CH](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/) (Medium)

-   Tags: hash table, string, backtracking
-   Return all possible letter combinations that the number could represent.

![17](https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png)


```python title="17. Letter Combinations of a Phone Number - Python Solution"
from typing import List


# Backtracking
def letterCombinations(digits: str) -> List[str]:
    letter_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    n = len(digits)
    if n == 0:
        return []

    res = []

    def dfs(idx, path):
        if idx == n:
            res.append(path)
            return None

        letters = letter_map[digits[idx]]

        for i in range(len(letters)):
            dfs(idx + 1, path + letters[i])

    dfs(0, "")

    return res


if __name__ == "__main__":
    assert letterCombinations("23") == [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf",
    ]

```

## 77. Combinations

-   [LeetCode](https://leetcode.com/problems/combinations/) | [LeetCode CH](https://leetcode.cn/problems/combinations/) (Medium)

-   Tags: backtracking

```python title="77. Combinations - Python Solution"
import itertools
from typing import List


# Backtracking
def combine(n: int, k: int) -> List[List[int]]:
    res = []

    def backtrack(start, path):
        if len(path) == k:
            res.append(path[:])
            return None

        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(1, [])

    return res


# itertools
def combineItertools(n: int, k: int) -> List[List[int]]:
    path = itertools.combinations(range(1, n + 1), k)
    return path


print(combine(4, 2))
# [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
print(list(combineItertools(4, 2)))
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

```

## 46. Permutations

-   [LeetCode](https://leetcode.com/problems/permutations/) | [LeetCode CH](https://leetcode.cn/problems/permutations/) (Medium)

-   Tags: array, backtracking

```python title="46. Permutations - Python Solution"
from typing import List


# Backtracking
def permute(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    path, res = [], []
    used = [False for _ in range(n)]

    def dfs(x: int):
        if x == n:
            res.append(path[:])
            return

        for i in range(n):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            dfs(x + 1)
            path.pop()
            used[i] = False

    dfs(0)

    return res


print(permute([1, 2, 3]))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3],
#  [2, 3, 1], [3, 1, 2], [3, 2, 1]]

```

## 39. Combination Sum

-   [LeetCode](https://leetcode.com/problems/combination-sum/) | [LeetCode CH](https://leetcode.cn/problems/combination-sum/) (Medium)

-   Tags: array, backtracking

```python title="39. Combination Sum - Python Solution"
from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    n = len(candidates)
    res, path = [], []

    def dfs(total, start):
        if total > target:
            return
        if total == target:
            res.append(path.copy())
            return

        for i in range(start, n):
            total += candidates[i]
            path.append(candidates[i])
            dfs(total, i)
            total -= candidates[i]
            path.pop()

    dfs(0, 0)

    return res


if __name__ == "__main__":
    print(combinationSum([2, 3, 5], 8))
    # [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    print(combinationSum([2, 3, 6, 7], 7))
    # [[2, 2, 3], [7]]

```

## 52. N-Queens II

-   [LeetCode](https://leetcode.com/problems/n-queens-ii/) | [LeetCode CH](https://leetcode.cn/problems/n-queens-ii/) (Hard)

-   Tags: backtracking
## 22. Generate Parentheses

-   [LeetCode](https://leetcode.com/problems/generate-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/generate-parentheses/) (Medium)

-   Tags: string, dynamic programming, backtracking

```python title="22. Generate Parentheses - Python Solution"
from typing import List


# Backtracking
def generateParenthesis1(n: int) -> List[str]:
    path, res = [], []

    def dfs(openN, closeN):
        if openN == closeN == n:
            res.append("".join(path))
            return

        if openN < n:
            path.append("(")
            dfs(openN + 1, closeN)
            path.pop()

        if closeN < openN:
            path.append(")")
            dfs(openN, closeN + 1)
            path.pop()

    dfs(0, 0)

    return res


# Backtracking
def generateParenthesis2(n: int) -> List[str]:
    m = n * 2
    res, path = [], [""] * m

    def dfs(i, left):
        if i == m:
            res.append("".join(path))
            return

        if left < n:
            path[i] = "("
            dfs(i + 1, left + 1)
        if i - left < left:
            path[i] = ")"
            dfs(i + 1, left)

    dfs(0, 0)
    return res


if __name__ == "__main__":
    print(generateParenthesis1(3))
    # ['((()))', '(()())', '(())()', '()(())', '()()()']
    print(generateParenthesis2(3))
    # ['((()))', '(()())', '(())()', '()(())', '()()()']

```

## 79. Word Search

-   [LeetCode](https://leetcode.com/problems/word-search/) | [LeetCode CH](https://leetcode.cn/problems/word-search/) (Medium)

-   Tags: array, string, backtracking, depth first search, matrix

```python title="79. Word Search - Python Solution"
from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    m, n = len(board), len(board[0])
    path = set()
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def dfs(r, c, i):
        if i == len(word):
            return True

        if (
            r < 0
            or r >= m
            or c < 0
            or c >= n
            or board[r][c] != word[i]
            or (r, c) in path
        ):
            return False

        path.add((r, c))

        for dr, dc in dirs:
            if dfs(r + dr, c + dc, i + 1):
                return True

        path.remove((r, c))
        return False

    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return True

    return False


board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"],
]
word = "ABCCED"
print(exist(board, word))  # True

```
