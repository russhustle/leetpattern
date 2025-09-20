#include <cassert>
#include <functional>
#include <queue>
#include <vector>
using namespace std;

class Solution {
   private:
    void dfs(vector<vector<int>>& image, int org, int color, int r, int c) {
        int m = image.size(), n = image[0].size();
        if (r < 0 || r >= m || c < 0 || c >= n || image[r][c] != org) {
            return;
        }
        image[r][c] = color;
        dfs(image, org, color, r - 1, c);
        dfs(image, org, color, r + 1, c);
        dfs(image, org, color, r, c - 1);
        dfs(image, org, color, r, c + 1);
    }

   public:
    // DFS
    vector<vector<int>> flood_fill_dfs(vector<vector<int>>& image, int sr,
                                       int sc, int color) {
        int org = image[sr][sc];
        if (org == color) return image;

        dfs(image, org, color, sr, sc);
        return image;
    }

    // DFS with lambda
    vector<vector<int>> flood_fill_dfs_lambda(vector<vector<int>>& image,
                                              int sr, int sc, int color) {
        int org = image[sr][sc];
        if (org == color) return image;

        int m = image.size(), n = image[0].size();

        function<void(int, int)> dfs = [&](int r, int c) -> void {
            if (r < 0 || r >= m || c < 0 || c >= n || image[r][c] != org) {
                return;
            }
            image[r][c] = color;
            dfs(r - 1, c);
            dfs(r + 1, c);
            dfs(r, c - 1);
            dfs(r, c + 1);
        };

        dfs(sr, sc);

        return image;
    }

    // BFS
    vector<vector<int>> flood_fill_bfs(vector<vector<int>>& image, int sr,
                                       int sc, int color) {
        int org = image[sr][sc];
        if (org == color) return image;

        int m = image.size(), n = image[0].size();
        vector<pair<int, int>> dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        queue<pair<int, int>> q;
        q.push({sr, sc});

        while (!q.empty()) {
            auto [r, c] = q.front();
            q.pop();
            image[r][c] = color;
            for (auto& dir : dirs) {
                int nr = r + dir.first;
                int nc = c + dir.second;
                if (nr >= 0 && nr < m && nc >= 0 && nc < n &&
                    image[nr][nc] == org) {
                    q.push({nr, nc});
                }
            }
        }

        return image;
    }
};

int main() {
    Solution solution;
    vector<vector<int>> image = {{1, 1, 1}, {1, 1, 0}, {1, 0, 1}};
    solution.flood_fill_dfs(image, 1, 1, 2);
    vector<vector<int>> expected = {{2, 2, 2}, {2, 2, 0}, {2, 0, 1}};
    assert((image == expected));

    image = {{1, 1, 1}, {1, 1, 0}, {1, 0, 1}};
    solution.flood_fill_dfs_lambda(image, 1, 1, 2);
    assert((image == expected));

    image = {{1, 1, 1}, {1, 1, 0}, {1, 0, 1}};
    solution.flood_fill_bfs(image, 1, 1, 2);
    assert((image == expected));
    return 0;
}
