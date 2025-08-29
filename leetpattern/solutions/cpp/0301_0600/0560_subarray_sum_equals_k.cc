#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

int subarraySum(vector<int>& nums, int k) {
    int n = nums.size();
    vector<int> prefixSum(n + 1);
    for (int i = 0; i < n; i++) {
        prefixSum[i + 1] = prefixSum[i] + nums[i];
    }

    int res = 0;
    unordered_map<int, int> cnt;

    for (int ps : prefixSum) {
        if (cnt.find(ps - k) != cnt.end()) res += cnt[ps - k];
        cnt[ps]++;
    }
    return res;
}

int main() {
    vector<int> nums = {1, 1, 1};
    int k = 2;
    cout << subarraySum(nums, k) << endl;  // 2
    return 0;
}
