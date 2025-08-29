---
comments: True
---

# Left Right Pointers

## Table of Contents

- [x] [9. Palindrome Number](https://leetcode.cn/problems/palindrome-number/) (Easy)
- [x] [15. 3Sum](https://leetcode.cn/problems/3sum/) (Medium)
- [x] [18. 4Sum](https://leetcode.cn/problems/4sum/) (Medium)
- [x] [69. Sqrt(x)](https://leetcode.cn/problems/sqrtx/) (Easy)
- [x] [88. Merge Sorted Array](https://leetcode.cn/problems/merge-sorted-array/) (Easy)
- [x] [977. Squares of a Sorted Array](https://leetcode.cn/problems/squares-of-a-sorted-array/) (Easy)
- [x] [881. Boats to Save People](https://leetcode.cn/problems/boats-to-save-people/) (Medium)
- [x] [75. Sort Colors](https://leetcode.cn/problems/sort-colors/) (Medium)
- [x] [125. Valid Palindrome](https://leetcode.cn/problems/valid-palindrome/) (Easy)
- [x] [167. Two Sum II - Input Array Is Sorted](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/) (Medium)
- [x] [11. Container With Most Water](https://leetcode.cn/problems/container-with-most-water/) (Medium)

## 9. Palindrome Number

-   [LeetCode](https://leetcode.com/problems/palindrome-number/) | [LeetCode CH](https://leetcode.cn/problems/palindrome-number/) (Easy)

-   Tags: math
-   Return true if the given number is a palindrome. Otherwise, return false.

```python title="9. Palindrome Number - Python Solution"
# Reverse
def isPalindromeReverse(x: int) -> bool:
    if x < 0:
        return False

    return str(x) == str(x)[::-1]


# Left Right Pointers
def isPalindromeLR(x: int) -> bool:
    if x < 0:
        return False

    x = list(str(x))  # 121 -> ['1', '2', '1']

    left, right = 0, len(x) - 1

    while left < right:
        if x[left] != x[right]:
            return False
        left += 1
        right -= 1

    return True


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# |  Reverse   |  O(N)  |   O(N)  |
# | Left Right |  O(N)  |   O(1)  |
# |------------|--------|---------|


x = 121
print(isPalindromeReverse(x))  # True
print(isPalindromeLR(x))  # True

```

## 15. 3Sum

-   [LeetCode](https://leetcode.com/problems/3sum/) | [LeetCode CH](https://leetcode.cn/problems/3sum/) (Medium)

-   Tags: array, two pointers, sorting
```python title="15. 3Sum - Python Solution"
from typing import List


# Left Right Pointers
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    n = len(nums)

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total > 0:
                right -= 1
            elif total < 0:
                left += 1
            else:
                res.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return res


nums = [-1, 0, 1, 2, -1, -4]
assert threeSum(nums) == [[-1, -1, 2], [-1, 0, 1]]

```

```cpp title="15. 3Sum - C++ Solution"
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> threeSum(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> res;
    int n = nums.size();

    for (int i = 0; i < n - 2; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) {
            continue;
        }

        int left = i + 1, right = n - 1;

        while (left < right) {
            int total = nums[i] + nums[left] + nums[right];

            if (total > 0)
                right--;
            else if (total < 0)
                left++;
            else {
                res.push_back({nums[i], nums[left], nums[right]});
                while (left < right && nums[left] == nums[left + 1]) left++;
                while (left < right && nums[right] == nums[right - 1]) right--;
                left++;
                right--;
            }
        }
    }
    return res;
}

int main() {
    vector<int> nums = {-1, 0, 1, 2, -1, -4};
    vector<vector<int>> res = threeSum(nums);
    for (auto& v : res) {
        for (int i : v) {
            cout << i << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## 18. 4Sum

-   [LeetCode](https://leetcode.com/problems/4sum/) | [LeetCode CH](https://leetcode.cn/problems/4sum/) (Medium)

-   Tags: array, two pointers, sorting
```python title="18. 4Sum - Python Solution"
from typing import List


# Left Right Pointers
def fourSum(nums: List[int], target: int) -> List[List[int]]:
    """Returns all unique quadruplets that sum up to the target."""
    nums.sort()
    result = []

    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]

                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

    return result


nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums, target))
# [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

```

## 69. Sqrt(x)

-   [LeetCode](https://leetcode.com/problems/sqrtx/) | [LeetCode CH](https://leetcode.cn/problems/sqrtx/) (Easy)

-   Tags: math, binary search
```python title="69. Sqrt(x) - Python Solution"
# Left Right Pointers
def mySqrt(x: int) -> int:
    """Returns the square root of a number."""
    if x < 2:
        return x

    left, right = 0, x // 2

    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1


x = 8
print(mySqrt(x))  # 2

```

## 88. Merge Sorted Array

-   [LeetCode](https://leetcode.com/problems/merge-sorted-array/) | [LeetCode CH](https://leetcode.cn/problems/merge-sorted-array/) (Easy)

-   Tags: array, two pointers, sorting
```python title="88. Merge Sorted Array - Python Solution"
from typing import List


# Left Right Pointers
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """Merges two sorted arrays in-place."""
    p1, p2, t = m - 1, n - 1, m + n - 1

    while p1 >= 0 or p2 >= 0:
        if p1 == -1:
            nums1[t] = nums2[p2]
            p2 -= 1
        elif p2 == -1:
            nums1[t] = nums1[p1]
            p1 -= 1
        elif nums1[p1] > nums2[p2]:
            nums1[t] = nums1[p1]
            p1 -= 1
        else:
            nums1[t] = nums2[p2]
            p2 -= 1

        t -= 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  # [1, 2, 2, 3, 5, 6]

```

## 977. Squares of a Sorted Array

-   [LeetCode](https://leetcode.com/problems/squares-of-a-sorted-array/) | [LeetCode CH](https://leetcode.cn/problems/squares-of-a-sorted-array/) (Easy)

-   Tags: array, two pointers, sorting
```python title="977. Squares of a Sorted Array - Python Solution"
from typing import List


# Left Right Pointers
def sortedSquares(nums: List[int]) -> List[int]:
    """Returns the squares of the sorted array."""
    n = len(nums)
    result = [0 for _ in range(n)]

    left, right, tail = 0, n - 1, n - 1

    while left <= right:
        if abs(nums[left]) >= abs(nums[right]):
            result[tail] = nums[left] ** 2
            left += 1
        else:
            result[tail] = nums[right] ** 2
            right -= 1
        tail -= 1

    return result


# |---------------------|------|-------|
# | Approach            | Time | Space |
# |---------------------|------|-------|
# | Left Right Pointers | O(n) | O(n)  |
# |---------------------|------|-------|


nums = [-4, -1, 0, 3, 10]
print(sortedSquares(nums))  # [0, 1, 9, 16, 100]

```

## 881. Boats to Save People

-   [LeetCode](https://leetcode.com/problems/boats-to-save-people/) | [LeetCode CH](https://leetcode.cn/problems/boats-to-save-people/) (Medium)

-   Tags: array, two pointers, greedy, sorting
```python title="881. Boats to Save People - Python Solution"
from typing import List


# Left Right Pointers
def numRescueBoats(people: List[int], limit: int) -> int:
    """Returns the minimum number of boats to rescue people."""
    people.sort()
    left, right = 0, len(people) - 1
    boats = 0

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        boats += 1

    return boats


people = [3, 2, 2, 1]
limit = 3
print(numRescueBoats(people, limit))  # 3

```

## 75. Sort Colors

-   [LeetCode](https://leetcode.com/problems/sort-colors/) | [LeetCode CH](https://leetcode.cn/problems/sort-colors/) (Medium)

-   Tags: array, two pointers, sorting
```python title="75. Sort Colors - Python Solution"
from copy import deepcopy
from typing import List


# Left Right Pointers
def sort_colors_lr_pointers(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    left = 0
    for right in range(n):
        if nums[right] == 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

    for right in range(left, n):
        if nums[right] == 1:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1


# Three Pointers
def sort_colors_three_pointers(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    left, right = 0, len(nums) - 1
    cur = 0

    while cur <= right:
        if nums[cur] == 0:
            nums[left], nums[cur] = nums[cur], nums[left]
            left += 1
            cur += 1
        elif nums[cur] == 2:
            nums[right], nums[cur] = nums[cur], nums[right]
            right -= 1
        else:
            cur += 1


nums = [2, 0, 2, 1, 1, 0]
nums1, nums2 = deepcopy(nums), deepcopy(nums)
sort_colors_lr_pointers(nums1)
print(nums1)  # [0, 0, 1, 1, 2, 2]
sort_colors_three_pointers(nums2)
print(nums2)  # [0, 0, 1, 1, 2, 2]

```

## 125. Valid Palindrome

-   [LeetCode](https://leetcode.com/problems/valid-palindrome/) | [LeetCode CH](https://leetcode.cn/problems/valid-palindrome/) (Easy)

-   Tags: two pointers, string
```python title="125. Valid Palindrome - Python Solution"
# List Comprehension
def isPalindrome(s: str) -> bool:
    s = [char.lower() for char in s if char.isalnum()]
    return s == s[::-1]


# Left Right Pointers
def isPalindromeLR(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))  # True
print(isPalindromeLR(s))  # True

```

## 167. Two Sum II - Input Array Is Sorted

-   [LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [LeetCode CH](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/) (Medium)

-   Tags: array, two pointers, binary search
```python title="167. Two Sum II - Input Array Is Sorted - Python Solution"
from typing import List


# Left Right Pointers
def twoSum(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]

        if total > target:
            right -= 1
        elif total < target:
            left += 1
        else:
            return [left + 1, right + 1]


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# | Left Right |  O(n)  |  O(1)   |
# |------------|--------|---------|


numbers = [2, 7, 11, 15]
target = 9
print(twoSum(numbers, target))  # [1, 2]

```

## 11. Container With Most Water

-   [LeetCode](https://leetcode.com/problems/container-with-most-water/) | [LeetCode CH](https://leetcode.cn/problems/container-with-most-water/) (Medium)

-   Tags: array, two pointers, greedy
- Return the maximum area of water that can be trapped between the vertical lines.

![11](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

```python title="11. Container With Most Water - Python Solution"
from typing import List


# Brute Force
def maxAreaBF(height: List[int]) -> int:
    max_area = 0

    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            h = min(height[i], height[j])
            w = j - i
            max_area = max(max_area, h * w)

    return max_area


# Left Right Pointers
def maxAreaLR(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    res = 0

    while left < right:
        h = min(height[left], height[right])
        w = right - left
        res = max(res, h * w)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return res


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# | Brute Force| O(n^2) |  O(1)   |
# | Left Right |  O(n)  |  O(1)   |
# |------------|--------|---------|


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxAreaBF(height))  # 49
print(maxAreaLR(height))  # 49

```

```cpp title="11. Container With Most Water - C++ Solution"
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int maxArea(vector<int>& height) {
    int left = 0, right = height.size() - 1;
    int res = 0;

    while (left < right) {
        int h = min(height[left], height[right]);
        int w = right - left;
        res = max(res, h * w);

        if (height[left] < height[right])
            left++;
        else
            right--;
    }
    return res;
}

int main() {
    vector<int> height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    cout << maxArea(height) << endl;  // 49
    return 0;
}
```

