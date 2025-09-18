#include <cassert>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
   public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> last;

        for (size_t i = 0; i < nums.size(); i++) {
            int num = nums[i];
            if (last.contains(num) && ((int)i - last[num] <= k)) return true;
            last[num] = i;
        }
        return false;
    }
    bool containsNearbyDuplicateSlidingWindow(vector<int>& nums, int k) {
        unordered_set<int> window;

        for (size_t i = 0; i < nums.size(); i++) {
            if (window.contains(nums[i])) return true;
            window.insert(nums[i]);

            if ((int)i - k >= 0) {
                window.erase(nums[i - k]);
            }
        }
        return false;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3, 1};
    assert(solution.containsNearbyDuplicate(nums, 3));
    assert(solution.containsNearbyDuplicateSlidingWindow(nums, 3));
    return 0;
}