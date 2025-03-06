#include <vector>
#include <queue>
#include <iostream>

using namespace std;

vector<int> findOrder(int numCourses, vector<vector<int>> &prerequisites)
{
    vector<vector<int>> adj(numCourses);
    vector<int> in_degree(numCourses, 0);

    for (auto &pre : prerequisites)
    {
        adj[pre[1]].push_back(pre[0]);
        in_degree[pre[0]]++;
    }

    queue<int> q;
    for (int i = 0; i < numCourses; i++)
        if (in_degree[i] == 0)
            q.push(i);

    vector<int> order;

    while (!q.empty())
    {
        int course = q.front();
        q.pop();
        order.push_back(course);

        for (int next : adj[course])
            if (--in_degree[next] == 0)
                q.push(next);
    }

    return (int)order.size() == numCourses ? order : vector<int>{};
}

int main()
{
    vector<vector<int>> prerequisites{{1, 0}, {2, 0}, {3, 1}, {3, 2}};
    vector<int> res = findOrder(4, prerequisites);
    for (size_t i = 0; i < res.size(); i++)
        cout << res[i] << "\n";
    return 0;
}
