#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>

using namespace std;

int threeSumClosest(vector<int>& nums, int target) {
    sort(nums.begin(), nums.end());
    int n = nums.size();
    int res = 0;
    int minDiff = INT_MAX;

    for (int i = 0; i < n - 2; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) continue;

        int left = i + 1, right = n - 1;
        while (left < right) {
            int total = nums[i] + nums[left] + nums[right];

            int diff = abs(total - target);
            if (diff < minDiff) {
                minDiff = diff;
                res = total;
            }

            if (total > target)
                right--;
            else if (total < target)
                left++;
            else
                return total;
        }
    }
    return res;
}

int main() {
    vector<int> nums = {-1, 2, 1, -4};
    int target = 1;
    cout << threeSumClosest(nums, target) << endl;
    return 0;
}
