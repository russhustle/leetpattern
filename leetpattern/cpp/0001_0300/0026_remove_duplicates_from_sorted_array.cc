#include <cassert>
#include <vector>
using namespace std;

class Solution {
   public:
    int removeDuplicates(vector<int>& nums) {
        int fast = 1, slow = 1;
        int n = nums.size();

        while (fast < n) {
            if (nums[fast] != nums[fast - 1]) {
                nums[slow] = nums[fast];
                slow++;
            }
            fast++;
        }
        return slow;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    assert(solution.removeDuplicates(nums) == 5);
    return 0;
}
