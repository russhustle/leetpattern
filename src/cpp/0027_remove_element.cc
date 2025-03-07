#include <iostream>
#include <vector>
using namespace std;

// Fast Slow Pointers
int removeElement(vector<int>& nums, int val) {
    size_t n = nums.size();
    size_t slow = 0, fast = 0;

    while (fast < n) {
        if (nums[fast] != val) {
            nums[slow] = nums[fast];
            slow++;
        }
        fast++;
    }
    return (int)slow;
}

int main() {
    vector<int> nums = {3, 2, 2, 3};
    int val = 3;
    cout << removeElement(nums, val) << endl;  // 2
    return 0;
}
