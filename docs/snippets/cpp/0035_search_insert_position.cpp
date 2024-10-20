#include <vector>
#include <iostream>
using namespace std;

int searchInsert(vector<int> &nums, int target)
{
    int left = 0;
    int right = nums.size() - 1;

    while (left <= right)
    {
        int mid = left + (right - left) / 2;
        if (nums[mid] > target)
        {
            right = mid - 1;
        }
        else if (nums[mid] < target)
        {
            left = mid + 1;
        }
        else
        {
            return mid;
        }
    }
    return left;
}

int main()
{
    vector<int> nums = {1, 3, 5, 6};
    int target = 4;
    int result = searchInsert(nums, target);
    cout << result << endl;
    return 0;
}