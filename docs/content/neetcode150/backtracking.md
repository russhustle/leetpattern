---
comments: True
---

# Backtracking

## Table of Contents

- [x] [78. Subsets](https://leetcode.cn/problems/subsets/) (Medium)
- [x] [39. Combination Sum](https://leetcode.cn/problems/combination-sum/) (Medium)
- [x] [40. Combination Sum II](https://leetcode.cn/problems/combination-sum-ii/) (Medium)
- [x] [46. Permutations](https://leetcode.cn/problems/permutations/) (Medium)
- [x] [90. Subsets II](https://leetcode.cn/problems/subsets-ii/) (Medium)
- [x] [79. Word Search](https://leetcode.cn/problems/word-search/) (Medium)
- [x] [131. Palindrome Partitioning](https://leetcode.cn/problems/palindrome-partitioning/) (Medium)
- [x] [17. Letter Combinations of a Phone Number](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/) (Medium)
- [x] [51. N-Queens](https://leetcode.cn/problems/n-queens/) (Hard)

## 78. Subsets

-   [LeetCode](https://leetcode.com/problems/subsets/) | [LeetCode CH](https://leetcode.cn/problems/subsets/) (Medium)

-   Tags: array, backtracking, bit manipulation

```python title="78. Subsets - Python Solution"
from typing import List


# Iterative Inclusion Backtracking
def subsets_iterative_inclusion(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    res, path = [], []

    def dfs(i):
        res.append(path.copy())

        for j in range(i, n):
            path.append(nums[j])
            dfs(j + 1)
            path.pop()

    dfs(0)

    return res


# Binary Decision Backtracking
def subsets_binary_decision(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    res, path = [], []

    def dfs(i):
        if i == n:
            res.append(path.copy())
            return

        # Exclude
        dfs(i + 1)

        # Include
        path.append(nums[i])
        dfs(i + 1)
        path.pop()

    dfs(0)

    return res


print(subsets_iterative_inclusion([1, 2, 3]))
# [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
print(subsets_binary_decision([1, 2, 3]))
# [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]

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

## 131. Palindrome Partitioning

-   [LeetCode](https://leetcode.com/problems/palindrome-partitioning/) | [LeetCode CH](https://leetcode.cn/problems/palindrome-partitioning/) (Medium)

-   Tags: string, dynamic programming, backtracking

```python title="131. Palindrome Partitioning - Python Solution"
from typing import List


# Backtracking
def partition(s: str) -> List[List[str]]:
    n = len(s)
    res, path = [], []

    def dfs(start):
        if start == n:
            res.append(path.copy())
            return

        for end in range(start, n):
            cur = s[start : end + 1]
            if cur == cur[::-1]:
                path.append(cur)
                dfs(end + 1)
                path.pop()

    dfs(0)

    return res


if __name__ == "__main__":
    print(partition("aab"))
    # [['a', 'a', 'b'], ['aa', 'b']]

```

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

## 51. N-Queens

-   [LeetCode](https://leetcode.com/problems/n-queens/) | [LeetCode CH](https://leetcode.cn/problems/n-queens/) (Hard)

-   Tags: array, backtracking
- Hard
- [N-Queens](https://leetcode.com/problems/n-queens/)
- [N 皇后](https://leetcode.cn/problems/n-queens/)


```python title="51. N-Queens - Python Solution"
from typing import List


# Backtracking
def solveNQueens(n: int) -> List[List[str]]:
    res = []
    board = ["." * n for _ in range(n)]

    def dfs(row):
        if row == n:
            res.append(board[:])
            return None
        for col in range(n):
            if is_valid(row, col, board):
                board[row] = board[row][:col] + "Q" + board[row][col + 1 :]
                dfs(row + 1)
                board[row] = board[row][:col] + "." + board[row][col + 1 :]

    def is_valid(row, col, chessboard):
        for i in range(row):
            if chessboard[i][col] == "Q":
                return False

        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        i, j = row - 1, col + 1
        while i >= 0 and j < len(chessboard):
            if chessboard[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True

    dfs(0)

    return [["".join(row) for row in i] for i in res]


# Backtracking
def solveNQueens2(n: int) -> List[List[str]]:
    res = []
    queens = [0] * n
    col = [False] * n
    diag1 = [False] * (n * 2 - 1)
    diag2 = [False] * (n * 2 - 1)

    def dfs(r: int) -> None:
        if r == n:
            res.append(["." * c + "Q" + "." * (n - 1 - c) for c in queens])
            return

        for c, ok in enumerate(col):
            if not ok and not diag1[r + c] and not diag2[r - c]:
                queens[r] = c
                col[c] = diag1[r + c] = diag2[r - c] = True
                dfs(r + 1)
                col[c] = diag1[r + c] = diag2[r - c] = False

    dfs(0)

    return res


if __name__ == "__main__":
    print(solveNQueens(4))
    # [['.Q..', '...Q', 'Q...', '..Q.'],
    #  ['..Q.', 'Q...', '...Q', '.Q..']]
    print(solveNQueens(1))
    # [['Q']]
    print(solveNQueens2(4))
    # [['.Q..', '...Q', 'Q...', '..Q.'],
    #  ['..Q.', 'Q...', '...Q', '.Q..']]
    print(solveNQueens2(1))
    # [['Q']]

```
