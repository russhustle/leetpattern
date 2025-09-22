#include <algorithm>
#include <cassert>
#include <climits>
#include <queue>
#include <vector>
using namespace std;

class NetworkDelayTime {
   public:
    // single-source, non-negative weight -> Dijkstra's
    // https://leetcode.cn/problems/network-delay-time/solutions/2668220/liang-chong-dijkstra-xie-fa-fu-ti-dan-py-ooe8/
    int dijkstra(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int, int>>> graph(n + 1);
        for (auto& t : times) {
            graph[t[0]].push_back({t[1], t[2]});
        }

        vector<int> dist(n + 1, INT_MAX);
        // min heap
        priority_queue<pair<int, int>, vector<pair<int, int>>,
                       greater<pair<int, int>>>
            min_heap;

        dist[k] = 0;
        min_heap.push({0, k});  // [dist, node]

        while (!min_heap.empty()) {
            auto [d, u] = min_heap.top();
            min_heap.pop();

            if (d > dist[u]) continue;  // found the shortest

            for (auto& [v, w] : graph[u]) {
                if (dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    min_heap.push({dist[v], v});
                }
            }
        }

        int res = 0;
        for (int i = 1; i <= n; ++i) {
            if (dist[i] == INT_MAX) return -1;
            res = max(res, dist[i]);
        }
        return res;
    }

    // single source -> Bellman-Ford
    int bellman_ford(vector<vector<int>>& times, int n, int k) {
        vector<int> dist(n + 1, INT_MAX);
        dist[k] = 0;

        for (int i = 1; i <= n - 1; i++) {
            for (auto& edge : times) {
                int u = edge[0], v = edge[1], t = edge[2];
                if (dist[u] != INT_MAX && dist[v] > dist[u] + t) {
                    dist[v] = dist[u] + t;
                }
            }
        }

        int res = 0;
        for (int i = 1; i <= n; i++) {
            if (dist[i] == INT_MAX) return -1;
            res = max(res, dist[i]);
        }
        return res;
    }
};

int main() {
    NetworkDelayTime solution;
    vector<vector<int>> times = {{2, 1, 1}, {2, 3, 1}, {3, 4, 1}};
    assert(solution.dijkstra(times, 4, 2) == 2);
    assert(solution.bellman_ford(times, 4, 2) == 2);

    return 0;
}
