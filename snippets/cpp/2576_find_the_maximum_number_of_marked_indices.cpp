#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

int maxNumOfMarkedIndices(vector<int> &nums)
{
    sort(nums.begin(), nums.end());
    int n = nums.size();
    int slow = 0;
    int fast = n / 2;
    int count = 0;

    while (slow < n / 2 && fast < n)
    {
        if (nums[fast] >= 2 * nums[slow])
        {
            count += 2;
            slow++;
        }
        fast++;
    }
    return count;
}

int main()
{
    vector<int> nums = {1, 3, 2, 3, 1};
    int result = maxNumOfMarkedIndices(nums);
    printf("Result: %d\n", result);
    return 0;
}