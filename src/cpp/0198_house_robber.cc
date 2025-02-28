#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    int rob(vector<int> &nums)
    {
        int prev = 0, cur = 0;

        for (int num : nums)
        {
            int temp = cur;
            cur = max(cur, prev + num);
            prev = temp;
        }
        return cur;
    }
};

int main()
{
    vector<int> nums = {2, 7, 9, 3, 1};
    Solution obj;
    int result = obj.rob(nums);
    cout << result << endl;
    return 0;
}
