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
