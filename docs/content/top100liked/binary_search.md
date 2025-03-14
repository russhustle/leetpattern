---
comments: True
---

# Binary Search

- [x] [35. Search Insert Position](https://leetcode.cn/problems/search-insert-position/) (Easy)
- [x] [74. Search a 2D Matrix](https://leetcode.cn/problems/search-a-2d-matrix/) (Medium)
- [x] [34. Find First and Last Position of Element in Sorted Array](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/) (Medium)
- [x] [33. Search in Rotated Sorted Array](https://leetcode.cn/problems/search-in-rotated-sorted-array/) (Medium)
- [x] [153. Find Minimum in Rotated Sorted Array](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/) (Medium)
- [x] [4. Median of Two Sorted Arrays](https://leetcode.cn/problems/median-of-two-sorted-arrays/) (Hard)

## 35. Search Insert Position

-   [LeetCode](https://leetcode.com/problems/search-insert-position/) | [LeetCode CH](https://leetcode.cn/problems/search-insert-position/) (Easy)

-   Tags: array, binary search
-   Return the index of the target if it is found. If not, return the index where it would be if it were inserted in order.

```python title="35. Search Insert Position - Python Solution"
from typing import List


# Binary Search
def searchInsert(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid

    return left


nums = [1, 3, 5, 6]
target = 5
print(searchInsert(nums, target))  # 2

```

## 74. Search a 2D Matrix

-   [LeetCode](https://leetcode.com/problems/search-a-2d-matrix/) | [LeetCode CH](https://leetcode.cn/problems/search-a-2d-matrix/) (Medium)

-   Tags: array, binary search, matrix

```python title="74. Search a 2D Matrix - Python Solution"
from typing import List


# Binary Search
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = left + (right - left) // 2
        mid_value = matrix[mid // n][mid % n]

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(searchMatrix(matrix, target))  # True

```

## 34. Find First and Last Position of Element in Sorted Array

-   [LeetCode](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | [LeetCode CH](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/) (Medium)

-   Tags: array, binary search
-   Find the starting and ending position of a given target value in a sorted array.

```python title="34. Find First and Last Position of Element in Sorted Array - Python Solution"
from bisect import bisect_left
from typing import List


# Binary Search
def searchRangeBS(nums: List[int], target: int) -> List[int]:
    def bisect_left(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    left = bisect_left(nums, target)
    right = bisect_left(nums, target + 1) - 1

    if left <= right:
        return [left, right]

    return [-1, -1]


# Bisect
def searchRangeBSBisect(nums: List[int], target: int) -> List[int]:
    if not nums:
        return [-1, -1]

    left = bisect_left(nums, target)
    right = bisect_left(nums, target + 1) - 1

    return [left, right] if left <= right else [-1, -1]


nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRangeBS(nums, target))  # [3, 4]
print(searchRangeBSBisect(nums, target))  # [3, 4]

```

```cpp title="34. Find First and Last Position of Element in Sorted Array - C++ Solution"
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

```

## 33. Search in Rotated Sorted Array

-   [LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [LeetCode CH](https://leetcode.cn/problems/search-in-rotated-sorted-array/) (Medium)

-   Tags: array, binary search

```python title="33. Search in Rotated Sorted Array - Python Solution"
from typing import List


# Binary Search
def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search(nums, target))  # 4

```

## 153. Find Minimum in Rotated Sorted Array

-   [LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [LeetCode CH](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/) (Medium)

-   Tags: array, binary search

```python title="153. Find Minimum in Rotated Sorted Array - Python Solution"
from typing import List


# Binary Search
def findMin(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[right]


nums = [4, 5, 6, 7, 0, 1, 2]
print(findMin(nums))  # 0

```

## 4. Median of Two Sorted Arrays

-   [LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/) | [LeetCode CH](https://leetcode.cn/problems/median-of-two-sorted-arrays/) (Hard)

-   Tags: array, binary search, divide and conquer

```python title="4. Median of Two Sorted Arrays - Python Solution"
from typing import List


# Brute Force
def findMedianSortedArraysBF(nums1: List[int], nums2: List[int]) -> float:
    nums = sorted(nums1 + nums2)
    n = len(nums)
    if n % 2 == 0:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2
    else:
        return nums[n // 2]


# Binary Search
def findMedianSortedArraysBS(nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    imin, imax, half_len = 0, m, (m + n + 1) // 2

    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i

        if i < m and nums2[j - 1] > nums1[i]:
            imin = i + 1
        elif i > 0 and nums1[i - 1] > nums2[j]:
            imax = i - 1
        else:
            if i == 0:
                max_of_left = nums2[j - 1]
            elif j == 0:
                max_of_left = nums1[i - 1]
            else:
                max_of_left = max(nums1[i - 1], nums2[j - 1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m:
                min_of_right = nums2[j]
            elif j == n:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i], nums2[j])

            return (max_of_left + min_of_right) / 2


# |--------------|-----------------|--------------|
# | Approach     | Time            | Space        |
# |--------------|-----------------|--------------|
# | Brute Force  | O((n+m)log(n+m))| O(n+m)       |
# | Binary Search| O(log(min(n,m)))| O(1)         |
# |--------------|-----------------|--------------|


nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArraysBF(nums1, nums2))  # 2.0
print(findMedianSortedArraysBS(nums1, nums2))  # 2.0

```
