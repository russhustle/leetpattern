---
comments: True
---

# Backtracking Permutation

## Table of Contents

- [x] [46. Permutations](https://leetcode.cn/problems/permutations/) (Medium)
- [ ] [3376. Minimum Time to Break Locks I](https://leetcode.cn/problems/minimum-time-to-break-locks-i/) (Medium)
- [x] [51. N-Queens](https://leetcode.cn/problems/n-queens/) (Hard)
- [ ] [52. N-Queens II](https://leetcode.cn/problems/n-queens-ii/) (Hard)
- [ ] [2850. Minimum Moves to Spread Stones Over Grid](https://leetcode.cn/problems/minimum-moves-to-spread-stones-over-grid/) (Medium)
- [ ] [1718. Construct the Lexicographically Largest Valid Sequence](https://leetcode.cn/problems/construct-the-lexicographically-largest-valid-sequence/) (Medium)
- [ ] [1307. Verbal Arithmetic Puzzle](https://leetcode.cn/problems/verbal-arithmetic-puzzle/) (Hard)
- [ ] [2014. Longest Subsequence Repeated k Times](https://leetcode.cn/problems/longest-subsequence-repeated-k-times/) (Hard)
- [ ] [267. Palindrome Permutation II](https://leetcode.cn/problems/palindrome-permutation-ii/) (Medium) 👑

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

## 3376. Minimum Time to Break Locks I

-   [LeetCode](https://leetcode.com/problems/minimum-time-to-break-locks-i/) | [LeetCode CH](https://leetcode.cn/problems/minimum-time-to-break-locks-i/) (Medium)

-   Tags: array, dynamic programming, backtracking, bit manipulation, depth first search, bitmask
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

## 52. N-Queens II

-   [LeetCode](https://leetcode.com/problems/n-queens-ii/) | [LeetCode CH](https://leetcode.cn/problems/n-queens-ii/) (Hard)

-   Tags: backtracking
## 2850. Minimum Moves to Spread Stones Over Grid

-   [LeetCode](https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/) | [LeetCode CH](https://leetcode.cn/problems/minimum-moves-to-spread-stones-over-grid/) (Medium)

-   Tags: array, dynamic programming, breadth first search, matrix
## 1718. Construct the Lexicographically Largest Valid Sequence

-   [LeetCode](https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/) | [LeetCode CH](https://leetcode.cn/problems/construct-the-lexicographically-largest-valid-sequence/) (Medium)

-   Tags: array, backtracking
## 1307. Verbal Arithmetic Puzzle

-   [LeetCode](https://leetcode.com/problems/verbal-arithmetic-puzzle/) | [LeetCode CH](https://leetcode.cn/problems/verbal-arithmetic-puzzle/) (Hard)

-   Tags: array, math, string, backtracking
## 2014. Longest Subsequence Repeated k Times

-   [LeetCode](https://leetcode.com/problems/longest-subsequence-repeated-k-times/) | [LeetCode CH](https://leetcode.cn/problems/longest-subsequence-repeated-k-times/) (Hard)

-   Tags: string, backtracking, greedy, counting, enumeration
## 267. Palindrome Permutation II

-   [LeetCode](https://leetcode.com/problems/palindrome-permutation-ii/) | [LeetCode CH](https://leetcode.cn/problems/palindrome-permutation-ii/) (Medium)

-   Tags: hash table, string, backtracking
