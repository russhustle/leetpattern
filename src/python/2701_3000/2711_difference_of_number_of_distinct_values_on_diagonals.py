from typing import List


def differenceOfDistinctValues(grid: List[List[int]]) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    res = [[0] * n for _ in range(m)]
    st = set()

    for k in range(1, m + n):
        min_j = max(n - k, 0)
        max_j = min(m + n - 1 - k, n - 1)

        st.clear()
        for j in range(min_j, max_j + 1):
            i = k + j - n
            res[i][j] = len(st)
            st.add(grid[i][j])

        st.clear()
        for j in range(max_j, min_j - 1, -1):
            i = k + j - n
            res[i][j] = abs(res[i][j] - len(st))
            st.add(grid[i][j])

    return res


if __name__ == "__main__":
    grid = [[1, 2, 3], [3, 1, 5], [3, 2, 1]]
    print(differenceOfDistinctValues(grid))
    # [[1, 1, 0], [1, 0, 1], [0, 1, 1]]
