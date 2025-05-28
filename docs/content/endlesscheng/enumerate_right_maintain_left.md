---
comments: True
---

# Enumerate Right Maintain Left

## Table of Contents

- [x] [1. Two Sum](https://leetcode.cn/problems/two-sum/) (Easy)
- [x] [1512. Number of Good Pairs](https://leetcode.cn/problems/number-of-good-pairs/) (Easy)
- [x] [2001. Number of Pairs of Interchangeable Rectangles](https://leetcode.cn/problems/number-of-pairs-of-interchangeable-rectangles/) (Medium)
- [x] [219. Contains Duplicate II](https://leetcode.cn/problems/contains-duplicate-ii/) (Easy)
- [x] [121. Best Time to Buy and Sell Stock](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/) (Easy)
- [x] [624. Maximum Distance in Arrays](https://leetcode.cn/problems/maximum-distance-in-arrays/) (Medium)
- [x] [2815. Max Pair Sum in an Array](https://leetcode.cn/problems/max-pair-sum-in-an-array/) (Easy)
- [x] [2342. Max Sum of a Pair With Equal Sum of Digits](https://leetcode.cn/problems/max-sum-of-a-pair-with-equal-sum-of-digits/) (Medium)
- [ ] [1679. Max Number of K-Sum Pairs](https://leetcode.cn/problems/max-number-of-k-sum-pairs/) (Medium)
- [ ] [2260. Minimum Consecutive Cards to Pick Up](https://leetcode.cn/problems/minimum-consecutive-cards-to-pick-up/) (Medium)
- [ ] [1010. Pairs of Songs With Total Durations Divisible by 60](https://leetcode.cn/problems/pairs-of-songs-with-total-durations-divisible-by-60/) (Medium)
- [ ] [3185. Count Pairs That Form a Complete Day II](https://leetcode.cn/problems/count-pairs-that-form-a-complete-day-ii/) (Medium)
- [ ] [2506. Count Pairs Of Similar Strings](https://leetcode.cn/problems/count-pairs-of-similar-strings/) (Easy)
- [ ] [2748. Number of Beautiful Pairs](https://leetcode.cn/problems/number-of-beautiful-pairs/) (Easy)
- [x] [2874. Maximum Value of an Ordered Triplet II](https://leetcode.cn/problems/maximum-value-of-an-ordered-triplet-ii/) (Medium)
- [ ] [1014. Best Sightseeing Pair](https://leetcode.cn/problems/best-sightseeing-pair/) (Medium)
- [ ] [1814. Count Nice Pairs in an Array](https://leetcode.cn/problems/count-nice-pairs-in-an-array/) (Medium)
- [ ] [2905. Find Indices With Index and Value Difference II](https://leetcode.cn/problems/find-indices-with-index-and-value-difference-ii/) (Medium)
- [ ] [1031. Maximum Sum of Two Non-Overlapping Subarrays](https://leetcode.cn/problems/maximum-sum-of-two-non-overlapping-subarrays/) (Medium)
- [x] [2555. Maximize Win From Two Segments](https://leetcode.cn/problems/maximize-win-from-two-segments/) (Medium)
- [ ] [1995. Count Special Quadruplets](https://leetcode.cn/problems/count-special-quadruplets/) (Easy)
- [ ] [3404. Count Special Subsequences](https://leetcode.cn/problems/count-special-subsequences/) (Medium)
- [ ] [3267. Count Almost Equal Pairs II](https://leetcode.cn/problems/count-almost-equal-pairs-ii/) (Hard)
- [ ] [1214. Two Sum BSTs](https://leetcode.cn/problems/two-sum-bsts/) (Medium) 👑
- [ ] [2964. Number of Divisible Triplet Sums](https://leetcode.cn/problems/number-of-divisible-triplet-sums/) (Medium) 👑
- [ ] [2441. Largest Positive Integer That Exists With Its Negative](https://leetcode.cn/problems/largest-positive-integer-that-exists-with-its-negative/) (Easy)
- [x] [454. 4Sum II](https://leetcode.cn/problems/4sum-ii/) (Medium)
- [ ] [3371. Identify the Largest Outlier in an Array](https://leetcode.cn/problems/identify-the-largest-outlier-in-an-array/) (Medium)

## 1. Two Sum

-   [LeetCode](https://leetcode.com/problems/two-sum/) | [LeetCode CH](https://leetcode.cn/problems/two-sum/) (Easy)

-   Tags: array, hash table
-   Return the indices of the two numbers such that they add up to a specific target.

| Approach | Time Complexity | Space Complexity |
| :------: | :-------------: | :--------------: |
| Hashmap  |      O(n)       |       O(n)       |

```python title="1. Two Sum - Python Solution"
"""
- Return the indices of the two numbers such that they add up to a specific target.
- Approach: Use a hashmap to store the indices of the numbers.
- Time Complexity: O(n)
- Space Complexity: O(n)
"""

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}  # val: idx

    for idx, val in enumerate(nums):
        if (target - val) in hashmap:
            return [hashmap[target - val], idx]

        hashmap[val] = idx


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    assert twoSum(nums, target) == [0, 1]

```

```cpp title="1. Two Sum - C++ Solution"
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

vector<int> twoSum(vector<int> &nums, int target) {
    unordered_map<int, int> hashmap;

    for (size_t i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];

        if (hashmap.find(complement) != hashmap.end()) {
            return {hashmap[complement], (int)i};
        }
        hashmap[nums[i]] = (int)i;
    }

    return {-1, -1};
}

int main() {
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> result = twoSum(nums, target);
    cout << result[0] << ", " << result[1] << endl;
    return 0;
}

```

## 1512. Number of Good Pairs

-   [LeetCode](https://leetcode.com/problems/number-of-good-pairs/) | [LeetCode CH](https://leetcode.cn/problems/number-of-good-pairs/) (Easy)

-   Tags: array, hash table, math, counting

```python title="1512. Number of Good Pairs - Python Solution"
from collections import defaultdict
from typing import List


# Hash
def numIdenticalPairs(nums: List[int]) -> int:
    res = 0
    counts = defaultdict(int)  # num: count

    for num in nums:
        res += counts[num]
        counts[num] += 1

    return res


nums = [1, 2, 3, 1, 1, 3]
print(numIdenticalPairs(nums))  # 4

```

## 2001. Number of Pairs of Interchangeable Rectangles

-   [LeetCode](https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/) | [LeetCode CH](https://leetcode.cn/problems/number-of-pairs-of-interchangeable-rectangles/) (Medium)

-   Tags: array, hash table, math, counting, number theory

```python title="2001. Number of Pairs of Interchangeable Rectangles - Python Solution"
from collections import defaultdict
from typing import List


# Hash
def interchangeableRectangles(rectangles: List[List[int]]) -> int:
    res = 0
    counts = defaultdict(int)

    for w, h in rectangles:
        ratio = w / h
        res += counts[ratio]
        counts[ratio] += 1

    return res


rectangles = [[4, 8], [3, 6], [10, 20], [15, 30]]
print(interchangeableRectangles(rectangles))  # 6

```

## 219. Contains Duplicate II

-   [LeetCode](https://leetcode.com/problems/contains-duplicate-ii/) | [LeetCode CH](https://leetcode.cn/problems/contains-duplicate-ii/) (Easy)

-   Tags: array, hash table, sliding window

```python title="219. Contains Duplicate II - Python Solution"
from typing import List


# Hash
def containsNearbyDuplicateHash(nums: List[int], k: int) -> bool:
    hashmap = {}  # num: last index

    for idx, num in enumerate(nums):
        if num in hashmap:
            if idx - hashmap[num] <= k:
                return True

        hashmap[num] = idx

    return False


# Sliding window - Fixed
def containsNearbyDuplicateWindow(nums: List[int], k: int) -> bool:
    window = set()
    left = 0

    for right in range(len(nums)):
        if right - left > k:
            window.remove(nums[left])
            left += 1
        if nums[right] in window:
            return True
        window.add(nums[right])

    return False


nums = [1, 2, 3, 1]
k = 3
print(containsNearbyDuplicateHash(nums, k))  # True
print(containsNearbyDuplicateWindow(nums, k))  # True

```

## 121. Best Time to Buy and Sell Stock

-   [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | [LeetCode CH](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/) (Easy)

-   Tags: array, dynamic programming
-   Return the maximum profit that can be achieved from buying on one day and selling on another day.

```python title="121. Best Time to Buy and Sell Stock - Python Solution"
from typing import List


# Brute Force
def maxProfitBF(prices: List[int]) -> int:
    max_profit = 0
    n = len(prices)
    for i in range(n):
        for j in range(i + 1, n):
            max_profit = max(max_profit, prices[j] - prices[i])

    return max_profit


# DP
def maxProfitDP(prices: List[int]) -> int:
    dp = [[0] * 2 for _ in range(len(prices))]
    dp[0][0] = -prices[0]  # buy
    dp[0][1] = 0  # sell

    for i in range(1, len(prices)):
        dp[i][0] = max(dp[i - 1][0], -prices[i])  # the lowest price to buy
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])

    return dp[-1][1]


# Greedy
def maxProfitGreedy(prices: List[int]) -> int:
    max_profit = 0
    seen_min = prices[0]

    for i in range(1, len(prices)):
        max_profit = max(max_profit, prices[i] - seen_min)
        seen_min = min(seen_min, prices[i])

    return max_profit


# Fast Slow Pointers
def maxProfitFS(prices: List[int]) -> int:
    max_profit = 0
    slow, fast = 0, 1

    while fast < len(prices):
        if prices[fast] > prices[slow]:
            max_profit = max(max_profit, prices[fast] - prices[slow])
        else:
            slow = fast
        fast += 1

    return max_profit


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# | Brute Force|  O(n^2)|  O(1)   |
# | DP         |  O(n)  |  O(n)   |
# | Greedy     |  O(n)  |  O(1)   |
# | Fast Slow  |  O(n)  |  O(1)   |
# |------------|--------|---------|


prices = [7, 1, 5, 3, 6, 4]
print(maxProfitBF(prices))  # 5
print(maxProfitDP(prices))  # 5
print(maxProfitGreedy(prices))  # 5
print(maxProfitFS(prices))  # 5

```

```cpp title="121. Best Time to Buy and Sell Stock - C++ Solution"
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        if (prices.size() <= 1)
            return 0;

        int seen_min = prices[0];
        int res = 0;

        for (int &price : prices)
        {
            res = max(res, price - seen_min);
            seen_min = min(seen_min, price);
        }
        return res;
    }
};

int main()
{
    vector<int> prices = {7, 1, 5, 3, 6, 4};
    Solution obj;
    cout << obj.maxProfit(prices) << endl;
    return 0;
}

```

## 624. Maximum Distance in Arrays

-   [LeetCode](https://leetcode.com/problems/maximum-distance-in-arrays/) | [LeetCode CH](https://leetcode.cn/problems/maximum-distance-in-arrays/) (Medium)

-   Tags: array, greedy

```python title="624. Maximum Distance in Arrays - Python Solution"
from typing import List


# Array
def maxDistance(arrays: List[List[int]]) -> int:
    mn, mx = float("inf"), float("-inf")
    res = 0

    for arr in arrays:
        res = max(res, arr[-1] - mn, mx - arr[0])
        mn = min(mn, arr[0])
        mx = max(mx, arr[-1])

    return res


arrays = [[1, 2, 3], [4, 5], [1, 2, 3]]
print(maxDistance(arrays))  # 4

```

## 2815. Max Pair Sum in an Array

-   [LeetCode](https://leetcode.com/problems/max-pair-sum-in-an-array/) | [LeetCode CH](https://leetcode.cn/problems/max-pair-sum-in-an-array/) (Easy)

-   Tags: array, hash table

```python title="2815. Max Pair Sum in an Array - Python Solution"
from collections import defaultdict
from typing import List


# Hash
def maxSumHash(nums: List[int]) -> int:
    def find(num):
        res = 0
        while num != 0:
            num, carry = divmod(num, 10)
            res = max(res, carry)
        return res

    freqs = defaultdict(list)

    for num in nums:
        x = find(num)
        freqs[x].append(num)

    res = -1
    for vals in freqs.values():
        if len(vals) > 1:
            vals = sorted(vals, reverse=True)
            res = max(res, sum(vals[:2]))

    return res


# Array
def maxSumArray(nums: List[int]) -> int:
    res = -1
    max_val = [float("-inf") for _ in range(10)]

    for num in nums:
        maxDigit = max(map(int, str(num)))
        res = max(res, num + max_val[maxDigit])
        max_val[maxDigit] = max(max_val[maxDigit], num)

    return res


nums = [2536, 1613, 3366, 162]
print(maxSumHash(nums))  # 5902
print(maxSumArray(nums))  # 5902

```

## 2342. Max Sum of a Pair With Equal Sum of Digits

-   [LeetCode](https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/) | [LeetCode CH](https://leetcode.cn/problems/max-sum-of-a-pair-with-equal-sum-of-digits/) (Medium)

-   Tags: array, hash table, sorting, heap priority queue

```python title="2342. Max Sum of a Pair With Equal Sum of Digits - Python Solution"
from typing import List


# Enumerate Right Maintain Left
def maximumSum(nums: List[int]) -> int:
    def digits_sum(num):
        res = 0
        while num:
            num, carry = divmod(num, 10)
            res += carry
        return res

    hashmap = {}  # digit sum: largest num
    res = -1

    for num in nums:
        ds = digits_sum(num)

        if ds not in hashmap:
            hashmap[ds] = num
        else:
            res = max(res, num + hashmap[ds])
            hashmap[ds] = max(hashmap[ds], num)

    return res


nums = [18, 43, 36, 13, 7]
print(maximumSum(nums))  # 54

```

## 1679. Max Number of K-Sum Pairs

-   [LeetCode](https://leetcode.com/problems/max-number-of-k-sum-pairs/) | [LeetCode CH](https://leetcode.cn/problems/max-number-of-k-sum-pairs/) (Medium)

-   Tags: array, hash table, two pointers, sorting

## 2260. Minimum Consecutive Cards to Pick Up

-   [LeetCode](https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/) | [LeetCode CH](https://leetcode.cn/problems/minimum-consecutive-cards-to-pick-up/) (Medium)

-   Tags: array, hash table, sliding window

## 1010. Pairs of Songs With Total Durations Divisible by 60

-   [LeetCode](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/) | [LeetCode CH](https://leetcode.cn/problems/pairs-of-songs-with-total-durations-divisible-by-60/) (Medium)

-   Tags: array, hash table, counting

## 3185. Count Pairs That Form a Complete Day II

-   [LeetCode](https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/) | [LeetCode CH](https://leetcode.cn/problems/count-pairs-that-form-a-complete-day-ii/) (Medium)

-   Tags: array, hash table, counting

## 2506. Count Pairs Of Similar Strings

-   [LeetCode](https://leetcode.com/problems/count-pairs-of-similar-strings/) | [LeetCode CH](https://leetcode.cn/problems/count-pairs-of-similar-strings/) (Easy)

-   Tags: array, hash table, string, bit manipulation, counting

## 2748. Number of Beautiful Pairs

-   [LeetCode](https://leetcode.com/problems/number-of-beautiful-pairs/) | [LeetCode CH](https://leetcode.cn/problems/number-of-beautiful-pairs/) (Easy)

-   Tags: array, hash table, math, counting, number theory

## 2874. Maximum Value of an Ordered Triplet II

-   [LeetCode](https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/) | [LeetCode CH](https://leetcode.cn/problems/maximum-value-of-an-ordered-triplet-ii/) (Medium)

-   Tags: array

```python title="2874. Maximum Value of an Ordered Triplet II - Python Solution"
from typing import List


def maximumTripletValue(nums: List[int]) -> int:
    res = 0
    max_diff = 0
    max_prev = 0

    for num in nums:
        res = max(res, max_diff * num)
        max_diff = max(max_diff, max_prev - num)
        max_prev = max(max_prev, num)

    return res


if __name__ == "__main__":
    nums = [12, 6, 1, 2, 7]
    print(maximumTripletValue(nums))  # 77

```

## 1014. Best Sightseeing Pair

-   [LeetCode](https://leetcode.com/problems/best-sightseeing-pair/) | [LeetCode CH](https://leetcode.cn/problems/best-sightseeing-pair/) (Medium)

-   Tags: array, dynamic programming

## 1814. Count Nice Pairs in an Array

-   [LeetCode](https://leetcode.com/problems/count-nice-pairs-in-an-array/) | [LeetCode CH](https://leetcode.cn/problems/count-nice-pairs-in-an-array/) (Medium)

-   Tags: array, hash table, math, counting

## 2905. Find Indices With Index and Value Difference II

-   [LeetCode](https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/) | [LeetCode CH](https://leetcode.cn/problems/find-indices-with-index-and-value-difference-ii/) (Medium)

-   Tags: array, two pointers

## 1031. Maximum Sum of Two Non-Overlapping Subarrays

-   [LeetCode](https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/) | [LeetCode CH](https://leetcode.cn/problems/maximum-sum-of-two-non-overlapping-subarrays/) (Medium)

-   Tags: array, dynamic programming, sliding window

## 2555. Maximize Win From Two Segments

-   [LeetCode](https://leetcode.com/problems/maximize-win-from-two-segments/) | [LeetCode CH](https://leetcode.cn/problems/maximize-win-from-two-segments/) (Medium)

-   Tags: array, binary search, sliding window

```python title="2555. Maximize Win From Two Segments - Python Solution"
from typing import List


# Sliding Window - Variable
def maximizeWin(prizePositions: List[int], k: int) -> int:
    n = len(prizePositions)

    if 2 * k >= prizePositions[-1] - prizePositions[0]:
        return n

    ans = left = 0
    mx = [0] * (n + 1)

    for right, p in enumerate(prizePositions):
        while p - prizePositions[left] > k:
            left += 1
        ans = max(ans, mx[left] + right - left + 1)
        mx[right + 1] = max(mx[right], right - left + 1)

    return ans


prizePositions = [1, 1, 2, 2, 3, 3, 5]
k = 2
print(maximizeWin(prizePositions, k))  # 7

```

## 1995. Count Special Quadruplets

-   [LeetCode](https://leetcode.com/problems/count-special-quadruplets/) | [LeetCode CH](https://leetcode.cn/problems/count-special-quadruplets/) (Easy)

-   Tags: array, hash table, enumeration

## 3404. Count Special Subsequences

-   [LeetCode](https://leetcode.com/problems/count-special-subsequences/) | [LeetCode CH](https://leetcode.cn/problems/count-special-subsequences/) (Medium)

-   Tags: array, hash table, math, enumeration

## 3267. Count Almost Equal Pairs II

-   [LeetCode](https://leetcode.com/problems/count-almost-equal-pairs-ii/) | [LeetCode CH](https://leetcode.cn/problems/count-almost-equal-pairs-ii/) (Hard)

-   Tags: array, hash table, sorting, counting, enumeration

## 1214. Two Sum BSTs

-   [LeetCode](https://leetcode.com/problems/two-sum-bsts/) | [LeetCode CH](https://leetcode.cn/problems/two-sum-bsts/) (Medium)

-   Tags: two pointers, binary search, stack, tree, depth first search, binary search tree, binary tree

## 2964. Number of Divisible Triplet Sums

-   [LeetCode](https://leetcode.com/problems/number-of-divisible-triplet-sums/) | [LeetCode CH](https://leetcode.cn/problems/number-of-divisible-triplet-sums/) (Medium)

-   Tags: array, hash table

## 2441. Largest Positive Integer That Exists With Its Negative

-   [LeetCode](https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/) | [LeetCode CH](https://leetcode.cn/problems/largest-positive-integer-that-exists-with-its-negative/) (Easy)

-   Tags: array, hash table, two pointers, sorting

## 454. 4Sum II

-   [LeetCode](https://leetcode.com/problems/4sum-ii/) | [LeetCode CH](https://leetcode.cn/problems/4sum-ii/) (Medium)

-   Tags: array, hash table
-   Return the number of tuples `(i, j, k, l)` such that `A[i] + B[j] + C[k] + D[l] == 0`.

```python title="454. 4Sum II - Python Solution"
from collections import defaultdict
from typing import List


def fourSumCount(
    nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
) -> int:

    sumAB = defaultdict(int)
    result = 0

    for i in nums1:
        for j in nums2:
            sumAB[i + j] += 1

    for i in nums3:
        for j in nums4:
            if -(i + j) in sumAB:
                result += sumAB[-(i + j)]

    return result


nums1 = [1, 2]
nums2 = [-2, -1]
nums3 = [-1, 2]
nums4 = [0, 2]
print(fourSumCount(nums1, nums2, nums3, nums4))  # 2

```

## 3371. Identify the Largest Outlier in an Array

-   [LeetCode](https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/) | [LeetCode CH](https://leetcode.cn/problems/identify-the-largest-outlier-in-an-array/) (Medium)

-   Tags: array, hash table, counting, enumeration
