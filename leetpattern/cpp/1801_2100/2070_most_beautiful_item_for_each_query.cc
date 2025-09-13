#include <algorithm>
#include <cassert>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

vector<int> maximumBeauty(vector<vector<int>>& items, vector<int>& queries) {
    std::sort(items.begin(), items.end(),
              [](const auto& a, const auto& b) { return a[0] < b[0]; });
    vector<int> idx(queries.size());
    iota(idx.begin(), idx.end(), 0);
    std::sort(idx.begin(), idx.end(),
              [&](int i, int j) { return queries[i] < queries[j]; });

    vector<int> res(queries.size());
    int max_beauty = 0;
    size_t j = 0;
    for (int i : idx) {
        int q = queries[i];
        while (j < items.size() && items[j][0] <= q) {
            max_beauty = max(max_beauty, items[j][1]);
            j++;
        }
        res[i] = max_beauty;
    }
    return res;
}

int main() {
    vector<vector<int>> items = {{1, 2}, {2, 4}, {3, 2}, {5, 6}, {3, 5}};
    vector<int> queries = {1, 2, 3, 4, 5, 6};
    vector<int> res = maximumBeauty(items, queries);
    assert((res == vector<int>{2, 4, 5, 5, 6, 6}));
    return 0;
}
