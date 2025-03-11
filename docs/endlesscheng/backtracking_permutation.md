---
comments: True
---

# Backtracking Permutation

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
