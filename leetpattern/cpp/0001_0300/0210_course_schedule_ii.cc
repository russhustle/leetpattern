#include <cassert>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

class Solution {
   public:
    // BFS
    vector<int> findOrderBFS(int numCourses,
                             vector<vector<int>> &prerequisites) {
        vector<vector<int>> graph(numCourses);
        vector<int> in_degree(numCourses, 0);
        vector<int> res;

        for (auto &pre : prerequisites) {
            graph[pre[1]].push_back(pre[0]);
            in_degree[pre[0]]++;
        }

        queue<int> q;
        for (int i = 0; i < numCourses; i++)
            if (in_degree[i] == 0) q.push(i);

        while (!q.empty()) {
            int cur = q.front();
            q.pop();
            res.push_back(cur);

            for (int next : graph[cur]) {
                in_degree[next]--;
                if (in_degree[next] == 0) q.push(next);
            }
        }

        return (int)res.size() == numCourses ? res : vector<int>{};
    }
};

int main() {
    Solution obj;
    vector<vector<int>> prerequisites{{1, 0}, {2, 0}, {3, 1}, {3, 2}};
    vector<int> res = obj.findOrderBFS(4, prerequisites);
    assert((res == vector<int>{0, 1, 2, 3} || res == vector<int>{0, 2, 1, 3}));
    return 0;
}
