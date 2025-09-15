#include <cassert>
#include <vector>
using namespace std;

class Solution {
   public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < target)
                left = mid + 1;
            else
                right = mid - 1;
        }
        return left;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 3, 5, 6};
    assert(solution.searchInsert(nums, 5) == 2);
    assert(solution.searchInsert(nums, 2) == 1);
    assert(solution.searchInsert(nums, 7) == 4);
    assert(solution.searchInsert(nums, 0) == 0);
    return 0;
}