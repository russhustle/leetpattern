#include <iostream>
#include <vector>
using namespace std;

void moveZeroes(vector<int>& nums) {
    size_t n = nums.size();
    size_t fast = 0, slow = 0;

    while (fast < n) {
        if (nums[fast] != 0) {
            swap(nums[slow], nums[fast]);
            slow++;
        }
        fast++;
    }
}

int main() {
    vector<int> nums = {0, 1, 0, 3, 12};
    moveZeroes(nums);
    // [1, 3, 12, 0, 0]
    for (size_t i = 0; i < nums.size(); i++) {
        cout << nums[i] << " ";
    }
    cout << endl;
    return 0;
}
