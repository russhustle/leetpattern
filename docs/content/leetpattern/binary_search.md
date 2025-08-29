---
comments: True
---

# Binary Search

## Table of Contents

- [x] [704. Binary Search](https://leetcode.cn/problems/binary-search/) (Easy)
- [x] [35. Search Insert Position](https://leetcode.cn/problems/search-insert-position/) (Easy)
- [x] [278. First Bad Version](https://leetcode.cn/problems/first-bad-version/) (Easy)
- [x] [34. Find First and Last Position of Element in Sorted Array](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/) (Medium)
- [x] [367. Valid Perfect Square](https://leetcode.cn/problems/valid-perfect-square/) (Easy)
- [x] [875. Koko Eating Bananas](https://leetcode.cn/problems/koko-eating-bananas/) (Medium)
- [x] [1011. Capacity To Ship Packages Within D Days](https://leetcode.cn/problems/capacity-to-ship-packages-within-d-days/) (Medium)
- [x] [378. Kth Smallest Element in a Sorted Matrix](https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/) (Medium)

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

## 278. First Bad Version

-   [LeetCode](https://leetcode.com/problems/first-bad-version/) | [LeetCode CH](https://leetcode.cn/problems/first-bad-version/) (Easy)

-   Tags: binary search, interactive
-   Find the first bad version given a function `isBadVersion`.

```python title="278. First Bad Version - Python Solution"
# Binary Search
def firstBadVersion(n: int) -> int:
    left, right = 1, n

    while left <= right:
        mid = left + (right - left) // 2

        if isBadVersion(mid):
            right = mid - 1
        else:
            left = mid + 1

    return left


def isBadVersion(version: int) -> bool:
    pass

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

## 367. Valid Perfect Square

-   [LeetCode](https://leetcode.com/problems/valid-perfect-square/) | [LeetCode CH](https://leetcode.cn/problems/valid-perfect-square/) (Easy)

-   Tags: math, binary search
-   Determine if a positive integer is a perfect square without using any built-in library function.

```python title="367. Valid Perfect Square - Python Solution"
# Binary Search
def isPerfectSquare(num: int) -> bool:
    if num < 2:
        return True

    left, right = 0, num // 2

    while left <= right:
        mid = left + (right - left) // 2

        if mid * mid == num:
            return True
        elif mid * mid < num:
            left = mid + 1
        else:
            right = mid - 1

    return False


num = 16
print(isPerfectSquare(num))  # True

```

## 875. Koko Eating Bananas

-   [LeetCode](https://leetcode.com/problems/koko-eating-bananas/) | [LeetCode CH](https://leetcode.cn/problems/koko-eating-bananas/) (Medium)

-   Tags: array, binary search
-   Koko loves to eat bananas. She wants to eat all the bananas within `H` hours. Each pile has a number of bananas. The `i-th` pile has `piles[i]` bananas. Return the minimum integer `K` such that she can eat all the bananas within `H` hours.

```python title="875. Koko Eating Bananas - Python Solution"
from typing import List


# Binary Search
def minEatingSpeed(piles: List[int], h: int) -> int:
    def canEat(piles, k, h):
        hours = 0
        for pile in piles:
            hours += (pile + k - 1) // k
        return hours <= h

    left, right = 1, max(piles)

    while left <= right:
        mid = left + (right - left) // 2

        if canEat(piles, mid, h):
            right = mid - 1
        else:
            left = mid + 1

    return left


piles = [3, 6, 7, 11]
h = 8
print(minEatingSpeed(piles, h))  # 4

```

## 1011. Capacity To Ship Packages Within D Days

-   [LeetCode](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | [LeetCode CH](https://leetcode.cn/problems/capacity-to-ship-packages-within-d-days/) (Medium)

-   Tags: array, binary search
-   A conveyor belt has packages that must be shipped from one port to another within `D` days. The `i-th` package has a weight of `weights[i]`. Each day, we load the ship with packages on the conveyor belt. The ship will be loaded with packages up to its capacity. The ship will not be loaded beyond its capacity. Return the least weight capacity of the ship.

```python title="1011. Capacity To Ship Packages Within D Days - Python Solution"
from typing import List


# Binary Search
def shipWithinDays(weights: List[int], days: int) -> int:

    def canShip(weights, D, capacity):
        days = 1
        current_weight = 0

        for weight in weights:
            if current_weight + weight > capacity:
                days += 1
                current_weight = 0
            current_weight += weight

        return days <= D

    left, right = max(weights), sum(weights)

    while left <= right:
        mid = left + (right - left) // 2

        if canShip(weights, days, mid):
            right = mid - 1
        else:
            left = mid + 1

    return left


weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
print(shipWithinDays(weights, days))  # 15

```

## 378. Kth Smallest Element in a Sorted Matrix

-   [LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | [LeetCode CH](https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/) (Medium)

-   Tags: array, binary search, sorting, heap priority queue, matrix
-   Given an `n x n` matrix where each of the rows and columns are sorted in ascending order, return the `k-th` smallest element in the matrix.

```python title="378. Kth Smallest Element in a Sorted Matrix - Python Solution"
from heapq import heapify, heappop, heappush
from typing import List


# Heap - Merge K Sorted
def kthSmallestHeap(matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    heap = [(matrix[i][0], i, 0) for i in range(n)]
    heapify(heap)

    for _ in range(k - 1):
        _, row, col = heappop(heap)

        if col + 1 < n:
            heappush(heap, (matrix[row][col + 1], row, col + 1))

    return heappop(heap)[0]


# Binary Search
def kthSmallestBinarySearch(matrix: List[List[int]], k: int) -> int:
    n = len(matrix)

    def check(mid):
        i, j = n - 1, 0
        num = 0

        while i >= 0 and j < n:
            if matrix[i][j] <= mid:
                num += i + 1
                j += 1
            else:
                i -= 1

        return num >= k

    left, right = matrix[0][0], matrix[-1][-1]

    while left < right:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1

    return left


matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8

print(kthSmallestHeap(matrix, k))  # 13
print(kthSmallestBinarySearch(matrix, k))  # 13

```
