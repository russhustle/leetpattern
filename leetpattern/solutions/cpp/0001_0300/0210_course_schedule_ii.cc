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
        vector<int> indegree(numCourses, 0);

        for (auto &pre : prerequisites) {
            graph[pre[1]].push_back(pre[0]);
            indegree[pre[0]]++;
        }

        queue<int> q;
        for (int i = 0; i < numCourses; i++)
            if (indegree[i] == 0) q.push(i);

        vector<int> order;

        while (!q.empty()) {
            int cur = q.front();
            q.pop();
            order.push_back(cur);

            for (int nxt : graph[cur]) {
                indegree[nxt]--;
                if (indegree[nxt] == 0) q.push(nxt);
            }
        }

        return (int)order.size() == numCourses ? order : vector<int>{};
    }
};

int main() {
    Solution obj;
    vector<vector<int>> prerequisites{{1, 0}, {2, 0}, {3, 1}, {3, 2}};
    vector<int> res = obj.findOrderBFS(4, prerequisites);
    for (size_t i = 0; i < res.size(); i++) cout << res[i] << "\n";
    return 0;
}
