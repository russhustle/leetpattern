#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
   public:
    int max_area_of_island(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int res = 0;

        auto dfs = [&](this auto&& dfs, int r, int c) -> int {
            if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] != 1) {
                return 0;
            }
            grid[r][c] = 0;

            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) +
                   dfs(r, c - 1);
        };

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    int area = dfs(i, j);
                    res = max(res, area);
                }
            }
        }
        return res;
    }
};

int main() {
    Solution solution;
    vector<vector<int>> grid = {{0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
                                {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0},
                                {0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0},
                                {0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0},
                                {0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0},
                                {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0},
                                {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0},
                                {0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0}};
    assert(solution.max_area_of_island(grid) == 6);
    return 0;
}
