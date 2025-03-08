#include <iostream>
#include <vector>
using namespace std;

void wiggleSort(vector<int>& nums) {
    int n = nums.size();

    for (int i = 0; i < n - 1; i++) {
        if (i % 2 == 0) {
            if (nums[i] > nums[i + 1]) swap(nums[i], nums[i + 1]);
        } else {
            if (nums[i] < nums[i + 1]) swap(nums[i], nums[i + 1]);
        }
    }
}

int main() {
    vector<int> nums = {3, 5, 2, 1, 6, 4};
    wiggleSort(nums);
    // 3 5 1 6 2 4
    for (size_t i = 0; i < nums.size(); i++) {
        cout << nums[i] << " ";
    }
    cout << endl;
    return 0;
}
