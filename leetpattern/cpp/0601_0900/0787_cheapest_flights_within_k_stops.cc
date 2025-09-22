#include <cassert>
#include <climits>
#include <queue>
#include <vector>
using namespace std;

class FindCheapestPrice {
   public:
    int bellman_ford(int n, vector<vector<int>>& flights, int src, int dst,
                     int k) {
        vector<int> dist(n, INT_MAX);
        dist[src] = 0;

        for (int i = 0; i <= k; ++i) {
            vector<int> temp(dist);
            for (auto& flight : flights) {
                int u = flight[0], v = flight[1], w = flight[2];
                if (dist[u] != INT_MAX && dist[u] + w < temp[v]) {
                    temp[v] = dist[u] + w;
                }
            }
            dist = temp;
        }
        return dist[dst] == INT_MAX ? -1 : dist[dst];
    }

    int dijkstra(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<vector<pair<int, int>>> graph(n);
        for (auto& flight : flights) {
            graph[flight[0]].push_back({flight[1], flight[2]});
        }
        priority_queue<array<int, 3>, vector<array<int, 3>>,
                       greater<array<int, 3>>>
            min_heap;
        min_heap.push({0, src, k + 1});

        while (!min_heap.empty()) {
            auto [cost, u, stops] = min_heap.top();
            min_heap.pop();
            if (u == dst) {
                return cost;
            }
            if (stops > 0) {
                for (auto& [v, w] : graph[u]) {
                    min_heap.push({cost + w, v, stops - 1});
                }
            }
        }

        return -1;
    }
};

int main() {
    FindCheapestPrice solution;
    int n = 4;
    vector<vector<int>> flights = {
        {0, 1, 100}, {1, 2, 100}, {2, 0, 100}, {1, 3, 600}, {2, 3, 200}};
    int src = 0, dst = 3, k = 1;
    assert(solution.bellman_ford(n, flights, src, dst, k) == 700);
    assert(solution.dijkstra(n, flights, src, dst, k) == 700);

    return 0;
}
