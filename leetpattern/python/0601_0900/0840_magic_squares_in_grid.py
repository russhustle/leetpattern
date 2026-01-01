from typing import List


class numMagicSquaresInside:
    def matrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m < 3 or n < 3:
            return 0

        def is_magic(i, j):
            # 中心必须是 5
            if grid[i + 1][j + 1] != 5:
                return False

            # 检查是否是 1~9 且不重复
            nums = set()
            for x in range(3):
                for y in range(3):
                    nums.add(grid[i + x][j + y])
            if nums != set(range(1, 10)):
                return False

            s = 15
            # 行
            for x in range(3):
                if sum(grid[i + x][j : j + 3]) != s:
                    return False
            # 列
            for y in range(3):
                if grid[i][j + y] + grid[i + 1][j + y] + grid[i + 2][j + y] != s:
                    return False
            # 对角线
            if grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] != s:
                return False
            if grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] != s:
                return False

            return True

        res = 0
        for i in range(m - 2):
            for j in range(n - 2):
                if is_magic(i, j):
                    res += 1

        return res


if __name__ == "__main__":
    sol = numMagicSquaresInside()
    assert sol.matrix([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]) == 1
    assert sol.matrix([[10, 3, 5], [1, 6, 11], [7, 9, 2]]) == 0
