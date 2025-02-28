#include <vector>
#include <iostream>
using namespace std;

class Solution
{
  int bisect_left(vector<int> &nums, int target)
  {
    int left = 0, right = (int)nums.size() - 1;

    while (left <= right)
    {
      int mid = left + (right - left) / 2;
      if (nums[mid] < target)
      {
        left = mid + 1;
      }
      else
      {
        right = mid - 1;
      }
    }
    return left;
  }

public:
  vector<int> searchRange(vector<int> &nums, int target)
  {
    int left = bisect_left(nums, target);
    if (left == (int)nums.size() || nums[left] != target)
    {
      return {-1, -1};
    }
    int right = bisect_left(nums, target + 1) - 1;
    return {left, right};
  }
};

int main()
{
  vector<int> nums = {5, 7, 7, 8, 8, 10};
  int target = 8;
  Solution s;
  vector<int> res = s.searchRange(nums, target);
  cout << res[0] << ", " << res[1] << endl;
  return 0;
}
