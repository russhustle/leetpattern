#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int minMoves(vector<int>& nums) {
    int res = 0;
    int min_num = *min_element(nums.begin(), nums.end());

    for (int num : nums) {
        res += num - min_num;
    }

    return res;
}

int main() {
    vector<int> nums = {1, 2, 3};
    cout << minMoves(nums) << endl;  // 3
    return 0;
}
