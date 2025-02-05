#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    // DFS
    void dfs(vector<vector<int>> &isConnected, vector<bool> &visited, int i)
    {
        visited[i] = true;
        for (size_t j = 0; j < isConnected.size(); ++j)
        {
            if (isConnected[i][j] == 1 && !visited[j])
            {
                dfs(isConnected, visited, j);
            }
        }
    }

    int findCircleNumDFS(vector<vector<int>> &isConnected)
    {
        int n = isConnected.size();
        vector<bool> visited(n, false);
        int count = 0;
        for (int i = 0; i < n; ++i)
        {
            if (!visited[i])
            {
                dfs(isConnected, visited, i);
                ++count;
            }
        }
        return count;
    }

    // Union Find
    int Find(vector<int> &parent, int idx)
    {
        int par = parent[idx];
        while (par != parent[par])
        {
            parent[par] = parent[parent[par]];
            par = parent[par];
        }
        return par;
    }

    void Union(vector<int> &parent, int n1, int n2)
    {
        int p1 = Find(parent, n1);
        int p2 = Find(parent, n2);

        if (p1 == p2)
        {
            return;
        }
        parent[p1] = p2;

        return;
    }

    int findCircleNumDFSUnionFind(vector<vector<int>> &isConnected)
    {
        // init
        int num = isConnected.size();
        vector<int> parent(num);
        for (int i = 0; i < num; i++)
        {
            parent[i] = i;
        }

        for (int i = 0; i < num; i++)
        {
            for (int j = i + 1; j < num; j++)
            {
                if (isConnected[i][j] == 1)
                {
                    Union(parent, i, j);
                }
            }
        }

        int res = 0;
        for (int i = 0; i < num; i++)
        {
            if (parent[i] == i)
            {
                res++;
            }
        }

        return res;
    }
};

int main()
{
    Solution solution;
    vector<vector<int>> isConnected = {
        {1, 1, 0},
        {1, 1, 0},
        {0, 0, 1}};
    cout << "Number of Provinces: " << solution.findCircleNumDFS(isConnected) << endl;
    cout << "Number of Provinces: " << solution.findCircleNumDFSUnionFind(isConnected) << endl;
    return 0;
}
