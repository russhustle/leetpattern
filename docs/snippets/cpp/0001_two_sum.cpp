#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> twoSum(vector<int> &nums, int target)
{
    unordered_map<int, int> hashmap;

    for (size_t i = 0; i < nums.size(); ++i)
    {
        int complement = target - nums[i];
        if (hashmap.find(complement) != hashmap.end())
        {
            return {hashmap[complement], static_cast<int>(i)};
        }
        hashmap[nums[i]] = i;
    }

    return {};
}

int main()
{
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> result = twoSum(nums, target);
    if (!result.empty())
    {
        printf("Two sum solution found: [%d, %d]\n", result[0], result[1]);
    }
    else
    {
        printf("Two sum solution not found\n");
    }
    return 0;
}
// Two sum solution found: [0, 1]