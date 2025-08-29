#include <vector>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <functional>
using namespace std;

class Solution
{
public:
    long long countPairs(int n, vector<vector<int>> &edges)
    {
        unordered_map<int, unordered_set<int>> graph;
        for (const auto &edge : edges)
        {
            graph[edge[0]].insert(edge[1]);
            graph[edge[1]].insert(edge[0]);
        }

        unordered_set<int> visited;

        function<int(int)> dfs = [&](int node) -> int
        {
            if (visited.count(node))
            {
                return 0;
            }
            visited.insert(node);
            int count = 1;
            for (const auto &neighbor : graph[node])
            {
                if (!visited.count(neighbor))
                {
                    count += dfs(neighbor);
                }
            }
            return count;
        };

        long long res = 0;
        long long total = n;

        for (int i = 0; i < n; ++i)
        {
            if (!visited.count(i))
            {
                int count = dfs(i);
                res += count * (total - count);
            }
        }
        return res / 2;
    }
};

int main()
{
    Solution s;
    vector<vector<int>> edges = {{0, 2}, {0, 5}, {2, 4}, {1, 6}, {5, 4}};
    cout << s.countPairs(7, edges) << endl;
    return 0;
}
