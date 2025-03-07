#include <functional>
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
   public:
    int beautifulSubsets(vector<int>& nums, int k) {
        int res = 0;
        unordered_map<int, int> cnt;

        auto dfs = [&](auto&& self, int i) -> void {
            if (i == (int)nums.size()) {
                res++;
                return;
            }
            self(self, i + 1);  // Skip nums[i]
            int x = nums[i];
            if (cnt[x - k] == 0 && cnt[x + k] == 0) {
                cnt[x]++;
                self(self, i + 1);  // Include nums[i]
                cnt[x]--;           // Backtrack
            }
        };

        dfs(dfs, 0);

        return res - 1;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 2, 3, 4};
    int k = 1;
    cout << sol.beautifulSubsets(nums, k) << endl;
    return 0;
}
