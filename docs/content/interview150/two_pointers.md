---
comments: True
---

# Two Pointers

## Table of Contents

- [x] [125. Valid Palindrome](https://leetcode.cn/problems/valid-palindrome/) (Easy)
- [x] [392. Is Subsequence](https://leetcode.cn/problems/is-subsequence/) (Easy)
- [x] [167. Two Sum II - Input Array Is Sorted](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/) (Medium)
- [x] [11. Container With Most Water](https://leetcode.cn/problems/container-with-most-water/) (Medium)
- [x] [15. 3Sum](https://leetcode.cn/problems/3sum/) (Medium)

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

## 392. Is Subsequence

-   [LeetCode](https://leetcode.com/problems/is-subsequence/) | [LeetCode CH](https://leetcode.cn/problems/is-subsequence/) (Easy)

-   Tags: two pointers, string, dynamic programming
```python title="392. Is Subsequence - Python Solution"
# DP - LCS
def isSubsequenceLCS(s: str, t: str) -> bool:
    m = len(s)
    n = len(t)

    if m > n:
        return False

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    length = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = dp[i][j - 1]  # only delete t string

            if length < dp[i][j]:
                length = dp[i][j]

    return length == m


# Two Pointers
def isSubsequenceTP(s: str, t: str) -> bool:
    i, j = 0, 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)


s = "abc"
t = "ahbgdc"
print(isSubsequenceLCS(s, t))  # True
print(isSubsequenceTP(s, t))  # True

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
