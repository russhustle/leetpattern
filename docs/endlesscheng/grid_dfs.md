---
comments: True
---

# Grid DFS

- [x] [200. Number of Islands](https://leetcode.cn/problems/number-of-islands/) (Medium)
- [x] [695. Max Area of Island](https://leetcode.cn/problems/max-area-of-island/) (Medium)
- [x] [463. Island Perimeter](https://leetcode.cn/problems/island-perimeter/) (Easy)
- [x] [2658. Maximum Number of Fish in a Grid](https://leetcode.cn/problems/maximum-number-of-fish-in-a-grid/) (Medium)
- [x] [1034. Coloring A Border](https://leetcode.cn/problems/coloring-a-border/) (Medium)
- [x] [1020. Number of Enclaves](https://leetcode.cn/problems/number-of-enclaves/) (Medium)
- [x] [2684. Maximum Number of Moves in a Grid](https://leetcode.cn/problems/maximum-number-of-moves-in-a-grid/) (Medium)
- [x] [1254. Number of Closed Islands](https://leetcode.cn/problems/number-of-closed-islands/) (Medium)
- [x] [130. Surrounded Regions](https://leetcode.cn/problems/surrounded-regions/) (Medium)
- [x] [1905. Count Sub Islands](https://leetcode.cn/problems/count-sub-islands/) (Medium)
- [ ] [1391. Check if There is a Valid Path in a Grid](https://leetcode.cn/problems/check-if-there-is-a-valid-path-in-a-grid/) (Medium)
- [x] [417. Pacific Atlantic Water Flow](https://leetcode.cn/problems/pacific-atlantic-water-flow/) (Medium)
- [ ] [529. Minesweeper](https://leetcode.cn/problems/minesweeper/) (Medium)
- [ ] [1559. Detect Cycles in 2D Grid](https://leetcode.cn/problems/detect-cycles-in-2d-grid/) (Medium)
- [x] [827. Making A Large Island](https://leetcode.cn/problems/making-a-large-island/) (Hard)
- [x] [305. Number of Islands II](https://leetcode.cn/problems/number-of-islands-ii/) (Hard) 👑
- [ ] [2061. Number of Spaces Cleaning Robot Cleaned](https://leetcode.cn/problems/number-of-spaces-cleaning-robot-cleaned/) (Medium) 👑
- [ ] [2852. Sum of Remoteness of All Cells](https://leetcode.cn/problems/sum-of-remoteness-of-all-cells/) (Medium) 👑
- [ ] [489. Robot Room Cleaner](https://leetcode.cn/problems/robot-room-cleaner/) (Hard) 👑

## 200. Number of Islands

-   [LeetCode](https://leetcode.com/problems/number-of-islands/) | [LeetCode CH](https://leetcode.cn/problems/number-of-islands/) (Medium)

-   Tags: array, depth first search, breadth first search, union find, matrix
-   Count the number of islands in a 2D grid.
-   Method 1: DFS
-   Method 2: BFS (use a queue to traverse the grid)

-   How to keep track of visited cells?

    1. Mark the visited cell as `0` (or any other value) to avoid revisiting it.
    2. Use a set to store the visited cells.

-   Steps:
    1. Init: variables
    2. DFS/BFS: starting from the cell with `1`, turn all the connected `1`s to `0`.
    3. Traverse the grid, and if the cell is `1`, increment the count and call DFS/BFS.

![0200](../assets/0200.jpg)

```python title="200. Number of Islands - Python Solution"
from collections import deque
from copy import deepcopy
from typing import List


# DFS
def numIslandsDFS(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    res = 0

    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != "1":
            return

        grid[r][c] = "2"

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(m):
        for c in range(n):
            if grid[r][c] == "1":
                dfs(r, c)
                res += 1

    return res


# BFS + Set
def numIslandsBFS1(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = set()
    res = 0

    def bfs(r, c):
        q = deque([(r, c)])

        while q:
            row, col = q.popleft()

            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if (
                    nr < 0
                    or nr >= m
                    or nc < 0
                    or nc >= n
                    or grid[nr][nc] == "0"
                    or (nr, nc) in visited
                ):
                    continue

                visited.add((nr, nc))
                q.append((nr, nc))

    for r in range(m):
        for c in range(n):
            if grid[r][c] == "1" and (r, c) not in visited:
                visited.add((r, c))
                bfs(r, c)
                res += 1

    return res


# BFS + Grid
def numIslandsBFS2(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    res = 0

    def bfs(r, c):
        q = deque([(r, c)])

        while q:
            row, col = q.popleft()

            for dr, dc in dirs:
                nr, nc = dr + row, dc + col
                if (
                    nr < 0
                    or nr >= m
                    or nc < 0
                    or nc >= n
                    or grid[nr][nc] != "1"
                ):
                    continue
                grid[nr][nc] = "2"
                q.append((nr, nc))

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                grid[i][j] = "2"
                bfs(i, j)
                res += 1

    return res


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

print(numIslandsDFS(deepcopy(grid)))  # 1
print(numIslandsBFS1(deepcopy(grid)))  # 1
print(numIslandsBFS2(deepcopy(grid)))  # 1

```

```cpp title="200. Number of Islands - C++ Solution"
#include <vector>
#include <iostream>
using namespace std;

class Solution
{
private:
    void dfs(vector<vector<char>> &grid, int r, int c)
    {
        int row = grid.size();
        int col = grid[0].size();

        if (r < 0 || r >= row || c < 0 || c >= col || grid[r][c] != '1')
        {
            return;
        }
        grid[r][c] = '0';

        dfs(grid, r - 1, c);
        dfs(grid, r + 1, c);
        dfs(grid, r, c - 1);
        dfs(grid, r, c + 1);
    }

public:
    int numIslands(vector<vector<char>> &grid)
    {
        int m = grid.size(), n = grid[0].size();
        int res = 0;
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j] == '1')
                {
                    res++;
                    dfs(grid, i, j);
                }
            }
        }
        return res;
    }
};

int main()
{
    Solution s;
    vector<vector<char>> grid = {
        {'1', '1', '0', '0', '0'},
        {'1', '1', '0', '0', '0'},
        {'0', '0', '1', '0', '0'},
        {'0', '0', '0', '1', '1'}};
    cout << s.numIslands(grid) << endl;
    return 0;
}

```

## 695. Max Area of Island

-   [LeetCode](https://leetcode.com/problems/max-area-of-island/) | [LeetCode CH](https://leetcode.cn/problems/max-area-of-island/) (Medium)

-   Tags: array, depth first search, breadth first search, union find, matrix

```python title="695. Max Area of Island - Python Solution"
from collections import deque
from typing import List


# DFS
def maxAreaOfIslandDFS(grid: List[List[int]]) -> int:
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])

    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != 1:
            return 0

        grid[r][c] = 2

        return (
            1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        )

    area = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                area = max(area, dfs(r, c))

    return area


# BFS
def maxAreaOfIslandBFS1(grid: List[List[int]]) -> int:
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = set()
    res = 0

    def bfs(r, c):
        q = deque([(r, c)])
        area = 0

        while q:
            row, col = q.popleft()
            area += 1

            for dr, dc in dirs:
                nr, nc = row + dr, col + dc

                if (
                    nr < 0
                    or nr >= m
                    or nc < 0
                    or nc >= n
                    or grid[nr][nc] == 0
                    or (nr, nc) in visited
                ):
                    continue

                visited.add((nr, nc))
                q.append((nr, nc))

        return area

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1 and (r, c) not in visited:
                visited.add((r, c))
                res = max(res, bfs(r, c))

    return res


# BFS + Grid
def numIslandsBFS2(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    res = 0

    def bfs(r, c):
        q = deque([(r, c)])
        area = 0

        while q:
            row, col = q.popleft()
            area += 1

            for dr, dc in dirs:
                nr, nc = row + dr, col + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] == 0:
                    continue

                q.append((nr, nc))
                grid[nr][nc] = 0

        return area

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                grid[r][c] = 0
                res = max(res, bfs(r, c))

    return res


grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]
print(maxAreaOfIslandDFS(grid))  # 6
print(maxAreaOfIslandBFS1(grid))  # 6
print(numIslandsBFS2(grid))  # 6

```

```cpp title="695. Max Area of Island - C++ Solution"
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
   public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int res = 0;

        auto dfs = [&](auto&& self, int r, int c) -> int {
            if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] != 1) {
                return 0;
            }
            grid[r][c] = 0;

            return 1 + self(self, r - 1, c) + self(self, r, c - 1) +
                   self(self, r + 1, c) + self(self, r, c + 1);
        };
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    int area = dfs(dfs, i, j);
                    res = max(res, area);
                }
            }
        }
        return res;
    }
};

int main() {
    Solution s;
    vector<vector<int>> grid = {{0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
                                {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0},
                                {0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0},
                                {0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0},
                                {0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0},
                                {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0},
                                {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0},
                                {0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0}};
    cout << s.maxAreaOfIsland(grid) << endl;
    return 0;
}

```

## 463. Island Perimeter

-   [LeetCode](https://leetcode.com/problems/island-perimeter/) | [LeetCode CH](https://leetcode.cn/problems/island-perimeter/) (Easy)

-   Tags: array, depth first search, breadth first search, matrix

```python title="463. Island Perimeter - Python Solution"
from typing import List


# DFS
def islandPerimeterDFS(grid: List[List[int]]) -> int:
    # TC: O(m * n)
    # SC: O(m * n)

    visited = set()
    m, n = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(r, c):
        if (r, c) in visited or grid[r][c] == 0:
            return 0
        visited.add((r, c))
        perimeter = 0

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr not in range(m) or nc not in range(n) or grid[nr][nc] == 0:
                perimeter += 1
            else:
                perimeter += dfs(nr, nc)

        return perimeter

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                return dfs(r, c)
    return 0


def islandPerimeter(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    perimeter = 0

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                perimeter += 4

                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2

                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(islandPerimeterDFS(grid))  # 16
print(islandPerimeter(grid))  # 16

```

## 2658. Maximum Number of Fish in a Grid

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-fish-in-a-grid/) (Medium)

-   Tags: array, depth first search, breadth first search, union find, matrix

```python title="2658. Maximum Number of Fish in a Grid - Python Solution"
from typing import List


# Grid DFS
def findMaxFish(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    res = 0

    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
            return 0
        val = grid[r][c]
        grid[r][c] = 0

        return (
            val + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
        )

    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0:
                res = max(res, dfs(i, j))

    return res


grid = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]
print(findMaxFish(grid))  # 7

```

## 1034. Coloring A Border

-   [LeetCode](https://leetcode.com/problems/coloring-a-border/) | [LeetCode CH](https://leetcode.cn/problems/coloring-a-border/) (Medium)

-   Tags: array, depth first search, breadth first search, matrix

```python title="1034. Coloring A Border - Python Solution"
from typing import List


# Grid DFS
def colorBorder(
    grid: List[List[int]], row: int, col: int, color: int
) -> List[List[int]]:

    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    m, n = len(grid), len(grid[0])
    org = grid[row][col]
    visited = set()
    borders = set()

    def dfs(r, c):
        if (r, c) in visited:
            return

        visited.add((r, c))

        is_border = False
        for dr, dc in dirs:
            nr, nc = dr + r, dc + c
            if 0 <= nr < m and 0 <= nc < n:
                if grid[nr][nc] == org:
                    dfs(nr, nc)
                elif (nr, nc) not in visited:
                    is_border = True
            else:
                is_border = True

        if is_border:
            borders.add((r, c))

    dfs(row, col)

    for r, c in borders:
        grid[r][c] = color

    return grid


grid = [[1, 2, 2], [2, 3, 2]]
row = 0
col = 1
color = 3
print(colorBorder(grid, row, col, color))  # [[1, 3, 3], [2, 3, 3]]

```

## 1020. Number of Enclaves

-   [LeetCode](https://leetcode.com/problems/number-of-enclaves/) | [LeetCode CH](https://leetcode.cn/problems/number-of-enclaves/) (Medium)

-   Tags: array, depth first search, breadth first search, union find, matrix

```python title="1020. Number of Enclaves - Python Solution"
from typing import List


# DFS
def numEnclaves(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if (
            r not in range(m)
            or c not in range(n)
            or grid[r][c] == 0
            or (r, c) in visited
        ):
            return

        grid[r][c] = 0
        visited.add((r, c))

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(m):
        for c in range(n):
            if (
                (r in [0, m - 1] or c in [0, n - 1])
                and grid[r][c] == 1
                and (r, c) not in visited
            ):
                dfs(r, c)

    count = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1 and (r, c) not in visited:
                count += 1

    return count


grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
print(numEnclaves(grid))  # 3

```

## 2684. Maximum Number of Moves in a Grid

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-moves-in-a-grid/) (Medium)

-   Tags: array, dynamic programming, matrix

```python title="2684. Maximum Number of Moves in a Grid - Python Solution"
from typing import List


# DFS
def maxMovesDFS(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    res = 0

    def dfs(r, c):
        nonlocal res
        res = max(res, c)
        if res == n - 1:
            return

        for k in r - 1, r, r + 1:
            if 0 <= k < m and grid[k][c + 1] > grid[r][c]:
                dfs(k, c + 1)
        grid[r][c] = 0

    for i in range(m):
        dfs(i, 0)

    return res


grid = [[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]
print(maxMovesDFS(grid))  # 3

```

## 1254. Number of Closed Islands

-   [LeetCode](https://leetcode.com/problems/number-of-closed-islands/) | [LeetCode CH](https://leetcode.cn/problems/number-of-closed-islands/) (Medium)

-   Tags: array, depth first search, breadth first search, union find, matrix

```python title="1254. Number of Closed Islands - Python Solution"
from typing import List


# DFS
def closedIsland(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if (
            r not in range(m)
            or c not in range(n)
            or grid[r][c] == 1
            or (r, c) in visited
        ):
            return

        grid[r][c] = 1
        visited.add((r, c))

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(m):
        for c in range(n):
            if (
                (r in [0, m - 1] or c in [0, n - 1])
                and grid[r][c] == 0
                and (r, c) not in visited
            ):
                dfs(r, c)

    island = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 0 and (r, c) not in visited:
                island += 1
                dfs(r, c)

    return island


grid = [
    [1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0],
]
print(closedIsland(grid))  # 2

```

## 130. Surrounded Regions

-   [LeetCode](https://leetcode.com/problems/surrounded-regions/) | [LeetCode CH](https://leetcode.cn/problems/surrounded-regions/) (Medium)

-   Tags: array, depth first search, breadth first search, union find, matrix

```python title="130. Surrounded Regions - Python Solution"
from collections import deque
from copy import deepcopy
from pprint import pprint
from typing import List


# 1. DFS
def solveDFS(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    if not board and not board[0]:
        return None

    m, n = len(board), len(board[0])

    def capture(r, c):
        if r not in range(m) or c not in range(n) or board[r][c] != "O":
            return None

        board[r][c] = "T"
        capture(r + 1, c)
        capture(r - 1, c)
        capture(r, c + 1)
        capture(r, c - 1)

    for r in range(m):
        for c in range(n):
            if board[r][c] == "O" and (r in [0, m - 1] or c in [0, n - 1]):
                capture(r, c)

    for r in range(m):
        for c in range(n):
            if board[r][c] == "O":
                board[r][c] = "X"

    for r in range(m):
        for c in range(n):
            if board[r][c] == "T":
                board[r][c] = "O"


# 2. BFS
def solveBFS(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    if not board and not board[0]:
        return None

    m, n = len(board), len(board[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def capture(r, c):
        q = deque([(r, c)])

        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if nr in range(m) and nc in range(n) and board[nr][nc] == "O":
                    q.append((nr, nc))
                    board[nr][nc] = "T"

    for r in range(m):
        for c in range(n):
            if board[r][c] == "O" and (r in [0, m - 1] or c in [0, n - 1]):
                board[r][c] = "T"
                capture(r, c)

    for r in range(m):
        for c in range(n):
            if board[r][c] == "O":
                board[r][c] = "X"

    for r in range(m):
        for c in range(n):
            if board[r][c] == "T":
                board[r][c] = "O"


board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
]
board1 = deepcopy(board)
solveDFS(board1)
pprint(board1)
# [['X', 'X', 'X', 'X'],
#  ['X', 'X', 'X', 'X'],
#  ['X', 'X', 'X', 'X'],
#  ['X', 'O', 'X', 'X']]

board2 = deepcopy(board)
solveBFS(board2)
pprint(board2)
# [['X', 'X', 'X', 'X'],
#  ['X', 'X', 'X', 'X'],
#  ['X', 'X', 'X', 'X'],
#  ['X', 'O', 'X', 'X']]

```

## 1905. Count Sub Islands

-   [LeetCode](https://leetcode.com/problems/count-sub-islands/) | [LeetCode CH](https://leetcode.cn/problems/count-sub-islands/) (Medium)

-   Tags: array, depth first search, breadth first search, union find, matrix

```python title="1905. Count Sub Islands - Python Solution"
from typing import List


# DFS
def countSubIslandsDFS(grid1: List[List[int]], grid2: List[List[int]]) -> int:
    m, n = len(grid2), len(grid2[0])
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def dfs(r, c, valid):
        grid2[r][c] = 0
        if grid1[r][c] == 0:
            valid = False
        for dr, dc in dirs:
            nr, nc = dr + r, dc + c
            if 0 <= nr < m and 0 <= nc < n and grid2[nr][nc] == 1:
                valid = dfs(nr, nc, valid)
        return valid

    res = 0

    for i in range(m):
        for j in range(n):
            if grid2[i][j] == 1:
                if dfs(i, j, True):
                    res += 1

    return res


grid1 = [
    [1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1],
]
grid2 = [
    [1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0],
]
print(countSubIslandsDFS(grid1, grid2))  # 3

```

## 1391. Check if There is a Valid Path in a Grid

-   [LeetCode](https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/) | [LeetCode CH](https://leetcode.cn/problems/check-if-there-is-a-valid-path-in-a-grid/) (Medium)

-   Tags: array, depth first search, breadth first search, union find, matrix

## 417. Pacific Atlantic Water Flow

-   [LeetCode](https://leetcode.com/problems/pacific-atlantic-water-flow/) | [LeetCode CH](https://leetcode.cn/problems/pacific-atlantic-water-flow/) (Medium)

-   Tags: array, depth first search, breadth first search, matrix

```python title="417. Pacific Atlantic Water Flow - Python Solution"
from collections import deque
from typing import List


# DFS
def pacificAtlanticDFS(heights: List[List[int]]) -> List[List[int]]:
    m, n = len(heights), len(heights[0])
    pac, atl = set(), set()
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def dfs(r, c, visited, prev_height):
        if (
            r not in range(m)
            or c not in range(n)
            or heights[r][c] < prev_height
            or (r, c) in visited
        ):
            return None

        visited.add((r, c))
        height = heights[r][c]
        for dr, dc in directions:
            dfs(dr + r, dc + c, visited, height)

    for c in range(n):
        dfs(0, c, pac, heights[0][c])
        dfs(m - 1, c, atl, heights[m - 1][c])

    for r in range(m):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, n - 1, atl, heights[r][n - 1])

    return list(pac & atl)


# BFS
def pacificAtlanticBFS(heights: List[List[int]]) -> List[List[int]]:
    m, n = len(heights), len(heights[0])
    pac, atl = set(), set()
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(r, c, visited):
        q = deque([(r, c)])
        visited.add((r, c))

        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if (
                    nr in range(m)
                    and nc in range(n)
                    and heights[row][col] <= heights[nr][nc]
                    and (nr, nc) not in visited
                ):
                    q.append((nr, nc))
                    visited.add((nr, nc))

    for c in range(n):
        bfs(0, c, pac)  # top
        bfs(m - 1, c, atl)  # bottom

    for r in range(m):
        bfs(r, 0, pac)  # left
        bfs(r, n - 1, atl)  # right

    return list(pac & atl)


heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]
print(pacificAtlanticDFS(heights))
# [(4, 0), (0, 4), (3, 1), (1, 4), (3, 0), (2, 2), (1, 3)]
print(pacificAtlanticBFS(heights))
# [(4, 0), (0, 4), (3, 1), (1, 4), (3, 0), (2, 2), (1, 3)]

```

## 529. Minesweeper

-   [LeetCode](https://leetcode.com/problems/minesweeper/) | [LeetCode CH](https://leetcode.cn/problems/minesweeper/) (Medium)

-   Tags: array, depth first search, breadth first search, matrix

## 1559. Detect Cycles in 2D Grid

-   [LeetCode](https://leetcode.com/problems/detect-cycles-in-2d-grid/) | [LeetCode CH](https://leetcode.cn/problems/detect-cycles-in-2d-grid/) (Medium)

-   Tags: array, depth first search, breadth first search, union find, matrix

## 827. Making A Large Island

-   [LeetCode](https://leetcode.com/problems/making-a-large-island/) | [LeetCode CH](https://leetcode.cn/problems/making-a-large-island/) (Hard)

-   Tags: array, depth first search, breadth first search, union find, matrix

```python title="827. Making A Large Island - Python Solution"
from collections import defaultdict
from typing import List


# Flood Fill
def largestIsland(grid: List[List[int]]) -> int:
    n = len(grid)
    areas = defaultdict(int)  # {index: area}
    index = 2
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(r, c, index):
        area = 1
        grid[r][c] = index
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                area += dfs(nr, nc, index)
        return area

    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                areas[index] = dfs(r, c, index)
                index += 1

    if not areas:
        return 1

    res = max(areas.values())

    for r in range(n):
        for c in range(n):
            if grid[r][c] == 0:
                connected = set()
                area = 1
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                        connected.add(grid[nr][nc])

                for island in connected:
                    area += areas[island]
                res = max(res, area)

    return res


grid = [[1, 0], [0, 1]]
print(largestIsland(grid))  # 3

```

## 305. Number of Islands II

-   [LeetCode](https://leetcode.com/problems/number-of-islands-ii/) | [LeetCode CH](https://leetcode.cn/problems/number-of-islands-ii/) (Hard)

-   Tags: array, hash table, union find

```python title="305. Number of Islands II - Python Solution"
from collections import defaultdict
from typing import List


# Union Find
def numIslands2(m: int, n: int, positions: List[List[int]]) -> List[int]:
    parent = defaultdict(tuple)
    islands = 0
    result = []
    visited = set()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def find(node):
        p = parent[node]
        while parent[p] != p:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        if p1 != p2:
            parent[p1] = p2
            return True
        return False

    for r, c in positions:
        if (r, c) in visited:
            result.append(islands)
            continue

        islands += 1
        parent[(r, c)] = (r, c)
        visited.add((r, c))

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (nr, nc) in visited:
                if union((r, c), (nr, nc)):
                    islands -= 1

        result.append(islands)

    return result


m = 3
n = 3
positions = [[0, 0], [0, 1], [1, 2], [2, 1]]
print(numIslands2(m, n, positions))  # [1, 1, 2, 3]

```

## 2061. Number of Spaces Cleaning Robot Cleaned

-   [LeetCode](https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/) | [LeetCode CH](https://leetcode.cn/problems/number-of-spaces-cleaning-robot-cleaned/) (Medium)

-   Tags: array, matrix, simulation

## 2852. Sum of Remoteness of All Cells

-   [LeetCode](https://leetcode.com/problems/sum-of-remoteness-of-all-cells/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-remoteness-of-all-cells/) (Medium)

-   Tags: array, hash table, depth first search, breadth first search, union find, matrix

## 489. Robot Room Cleaner

-   [LeetCode](https://leetcode.com/problems/robot-room-cleaner/) | [LeetCode CH](https://leetcode.cn/problems/robot-room-cleaner/) (Hard)

-   Tags: backtracking, interactive
