#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

// DP
int robDP(vector<int>& nums) {
    int n = nums.size();
    if (n <= 3) return *max_element(nums.begin(), nums.end());

    vector<int> dp1(n, 0), dp2(n, 0);

    dp1[0] = nums[0];
    dp2[1] = max(nums[0], nums[1]);
    for (int i = 2; i < n - 1; i++) {
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i]);
    }

    dp2[1] = nums[1];
    dp2[2] = max(nums[1], nums[2]);
    for (int i = 3; i < n; i++) {
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i]);
    }

    return max(dp1[n - 2], dp2[n - 1]);
}

// DP (Space Optimized)
int robDPOptimized(vector<int>& nums) {
    int n = nums.size();
    if (n <= 3) return *max_element(nums.begin(), nums.end());

    int f1 = nums[0];
    int f2 = max(nums[0], nums[1]);
    int res1;
    for (int i = 2; i < n - 1; i++) {
        res1 = max(f2, f1 + nums[i]);
        f1 = f2;
        f2 = res1;
    }

    f1 = nums[1];
    f2 = max(nums[1], nums[2]);
    int res2;
    for (int i = 3; i < n; i++) {
        res2 = max(f2, f1 + nums[i]);
        f1 = f2;
        f2 = res2;
    }

    return max(res1, res2);
}

int main() {
    vector<int> nums = {2, 3, 2};
    cout << robDP(nums) << endl;           // 3
    cout << robDPOptimized(nums) << endl;  // 3

    nums = {1, 2, 3, 1};
    cout << robDP(nums) << endl;           // 4
    cout << robDPOptimized(nums) << endl;  // 4

    return 0;
}
