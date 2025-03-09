#include <iostream>
#include <vector>
using namespace std;

int rob(vector<int> &nums) {
    int prev = 0, cur = 0, temp = 0;

    for (int num : nums) {
        temp = cur;
        cur = max(cur, prev + num);
        prev = temp;
    }
    return cur;
}

int main() {
    vector<int> nums = {2, 7, 9, 3, 1};
    cout << rob(nums) << endl;  // 12
    return 0;
}
