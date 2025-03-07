#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
   public:
    bool canJump(vector<int>& nums) {
        int canReach = 0;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            if (i > canReach) return false;
            canReach = max(canReach, i + nums[i]);
        }
        return true;
    }
};

int main() {
    Solution obj;
    vector<int> nums = {2, 3, 1, 1, 4};
    cout << obj.canJump(nums) << endl;
    return 0;
}
