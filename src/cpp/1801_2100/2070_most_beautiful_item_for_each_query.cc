#include <algorithm>
#include <iostream>
#include <numeric>
#include <ranges>
#include <vector>
using namespace std;

vector<int> maximumBeauty(vector<vector<int>>& items, vector<int>& queries) {
    ranges::sort(items, {}, [](auto& item) { return item[0]; });
    vector<int> idx(queries.size());
    iota(idx.begin(), idx.end(), 0);
    ranges::sort(idx, {}, [&](int i) { return queries[i]; });

    vector<int> res(queries.size());
    int max_beauty = 0, j = 0;
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
    // 2 4 5 5 6 6
    for (int i : res) {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}
