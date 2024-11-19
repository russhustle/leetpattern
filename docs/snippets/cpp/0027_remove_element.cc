#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    int removeElement(vector<int> &nums, int val)
    {
        int slow = 0;

        for (size_t fast = 0; fast < nums.size(); fast++)
        {
            if (val != nums[fast])
            {
                nums[slow++] = nums[fast];
            }
        }
        return slow;
    }
};

int main()
{
    Solution solution;
    vector<int> nums = {3, 2, 2, 3};
    int val = 3;
    cout << solution.removeElement(nums, val) << endl; // 2
    return 0;
}
