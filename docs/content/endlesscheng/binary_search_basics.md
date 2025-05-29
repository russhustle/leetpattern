---
comments: True
---

# Binary Search Basics

## Table of Contents

- [x] [34. Find First and Last Position of Element in Sorted Array](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/) (Medium)
- [x] [35. Search Insert Position](https://leetcode.cn/problems/search-insert-position/) (Easy)
- [x] [704. Binary Search](https://leetcode.cn/problems/binary-search/) (Easy)
- [x] [744. Find Smallest Letter Greater Than Target](https://leetcode.cn/problems/find-smallest-letter-greater-than-target/) (Easy)
- [x] [2529. Maximum Count of Positive Integer and Negative Integer](https://leetcode.cn/problems/maximum-count-of-positive-integer-and-negative-integer/) (Easy)

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

## 704. Binary Search

-   [LeetCode](https://leetcode.com/problems/binary-search/) | [LeetCode CH](https://leetcode.cn/problems/binary-search/) (Easy)

-   Tags: array, binary search
- Implement binary search algorithm.


```python title="704. Binary Search - Python Solution"
from typing import List


# Binary Search [left, right]
def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid

    return -1


# Binary Search [left, right)
def search_half_open(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
        else:
            return mid

    return -1


# Binary Search (left, right)
def search_open_interval(nums: List[int], target: int) -> int:
    left, right = -1, len(nums)

    while left + 1 < right:
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid
        elif nums[mid] > target:
            right = mid
        else:
            return mid

    return -1


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    assert search(nums, target) == 4
    assert search_half_open(nums, target) == 4
    assert search_open_interval(nums, target) == 4

```

## 744. Find Smallest Letter Greater Than Target

-   [LeetCode](https://leetcode.com/problems/find-smallest-letter-greater-than-target/) | [LeetCode CH](https://leetcode.cn/problems/find-smallest-letter-greater-than-target/) (Easy)

-   Tags: array, binary search

```python title="744. Find Smallest Letter Greater Than Target - Python Solution"
from typing import List


# Binary Search
def nextGreatestLetter(letters: List[str], target: str) -> str:
    left, right = 0, len(letters)

    while left < right:
        mid = left + (right - left) // 2
        if letters[mid] > target:
            right = mid
        else:
            left = mid + 1

    return letters[left] if left < len(letters) else letters[0]


letters = ["c", "f", "j"]
target = "a"
print(nextGreatestLetter(letters, target))  # c

```

## 2529. Maximum Count of Positive Integer and Negative Integer

-   [LeetCode](https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/) | [LeetCode CH](https://leetcode.cn/problems/maximum-count-of-positive-integer-and-negative-integer/) (Easy)

-   Tags: array, binary search, counting

```python title="2529. Maximum Count of Positive Integer and Negative Integer - Python Solution"
from bisect import bisect_left, bisect_right
from typing import List


# Binary Search
def maximumCount(nums: List[int]) -> int:
    pos = bisect_left(nums, 0)
    neg = len(nums) - bisect_right(nums, 0)

    return max(pos, neg)


nums = [-2, -1, -1, 1, 2, 3]
print(maximumCount(nums))  # 3

```
