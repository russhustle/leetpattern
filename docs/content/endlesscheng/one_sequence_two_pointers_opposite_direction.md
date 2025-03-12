---
comments: True
---

# One Sequence Two Pointers Opposite Direction

- [x] [344. Reverse String](https://leetcode.cn/problems/reverse-string/) (Easy)
- [x] [125. Valid Palindrome](https://leetcode.cn/problems/valid-palindrome/) (Easy)
- [x] [1750. Minimum Length of String After Deleting Similar Ends](https://leetcode.cn/problems/minimum-length-of-string-after-deleting-similar-ends/) (Medium)
- [ ] [2105. Watering Plants II](https://leetcode.cn/problems/watering-plants-ii/) (Medium)
- [x] [977. Squares of a Sorted Array](https://leetcode.cn/problems/squares-of-a-sorted-array/) (Easy)
- [ ] [658. Find K Closest Elements](https://leetcode.cn/problems/find-k-closest-elements/) (Medium)
- [ ] [1471. The k Strongest Values in an Array](https://leetcode.cn/problems/the-k-strongest-values-in-an-array/) (Medium)
- [x] [167. Two Sum II - Input Array Is Sorted](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/) (Medium)
- [ ] [633. Sum of Square Numbers](https://leetcode.cn/problems/sum-of-square-numbers/) (Medium)
- [ ] [2824. Count Pairs Whose Sum is Less than Target](https://leetcode.cn/problems/count-pairs-whose-sum-is-less-than-target/) (Easy)
- [x] [15. 3Sum](https://leetcode.cn/problems/3sum/) (Medium)
- [x] [16. 3Sum Closest](https://leetcode.cn/problems/3sum-closest/) (Medium)
- [x] [18. 4Sum](https://leetcode.cn/problems/4sum/) (Medium)
- [ ] [611. Valid Triangle Number](https://leetcode.cn/problems/valid-triangle-number/) (Medium)
- [ ] [1577. Number of Ways Where Square of Number Is Equal to Product of Two Numbers](https://leetcode.cn/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/) (Medium)
- [ ] [923. 3Sum With Multiplicity](https://leetcode.cn/problems/3sum-with-multiplicity/) (Medium)
- [ ] [948. Bag of Tokens](https://leetcode.cn/problems/bag-of-tokens/) (Medium)
- [x] [11. Container With Most Water](https://leetcode.cn/problems/container-with-most-water/) (Medium)
- [x] [42. Trapping Rain Water](https://leetcode.cn/problems/trapping-rain-water/) (Hard)
- [ ] [1616. Split Two Strings to Make Palindrome](https://leetcode.cn/problems/split-two-strings-to-make-palindrome/) (Medium)
- [ ] [1498. Number of Subsequences That Satisfy the Given Sum Condition](https://leetcode.cn/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/) (Medium)
- [ ] [1782. Count Pairs Of Nodes](https://leetcode.cn/problems/count-pairs-of-nodes/) (Hard)
- [x] [1099. Two Sum Less Than K](https://leetcode.cn/problems/two-sum-less-than-k/) (Easy) 👑
- [ ] [360. Sort Transformed Array](https://leetcode.cn/problems/sort-transformed-array/) (Medium) 👑
- [ ] [2422. Merge Operations to Turn Array Into a Palindrome](https://leetcode.cn/problems/merge-operations-to-turn-array-into-a-palindrome/) (Medium) 👑
- [ ] [259. 3Sum Smaller](https://leetcode.cn/problems/3sum-smaller/) (Medium) 👑

## 344. Reverse String

- [LeetCode](https://leetcode.com/problems/reverse-string/) | [LeetCode CH](https://leetcode.cn/problems/reverse-string/) (Easy)

- Tags: two pointers, string

```python title="344. Reverse String - Python Solution"
from typing import List


def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


s = ["h", "e", "l", "l", "o"]
reverseString(s)
print(s)  # ['o', 'l', 'l', 'e', 'h']

```

## 125. Valid Palindrome

- [LeetCode](https://leetcode.com/problems/valid-palindrome/) | [LeetCode CH](https://leetcode.cn/problems/valid-palindrome/) (Easy)

- Tags: two pointers, string

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

## 1750. Minimum Length of String After Deleting Similar Ends

- [LeetCode](https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/) | [LeetCode CH](https://leetcode.cn/problems/minimum-length-of-string-after-deleting-similar-ends/) (Medium)

- Tags: two pointers, string

```python title="1750. Minimum Length of String After Deleting Similar Ends - Python Solution"
# Sliding Window Variable Size
def minimumLength(s: str) -> int:
    left, right = 0, len(s) - 1

    while left < right and s[left] == s[right]:
        val = s[left]

        while left <= right and s[left] == val:
            left += 1
        while left <= right and s[right] == val:
            right -= 1

    return right - left + 1


print(minimumLength("cabaabac"))  # 0
print(minimumLength("aabccabba"))  # 3

```

## 2105. Watering Plants II

- [LeetCode](https://leetcode.com/problems/watering-plants-ii/) | [LeetCode CH](https://leetcode.cn/problems/watering-plants-ii/) (Medium)

- Tags: array, two pointers, simulation

## 977. Squares of a Sorted Array

- [LeetCode](https://leetcode.com/problems/squares-of-a-sorted-array/) | [LeetCode CH](https://leetcode.cn/problems/squares-of-a-sorted-array/) (Easy)

- Tags: array, two pointers, sorting

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

## 658. Find K Closest Elements

- [LeetCode](https://leetcode.com/problems/find-k-closest-elements/) | [LeetCode CH](https://leetcode.cn/problems/find-k-closest-elements/) (Medium)

- Tags: array, two pointers, binary search, sliding window, sorting, heap priority queue

## 1471. The k Strongest Values in an Array

- [LeetCode](https://leetcode.com/problems/the-k-strongest-values-in-an-array/) | [LeetCode CH](https://leetcode.cn/problems/the-k-strongest-values-in-an-array/) (Medium)

- Tags: array, two pointers, sorting

## 167. Two Sum II - Input Array Is Sorted

- [LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [LeetCode CH](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/) (Medium)

- Tags: array, two pointers, binary search

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

## 633. Sum of Square Numbers

- [LeetCode](https://leetcode.com/problems/sum-of-square-numbers/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-square-numbers/) (Medium)

- Tags: math, two pointers, binary search

## 2824. Count Pairs Whose Sum is Less than Target

- [LeetCode](https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/) | [LeetCode CH](https://leetcode.cn/problems/count-pairs-whose-sum-is-less-than-target/) (Easy)

- Tags: array, two pointers, binary search, sorting

## 15. 3Sum

- [LeetCode](https://leetcode.com/problems/3sum/) | [LeetCode CH](https://leetcode.cn/problems/3sum/) (Medium)

- Tags: array, two pointers, sorting

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

## 16. 3Sum Closest

- [LeetCode](https://leetcode.com/problems/3sum-closest/) | [LeetCode CH](https://leetcode.cn/problems/3sum-closest/) (Medium)

- Tags: array, two pointers, sorting

```python title="16. 3Sum Closest - Python Solution"
from typing import List


# Left Right Pointers
def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()
    n = len(nums)
    res = 0
    minDiff = float("inf")

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total > target:
                if total - target < minDiff:
                    minDiff = total - target
                    res = total
                right -= 1

            elif total < target:
                if target - total < minDiff:
                    minDiff = target - total
                    res = total
                left += 1

            else:
                return total

    return res


nums = [-1, 2, 1, -4]
target = 1
assert threeSumClosest(nums, target) == 2

```

```cpp title="16. 3Sum Closest - C++ Solution"
#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>

using namespace std;

int threeSumClosest(vector<int>& nums, int target) {
    sort(nums.begin(), nums.end());
    int n = nums.size();
    int res = 0;
    int minDiff = INT_MAX;

    for (int i = 0; i < n - 2; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) continue;

        int left = i + 1, right = n - 1;
        while (left < right) {
            int total = nums[i] + nums[left] + nums[right];

            int diff = abs(total - target);
            if (diff < minDiff) {
                minDiff = diff;
                res = total;
            }

            if (total > target)
                right--;
            else if (total < target)
                left++;
            else
                return total;
        }
    }
    return res;
}

int main() {
    vector<int> nums = {-1, 2, 1, -4};
    int target = 1;
    cout << threeSumClosest(nums, target) << endl;
    return 0;
}

```

## 18. 4Sum

- [LeetCode](https://leetcode.com/problems/4sum/) | [LeetCode CH](https://leetcode.cn/problems/4sum/) (Medium)

- Tags: array, two pointers, sorting

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

## 611. Valid Triangle Number

- [LeetCode](https://leetcode.com/problems/valid-triangle-number/) | [LeetCode CH](https://leetcode.cn/problems/valid-triangle-number/) (Medium)

- Tags: array, two pointers, binary search, greedy, sorting

## 1577. Number of Ways Where Square of Number Is Equal to Product of Two Numbers

- [LeetCode](https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/) | [LeetCode CH](https://leetcode.cn/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/) (Medium)

- Tags: array, hash table, math, two pointers

## 923. 3Sum With Multiplicity

- [LeetCode](https://leetcode.com/problems/3sum-with-multiplicity/) | [LeetCode CH](https://leetcode.cn/problems/3sum-with-multiplicity/) (Medium)

- Tags: array, hash table, two pointers, sorting, counting

## 948. Bag of Tokens

- [LeetCode](https://leetcode.com/problems/bag-of-tokens/) | [LeetCode CH](https://leetcode.cn/problems/bag-of-tokens/) (Medium)

- Tags: array, two pointers, greedy, sorting

## 11. Container With Most Water

- [LeetCode](https://leetcode.com/problems/container-with-most-water/) | [LeetCode CH](https://leetcode.cn/problems/container-with-most-water/) (Medium)

- Tags: array, two pointers, greedy
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

## 42. Trapping Rain Water

- [LeetCode](https://leetcode.com/problems/trapping-rain-water/) | [LeetCode CH](https://leetcode.cn/problems/trapping-rain-water/) (Hard)

- Tags: array, two pointers, dynamic programming, stack, monotonic stack
- ![42](../assets/0042.png)

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZI2z5pq0TqA?si=OEYg01dbmzvmtIwZ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

| Approach   | Time | Space |
| ---------- | ---- | ----- |
| DP         | O(N) | O(N)  |
| Left Right | O(N) | O(1)  |
| Monotonic  | O(N) | O(N)  |

```python title="42. Trapping Rain Water - Python Solution"
from typing import List


# DP
def trapDP(height: List[int]) -> int:
    if not height:
        return 0

    n = len(height)
    maxLeft, maxRight = [0 for _ in range(n)], [0 for _ in range(n)]

    for i in range(1, n):
        maxLeft[i] = max(maxLeft[i - 1], height[i - 1])

    for i in range(n - 2, -1, -1):
        maxRight[i] = max(maxRight[i + 1], height[i + 1])

    res = 0
    for i in range(n):
        res += max(0, min(maxLeft[i], maxRight[i]) - height[i])

    return res


# Left Right Pointers
def trapLR(height: List[int]) -> int:
    if not height:
        return 0

    left, right = 0, len(height) - 1
    maxL, maxR = height[left], height[right]
    res = 0

    while left < right:
        if maxL < maxR:
            left += 1
            maxL = max(maxL, height[left])
            res += maxL - height[left]
        else:
            right -= 1
            maxR = max(maxR, height[right])
            res += maxR - height[right]

    return res


# Monotonic Stack
def trapStack(height: List[int]) -> int:
    stack = []
    total = 0

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()
            if not stack:
                break
            distance = i - stack[-1] - 1
            bounded_height = min(height[i], height[stack[-1]]) - height[top]
            total += distance * bounded_height
        stack.append(i)

    return total


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trapDP(height))  # 6
print(trapLR(height))  # 6
print(trapStack(height))  # 6

```

```cpp title="42. Trapping Rain Water - C++ Solution"
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

class Solution
{
public:
    int trap(vector<int> &height)
    {
        if (height.empty())
            return 0;

        int res = 0;
        int left = 0, right = height.size() - 1;
        int maxL = height[left], maxR = height[right];

        while (left < right)
        {
            if (maxL < maxR)
            {
                left++;
                maxL = max(maxL, height[left]);
                res += maxL - height[left];
            }
            else
            {
                right--;
                maxR = max(maxR, height[right]);
                res += maxR - height[right];
            }
        }
        return res;
    }
};

int main()
{
    vector<int> height = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    Solution solution;
    cout << solution.trap(height) << endl;
    return 0;
}

```

## 1616. Split Two Strings to Make Palindrome

- [LeetCode](https://leetcode.com/problems/split-two-strings-to-make-palindrome/) | [LeetCode CH](https://leetcode.cn/problems/split-two-strings-to-make-palindrome/) (Medium)

- Tags: two pointers, string

## 1498. Number of Subsequences That Satisfy the Given Sum Condition

- [LeetCode](https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/) | [LeetCode CH](https://leetcode.cn/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/) (Medium)

- Tags: array, two pointers, binary search, sorting

## 1782. Count Pairs Of Nodes

- [LeetCode](https://leetcode.com/problems/count-pairs-of-nodes/) | [LeetCode CH](https://leetcode.cn/problems/count-pairs-of-nodes/) (Hard)

- Tags: array, two pointers, binary search, graph, sorting

## 1099. Two Sum Less Than K

- [LeetCode](https://leetcode.com/problems/two-sum-less-than-k/) | [LeetCode CH](https://leetcode.cn/problems/two-sum-less-than-k/) (Easy)

- Tags: array, two pointers, binary search, sorting

```python title="1099. Two Sum Less Than K - Python Solution"
from typing import List


# Left Right Pointers
def twoSumLessThanK(nums: List[int], k: int) -> int:
    nums.sort()
    left, right = 0, len(nums) - 1
    res = float("-inf")

    while left < right:
        total = nums[left] + nums[right]

        if total >= k:
            right -= 1
        else:
            res = max(res, total)
            left += 1

    return res if res != float("-inf") else -1


nums = [34, 23, 1, 24, 75, 33, 54, 8]
k = 60
print(twoSumLessThanK(nums, k))  # 58

```

## 360. Sort Transformed Array

- [LeetCode](https://leetcode.com/problems/sort-transformed-array/) | [LeetCode CH](https://leetcode.cn/problems/sort-transformed-array/) (Medium)

- Tags: array, math, two pointers, sorting

## 2422. Merge Operations to Turn Array Into a Palindrome

- [LeetCode](https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/) | [LeetCode CH](https://leetcode.cn/problems/merge-operations-to-turn-array-into-a-palindrome/) (Medium)

- Tags: array, two pointers, greedy

## 259. 3Sum Smaller

- [LeetCode](https://leetcode.com/problems/3sum-smaller/) | [LeetCode CH](https://leetcode.cn/problems/3sum-smaller/) (Medium)

- Tags: array, two pointers, binary search, sorting
