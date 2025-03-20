---
comments: True
---

# Backtracking

## Table of Contents

- [x] [46. Permutations](https://leetcode.cn/problems/permutations/) (Medium)
- [x] [78. Subsets](https://leetcode.cn/problems/subsets/) (Medium)
- [x] [17. Letter Combinations of a Phone Number](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/) (Medium)
- [x] [39. Combination Sum](https://leetcode.cn/problems/combination-sum/) (Medium)
- [x] [22. Generate Parentheses](https://leetcode.cn/problems/generate-parentheses/) (Medium)
- [x] [79. Word Search](https://leetcode.cn/problems/word-search/) (Medium)
- [x] [131. Palindrome Partitioning](https://leetcode.cn/problems/palindrome-partitioning/) (Medium)
- [x] [51. N-Queens](https://leetcode.cn/problems/n-queens/) (Hard)

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

## 17. Letter Combinations of a Phone Number

-   [LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | [LeetCode CH](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/) (Medium)

-   Tags: hash table, string, backtracking
-   Return all possible letter combinations that the number could represent.

![17](https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png)

```python title="17. Letter Combinations of a Phone Number - Python Solution"
from typing import List


# Backtracking
def letterCombinations(digits: str) -> List[str]:
    """Return all possible letter combinations that the number could represent.

    Args:
        digits (str): A string containing digits from 2-9 inclusive.

    Returns:
        List[str]: All possible letter combinations.

    Complexity:
        Time: O(4^n), where n is the number of digits in the input string.
        Space: O(4^n), where n is the number of digits in the input string.

    Example:
        >>> letterCombinations("23")
        ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
        >>> letterCombinations("")
        []
    """

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
    import doctest

    doctest.testmod()

```

## 39. Combination Sum

-   [LeetCode](https://leetcode.com/problems/combination-sum/) | [LeetCode CH](https://leetcode.cn/problems/combination-sum/) (Medium)

-   Tags: array, backtracking

```python title="39. Combination Sum - Python Solution"
from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []
    path = []

    def backtracking(total, start):
        if total > target:
            return None
        if total == target:
            result.append(path[:])
            return None

        for i in range(start, len(candidates)):
            total += candidates[i]
            path.append(candidates[i])

            backtracking(total, i)

            total -= candidates[i]
            path.pop()

    backtracking(0, 0)
    return result


print(combinationSum([2, 3, 6, 7], 7))  # [[2, 2, 3], [7]]

```

## 22. Generate Parentheses

-   [LeetCode](https://leetcode.com/problems/generate-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/generate-parentheses/) (Medium)

-   Tags: string, dynamic programming, backtracking

```python title="22. Generate Parentheses - Python Solution"
from typing import List


# Stack
def generateParenthesis(n: int) -> List[str]:
    stack = []
    result = []

    def backtrack(openN, closeN):
        if openN == closeN == n:
            result.append("".join(stack))
            return None

        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closeN)
            stack.pop()

        if closeN < openN:
            stack.append(")")
            backtrack(openN, closeN + 1)
            stack.pop()

    backtrack(0, 0)

    return result


print(generateParenthesis(3))
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

## 131. Palindrome Partitioning

-   [LeetCode](https://leetcode.com/problems/palindrome-partitioning/) | [LeetCode CH](https://leetcode.cn/problems/palindrome-partitioning/) (Medium)

-   Tags: string, dynamic programming, backtracking

```python title="131. Palindrome Partitioning - Python Solution"
from typing import List


# Backtracking
def partition(s: str) -> List[List[str]]:
    res = []
    n = len(s)

    def backtrack(idx, path):
        if idx == n:
            res.append(path[:])
            return None

        for j in range(idx, n):
            cur = s[idx : j + 1]
            if cur == cur[::-1]:
                path.append(cur)
                backtrack(j + 1, path)
                path.pop()

    backtrack(0, [])

    return res


print(partition("aab"))  # [['a', 'a', 'b'], ['aa', 'b']]

```

## 51. N-Queens

-   [LeetCode](https://leetcode.com/problems/n-queens/) | [LeetCode CH](https://leetcode.cn/problems/n-queens/) (Hard)

-   Tags: array, backtracking
- Hard
- [N-Queens](https://leetcode.com/problems/n-queens/)
- [N 皇后](https://leetcode.cn/problems/n-queens/)

```python title="51. N-Queens - Python Solution"
from typing import List


# Backtracking - Board
def solveNQueens(n: int) -> List[List[str]]:
    result = []
    chessboard = ["." * n for _ in range(n)]

    def backtracking(row):
        if row == n:
            result.append(chessboard[:])
            return None
        for col in range(n):
            if is_valid(row, col, chessboard):
                chessboard[row] = (
                    chessboard[row][:col] + "Q" + chessboard[row][col + 1 :]
                )
                backtracking(row + 1)
                chessboard[row] = (
                    chessboard[row][:col] + "." + chessboard[row][col + 1 :]
                )

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

    backtracking(0)

    return [["".join(row) for row in solution] for solution in result]


print(solveNQueens(4))
# [['.Q..', '...Q', 'Q...', '..Q.'],
#  ['..Q.', 'Q...', '...Q', '.Q..']]

```
