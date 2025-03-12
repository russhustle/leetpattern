---
comments: True
---

# Backtracking Exhaustive Search and Pruning

- [ ] [3211. Generate Binary Strings Without Adjacent Zeros](https://leetcode.cn/problems/generate-binary-strings-without-adjacent-zeros/) (Medium)
- [ ] [967. Numbers With Same Consecutive Differences](https://leetcode.cn/problems/numbers-with-same-consecutive-differences/) (Medium)
- [ ] [1415. The k-th Lexicographical String of All Happy Strings of Length n](https://leetcode.cn/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/) (Medium)
- [ ] [1219. Path with Maximum Gold](https://leetcode.cn/problems/path-with-maximum-gold/) (Medium)
- [x] [79. Word Search](https://leetcode.cn/problems/word-search/) (Medium)
- [ ] [980. Unique Paths III](https://leetcode.cn/problems/unique-paths-iii/) (Hard)
- [ ] [1255. Maximum Score Words Formed by Letters](https://leetcode.cn/problems/maximum-score-words-formed-by-letters/) (Hard)
- [ ] [473. Matchsticks to Square](https://leetcode.cn/problems/matchsticks-to-square/) (Medium)
- [x] [212. Word Search II](https://leetcode.cn/problems/word-search-ii/) (Hard)
- [x] [37. Sudoku Solver](https://leetcode.cn/problems/sudoku-solver/) (Hard)
- [ ] [638. Shopping Offers](https://leetcode.cn/problems/shopping-offers/) (Medium)
- [ ] [1240. Tiling a Rectangle with the Fewest Squares](https://leetcode.cn/problems/tiling-a-rectangle-with-the-fewest-squares/) (Hard)
- [ ] [679. 24 Game](https://leetcode.cn/problems/24-game/) (Hard)
- [ ] [282. Expression Add Operators](https://leetcode.cn/problems/expression-add-operators/) (Hard)
- [ ] [126. Word Ladder II](https://leetcode.cn/problems/word-ladder-ii/) (Hard)
- [ ] [691. Stickers to Spell Word](https://leetcode.cn/problems/stickers-to-spell-word/) (Hard)
- [ ] [2056. Number of Valid Move Combinations On Chessboard](https://leetcode.cn/problems/number-of-valid-move-combinations-on-chessboard/) (Hard)
- [ ] [2386. Find the K-Sum of an Array](https://leetcode.cn/problems/find-the-k-sum-of-an-array/) (Hard)
- [ ] [488. Zuma Game](https://leetcode.cn/problems/zuma-game/) (Hard)
- [ ] [2664. The Knight’s Tour](https://leetcode.cn/problems/the-knights-tour/) (Medium) 👑
- [ ] [247. Strobogrammatic Number II](https://leetcode.cn/problems/strobogrammatic-number-ii/) (Medium) 👑
- [ ] [248. Strobogrammatic Number III](https://leetcode.cn/problems/strobogrammatic-number-iii/) (Hard) 👑
- [ ] [411. Minimum Unique Word Abbreviation](https://leetcode.cn/problems/minimum-unique-word-abbreviation/) (Hard) 👑
- [ ] [1088. Confusing Number II](https://leetcode.cn/problems/confusing-number-ii/) (Hard) 👑

## 3211. Generate Binary Strings Without Adjacent Zeros

-   [LeetCode](https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/) | [LeetCode CH](https://leetcode.cn/problems/generate-binary-strings-without-adjacent-zeros/) (Medium)

-   Tags: string, backtracking, bit manipulation

## 967. Numbers With Same Consecutive Differences

-   [LeetCode](https://leetcode.com/problems/numbers-with-same-consecutive-differences/) | [LeetCode CH](https://leetcode.cn/problems/numbers-with-same-consecutive-differences/) (Medium)

-   Tags: backtracking, breadth first search

## 1415. The k-th Lexicographical String of All Happy Strings of Length n

-   [LeetCode](https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/) | [LeetCode CH](https://leetcode.cn/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/) (Medium)

-   Tags: string, backtracking

## 1219. Path with Maximum Gold

-   [LeetCode](https://leetcode.com/problems/path-with-maximum-gold/) | [LeetCode CH](https://leetcode.cn/problems/path-with-maximum-gold/) (Medium)

-   Tags: array, backtracking, matrix

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

## 980. Unique Paths III

-   [LeetCode](https://leetcode.com/problems/unique-paths-iii/) | [LeetCode CH](https://leetcode.cn/problems/unique-paths-iii/) (Hard)

-   Tags: array, backtracking, bit manipulation, matrix

## 1255. Maximum Score Words Formed by Letters

-   [LeetCode](https://leetcode.com/problems/maximum-score-words-formed-by-letters/) | [LeetCode CH](https://leetcode.cn/problems/maximum-score-words-formed-by-letters/) (Hard)

-   Tags: array, string, dynamic programming, backtracking, bit manipulation, bitmask

## 473. Matchsticks to Square

-   [LeetCode](https://leetcode.com/problems/matchsticks-to-square/) | [LeetCode CH](https://leetcode.cn/problems/matchsticks-to-square/) (Medium)

-   Tags: array, dynamic programming, backtracking, bit manipulation, bitmask

## 212. Word Search II

-   [LeetCode](https://leetcode.com/problems/word-search-ii/) | [LeetCode CH](https://leetcode.cn/problems/word-search-ii/) (Hard)

-   Tags: array, string, backtracking, trie, matrix

```python title="212. Word Search II - Python Solution"
from typing import List

from template import TrieNode


# Backtracking + Trie
def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    root = TrieNode()
    for word in words:
        root.addWord(word)

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
        if node.isWord:
            result.add(word)

        dfs(r - 1, c, node, word)
        dfs(r + 1, c, node, word)
        dfs(r, c - 1, node, word)
        dfs(r, c + 1, node, word)

        visit.remove((r, c))

    for r in range(m):
        for c in range(n):
            dfs(r, c, root, "")

    return list(result)


board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"],
]
words = ["oath", "pea", "eat", "rain"]
print(findWords(board, words))
# ['eat', 'oath']

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

## 638. Shopping Offers

-   [LeetCode](https://leetcode.com/problems/shopping-offers/) | [LeetCode CH](https://leetcode.cn/problems/shopping-offers/) (Medium)

-   Tags: array, dynamic programming, backtracking, bit manipulation, memoization, bitmask

## 1240. Tiling a Rectangle with the Fewest Squares

-   [LeetCode](https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/) | [LeetCode CH](https://leetcode.cn/problems/tiling-a-rectangle-with-the-fewest-squares/) (Hard)

-   Tags: backtracking

## 679. 24 Game

-   [LeetCode](https://leetcode.com/problems/24-game/) | [LeetCode CH](https://leetcode.cn/problems/24-game/) (Hard)

-   Tags: array, math, backtracking

## 282. Expression Add Operators

-   [LeetCode](https://leetcode.com/problems/expression-add-operators/) | [LeetCode CH](https://leetcode.cn/problems/expression-add-operators/) (Hard)

-   Tags: math, string, backtracking

## 126. Word Ladder II

-   [LeetCode](https://leetcode.com/problems/word-ladder-ii/) | [LeetCode CH](https://leetcode.cn/problems/word-ladder-ii/) (Hard)

-   Tags: hash table, string, backtracking, breadth first search

## 691. Stickers to Spell Word

-   [LeetCode](https://leetcode.com/problems/stickers-to-spell-word/) | [LeetCode CH](https://leetcode.cn/problems/stickers-to-spell-word/) (Hard)

-   Tags: array, hash table, string, dynamic programming, backtracking, bit manipulation, memoization, bitmask

## 2056. Number of Valid Move Combinations On Chessboard

-   [LeetCode](https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/) | [LeetCode CH](https://leetcode.cn/problems/number-of-valid-move-combinations-on-chessboard/) (Hard)

-   Tags: array, string, backtracking, simulation

## 2386. Find the K-Sum of an Array

-   [LeetCode](https://leetcode.com/problems/find-the-k-sum-of-an-array/) | [LeetCode CH](https://leetcode.cn/problems/find-the-k-sum-of-an-array/) (Hard)

-   Tags: array, sorting, heap priority queue

## 488. Zuma Game

-   [LeetCode](https://leetcode.com/problems/zuma-game/) | [LeetCode CH](https://leetcode.cn/problems/zuma-game/) (Hard)

-   Tags: string, dynamic programming, stack, breadth first search, memoization

## 2664. The Knight’s Tour

-   [LeetCode](https://leetcode.com/problems/the-knights-tour/) | [LeetCode CH](https://leetcode.cn/problems/the-knights-tour/) (Medium)

-   Tags: array, backtracking, matrix

## 247. Strobogrammatic Number II

-   [LeetCode](https://leetcode.com/problems/strobogrammatic-number-ii/) | [LeetCode CH](https://leetcode.cn/problems/strobogrammatic-number-ii/) (Medium)

-   Tags: array, string, recursion

## 248. Strobogrammatic Number III

-   [LeetCode](https://leetcode.com/problems/strobogrammatic-number-iii/) | [LeetCode CH](https://leetcode.cn/problems/strobogrammatic-number-iii/) (Hard)

-   Tags: array, string, recursion

## 411. Minimum Unique Word Abbreviation

-   [LeetCode](https://leetcode.com/problems/minimum-unique-word-abbreviation/) | [LeetCode CH](https://leetcode.cn/problems/minimum-unique-word-abbreviation/) (Hard)

-   Tags: array, string, backtracking, bit manipulation

## 1088. Confusing Number II

-   [LeetCode](https://leetcode.com/problems/confusing-number-ii/) | [LeetCode CH](https://leetcode.cn/problems/confusing-number-ii/) (Hard)

-   Tags: math, backtracking
