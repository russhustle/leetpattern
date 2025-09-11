#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

vector<int> rowAndMaximumOnes(vector<vector<int>>& mat) {
    vector<int> res = {0, 0};

    for (size_t i = 0; i < mat.size(); i++) {
        int cnt = accumulate(mat[i].begin(), mat[i].end(), 0);
        if (cnt > res[1]) {
            res[0] = (int)i;
            res[1] = cnt;
        }
    }
    return res;
}

int main() {
    vector<vector<int>> mat = {
        {0, 0, 0, 1}, {0, 1, 1, 1}, {1, 1, 1, 1}, {0, 0, 0, 0}};
    vector<int> res = rowAndMaximumOnes(mat);
    cout << res[0] << ", " << res[1] << endl;  // 2, 4
    return 0;
}
