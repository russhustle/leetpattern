---
comments: True
---

# Backtracking

## Table of Contents

- [x] [77. Combinations](https://leetcode.cn/problems/combinations/) (Medium)
- [x] [17. Letter Combinations of a Phone Number](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/) (Medium)
- [x] [39. Combination Sum](https://leetcode.cn/problems/combination-sum/) (Medium)
- [x] [40. Combination Sum II](https://leetcode.cn/problems/combination-sum-ii/) (Medium)
- [x] [216. Combination Sum III](https://leetcode.cn/problems/combination-sum-iii/) (Medium)
- [x] [131. Palindrome Partitioning](https://leetcode.cn/problems/palindrome-partitioning/) (Medium)
- [x] [93. Restore IP Addresses](https://leetcode.cn/problems/restore-ip-addresses/) (Medium)
- [x] [78. Subsets](https://leetcode.cn/problems/subsets/) (Medium)
- [x] [90. Subsets II](https://leetcode.cn/problems/subsets-ii/) (Medium)
- [x] [491. Non-decreasing Subsequences](https://leetcode.cn/problems/non-decreasing-subsequences/) (Medium)
- [x] [46. Permutations](https://leetcode.cn/problems/permutations/) (Medium)
- [x] [47. Permutations II](https://leetcode.cn/problems/permutations-ii/) (Medium)
- [x] [51. N-Queens](https://leetcode.cn/problems/n-queens/) (Hard)
- [x] [37. Sudoku Solver](https://leetcode.cn/problems/sudoku-solver/) (Hard)
- [x] [79. Word Search](https://leetcode.cn/problems/word-search/) (Medium)
- [x] [212. Word Search II](https://leetcode.cn/problems/word-search-ii/) (Hard)

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

## 216. Combination Sum III

-   [LeetCode](https://leetcode.com/problems/combination-sum-iii/) | [LeetCode CH](https://leetcode.cn/problems/combination-sum-iii/) (Medium)

-   Tags: array, backtracking
```python title="216. Combination Sum III - Python Solution"
import itertools
from typing import List


# 1. Backtracking
def combinationSum3(k: int, n: int) -> List[List[int]]:
    path, result = [], []

    def backtracking(start):
        if len(path) == k and sum(path) == n:
            result.append(path[:])
            return

        for i in range(start, 10):
            path.append(i)
            backtracking(i + 1)
            path.pop()

    backtracking(1)

    return result


# 2. Itertools
def combinationSum3Itertools(k: int, n: int) -> List[List[int]]:
    combinations = itertools.combinations(range(1, 10), k)
    result = []

    for i in combinations:
        if sum(i) == n:
            result.append(i)

    return result


print(combinationSum3(3, 7))  # [[1, 2, 4]]
print(combinationSum3Itertools(3, 7))  # [(1, 2, 4)]

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

## 93. Restore IP Addresses

-   [LeetCode](https://leetcode.com/problems/restore-ip-addresses/) | [LeetCode CH](https://leetcode.cn/problems/restore-ip-addresses/) (Medium)

-   Tags: string, backtracking
```python title="93. Restore IP Addresses - Python Solution"
from typing import List


def restoreIpAddresses(s: str) -> List[str]:
    result = []

    def backtracking(start_index, point_num, current, result):
        # stop condition
        if point_num == 3:
            if is_valid(s, start_index, len(s) - 1):
                current += s[start_index:]
                result.append(current)
            return

        for i in range(start_index, len(s)):
            if is_valid(s, start_index, i):
                sub = s[start_index : i + 1]
                backtracking(i + 1, point_num + 1, current + sub + ".", result)
            else:
                break

    def is_valid(s, start, end):
        if start > end:
            return False

        if s[start] == "0" and start != end:
            return False

        num = 0
        for i in range(start, end + 1):
            if not s[i].isdigit():
                return False
            num = num * 10 + int(s[i])
            if num > 255:
                return False
        return True

    backtracking(0, 0, "", result)

    return result


print(restoreIpAddresses("25525511135"))
# ['255.255.11.135', '255.255.111.35']

```

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

## 37. Sudoku Solver

-   [LeetCode](https://leetcode.com/problems/sudoku-solver/) | [LeetCode CH](https://leetcode.cn/problems/sudoku-solver/) (Hard)

-   Tags: array, hash table, backtracking, matrix
- [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)
- [解数独](https://leetcode.cn/problems/sudoku-solver/)
- Hard

```python title="37. Sudoku Solver - Python Solution"
from pprint import pprint
from typing import List


# Backtracking - Board
def solveSudoku(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """

    def backtracking(board: List[List[str]]) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    continue
                for k in range(1, 10):
                    if is_valid(i, j, k, board):
                        board[i][j] = str(k)
                        if backtracking(board):
                            return True
                        board[i][j] = "."
                return False
        return True

    def is_valid(row: int, col: int, val: int, board: List[List[str]]) -> bool:
        for i in range(9):
            if board[row][i] == str(val):
                return False
        for j in range(9):
            if board[j][col] == str(val):
                return False
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == str(val):
                    return False
        return True

    backtracking(board)


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

solveSudoku(board)
pprint(board)
# [['5', '3', '4', '6', '7', '8', '9', '1', '2'],
#  ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
#  ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
#  ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
#  ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
#  ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
#  ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
#  ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
#  ['3', '4', '5', '2', '8', '6', '1', '7', '9']]

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

## 212. Word Search II

-   [LeetCode](https://leetcode.com/problems/word-search-ii/) | [LeetCode CH](https://leetcode.cn/problems/word-search-ii/) (Hard)

-   Tags: array, string, backtracking, trie, matrix
```python title="212. Word Search II - Python Solution"
from typing import List

from leetpattern.utils import Trie


# Backtracking + Trie
def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    trie = Trie()
    for word in words:
        trie.add_word(word)

    m, n = len(board), len(board[0])
    result, visit = set(), set()

    def dfs(r, c, node, word):
        if (
            r < 0
            or r >= m
            or c < 0
            or c >= n
            or (r, c) in visit
            or board[r][c] not in node.children
        ):
            return None

        visit.add((r, c))

        node = node.children[board[r][c]]
        word += board[r][c]
        if node.is_word:
            result.add(word)

        dfs(r - 1, c, node, word)
        dfs(r + 1, c, node, word)
        dfs(r, c - 1, node, word)
        dfs(r, c + 1, node, word)

        visit.remove((r, c))

    for r in range(m):
        for c in range(n):
            dfs(r, c, trie.root, "")

    return list(result)


def test_find_words():
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words = ["oath", "pea", "eat", "rain"]
    result = findWords(board, words)
    assert sorted(result) == ["eat", "oath"]

```
