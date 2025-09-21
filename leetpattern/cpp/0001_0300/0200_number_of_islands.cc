#include <cassert>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

class Solution {
   public:
    // dfs
    int num_islands_dfs(vector<vector<char>> &grid) {
        int m = grid.size(), n = grid[0].size();
        int res = 0;

        // c++23 lambda recursion
        auto dfs = [&](this auto &&dfs, int r, int c) -> void {
            if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] != '1') {
                return;
            }
            grid[r][c] = '0';
            dfs(r + 1, c);
            dfs(r - 1, c);
            dfs(r, c + 1);
            dfs(r, c - 1);
        };

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    res++;
                    dfs(i, j);
                }
            }
        }
        return res;
    }

    // bfs
    int num_islands_bfs(vector<vector<char>> &grid) {
        int m = grid.size(), n = grid[0].size();
        int res = 0;
        vector<pair<int, int>> dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        auto bfs = [&](int r, int c) {
            queue<pair<int, int>> q;
            q.push({r, c});
            grid[r][c] = '0';
            while (!q.empty()) {
                auto [cr, cc] = q.front();
                q.pop();
                for (auto &[dr, dc] : dirs) {
                    int nr = cr + dr, nc = cc + dc;
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n &&
                        grid[nr][nc] == '1') {
                        grid[nr][nc] = '0';
                        q.push({nr, nc});
                    }
                }
            }
        };

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    res++;
                    bfs(i, j);
                }
            }
        }
        return res;
    }
};

int main() {
    Solution solution;
    vector<vector<char>> grid = {{'1', '1', '0', '0', '0'},
                                 {'1', '1', '0', '0', '0'},
                                 {'0', '0', '1', '0', '0'},
                                 {'0', '0', '0', '1', '1'}};
    assert(solution.num_islands_dfs(grid) == 3);
    grid = {{'1', '1', '0', '0', '0'},
            {'1', '1', '0', '0', '0'},
            {'0', '0', '1', '0', '0'},
            {'0', '0', '0', '1', '1'}};
    assert(solution.num_islands_bfs(grid) == 3);
    return 0;
}
