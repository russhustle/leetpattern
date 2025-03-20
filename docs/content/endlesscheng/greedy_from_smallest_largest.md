---
comments: True
---

# Greedy from Smallest Largest

## Table of Contents

- [x] [3074. Apple Redistribution into Boxes](https://leetcode.cn/problems/apple-redistribution-into-boxes/) (Easy)
- [ ] [2279. Maximum Bags With Full Capacity of Rocks](https://leetcode.cn/problems/maximum-bags-with-full-capacity-of-rocks/) (Medium)
- [ ] [1833. Maximum Ice Cream Bars](https://leetcode.cn/problems/maximum-ice-cream-bars/) (Medium)
- [x] [1005. Maximize Sum Of Array After K Negations](https://leetcode.cn/problems/maximize-sum-of-array-after-k-negations/) (Easy)
- [ ] [1481. Least Number of Unique Integers after K Removals](https://leetcode.cn/problems/least-number-of-unique-integers-after-k-removals/) (Medium)
- [ ] [1403. Minimum Subsequence in Non-Increasing Order](https://leetcode.cn/problems/minimum-subsequence-in-non-increasing-order/) (Easy)
- [ ] [3010. Divide an Array Into Subarrays With Minimum Cost I](https://leetcode.cn/problems/divide-an-array-into-subarrays-with-minimum-cost-i/) (Easy)
- [ ] [1338. Reduce Array Size to The Half](https://leetcode.cn/problems/reduce-array-size-to-the-half/) (Medium)
- [ ] [1710. Maximum Units on a Truck](https://leetcode.cn/problems/maximum-units-on-a-truck/) (Easy)
- [x] [3075. Maximize Happiness of Selected Children](https://leetcode.cn/problems/maximize-happiness-of-selected-children/) (Medium)
- [ ] [2554. Maximum Number of Integers to Choose From a Range I](https://leetcode.cn/problems/maximum-number-of-integers-to-choose-from-a-range-i/) (Medium)
- [ ] [2126. Destroying Asteroids](https://leetcode.cn/problems/destroying-asteroids/) (Medium)
- [ ] [2587. Rearrange Array to Maximize Prefix Score](https://leetcode.cn/problems/rearrange-array-to-maximize-prefix-score/) (Medium)
- [ ] [976. Largest Perimeter Triangle](https://leetcode.cn/problems/largest-perimeter-triangle/) (Easy)
- [ ] [1561. Maximum Number of Coins You Can Get](https://leetcode.cn/problems/maximum-number-of-coins-you-can-get/) (Medium)
- [ ] [3301. Maximize the Total Height of Unique Towers](https://leetcode.cn/problems/maximize-the-total-height-of-unique-towers/) (Medium)
- [x] [945. Minimum Increment to Make Array Unique](https://leetcode.cn/problems/minimum-increment-to-make-array-unique/) (Medium)
- [ ] [1846. Maximum Element After Decreasing and Rearranging](https://leetcode.cn/problems/maximum-element-after-decreasing-and-rearranging/) (Medium)
- [ ] [1647. Minimum Deletions to Make Character Frequencies Unique](https://leetcode.cn/problems/minimum-deletions-to-make-character-frequencies-unique/) (Medium)
- [ ] [2971. Find Polygon With the Largest Perimeter](https://leetcode.cn/problems/find-polygon-with-the-largest-perimeter/) (Medium)
- [ ] [2178. Maximum Split of Positive Even Integers](https://leetcode.cn/problems/maximum-split-of-positive-even-integers/) (Medium)
- [ ] [2567. Minimum Score by Changing Two Elements](https://leetcode.cn/problems/minimum-score-by-changing-two-elements/) (Medium)
- [ ] [1509. Minimum Difference Between Largest and Smallest Value in Three Moves](https://leetcode.cn/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/) (Medium)
- [ ] [3397. Maximum Number of Distinct Elements After Operations](https://leetcode.cn/problems/maximum-number-of-distinct-elements-after-operations/) (Medium)
- [ ] [3457. Eat Pizzas!](https://leetcode.cn/problems/eat-pizzas/) (Medium)
- [ ] [1262. Greatest Sum Divisible by Three](https://leetcode.cn/problems/greatest-sum-divisible-by-three/) (Medium)
- [ ] [948. Bag of Tokens](https://leetcode.cn/problems/bag-of-tokens/) (Medium)
- [ ] [1775. Equal Sum Arrays With Minimum Number of Operations](https://leetcode.cn/problems/equal-sum-arrays-with-minimum-number-of-operations/) (Medium)
- [ ] [2333. Minimum Sum of Squared Difference](https://leetcode.cn/problems/minimum-sum-of-squared-difference/) (Medium)
- [ ] [3440. Reschedule Meetings for Maximum Free Time II](https://leetcode.cn/problems/reschedule-meetings-for-maximum-free-time-ii/) (Medium)
- [ ] [2141. Maximum Running Time of N Computers](https://leetcode.cn/problems/maximum-running-time-of-n-computers/) (Hard)
- [ ] [1196. How Many Apples Can You Put into the Basket](https://leetcode.cn/problems/how-many-apples-can-you-put-into-the-basket/) (Easy) 👑
- [ ] [2214. Minimum Health to Beat Game](https://leetcode.cn/problems/minimum-health-to-beat-game/) (Medium) 👑
- [ ] [2098. Subsequence of Size K With the Largest Even Sum](https://leetcode.cn/problems/subsequence-of-size-k-with-the-largest-even-sum/) (Medium) 👑
- [ ] [2548. Maximum Price to Fill a Bag](https://leetcode.cn/problems/maximum-price-to-fill-a-bag/) (Medium) 👑
- [ ] [3119. Maximum Number of Potholes That Can Be Fixed](https://leetcode.cn/problems/maximum-number-of-potholes-that-can-be-fixed/) (Medium) 👑
- [ ] [2557. Maximum Number of Integers to Choose From a Range II](https://leetcode.cn/problems/maximum-number-of-integers-to-choose-from-a-range-ii/) (Medium) 👑
- [x] [624. Maximum Distance in Arrays](https://leetcode.cn/problems/maximum-distance-in-arrays/) (Medium)
- [ ] [910. Smallest Range II](https://leetcode.cn/problems/smallest-range-ii/) (Medium)
- [ ] [2835. Minimum Operations to Form Subsequence With Target Sum](https://leetcode.cn/problems/minimum-operations-to-form-subsequence-with-target-sum/) (Hard)
- [ ] [3366. Minimum Array Sum](https://leetcode.cn/problems/minimum-array-sum/) (Medium)

## 3074. Apple Redistribution into Boxes

-   [LeetCode](https://leetcode.com/problems/apple-redistribution-into-boxes/) | [LeetCode CH](https://leetcode.cn/problems/apple-redistribution-into-boxes/) (Easy)

-   Tags: array, greedy, sorting

```python title="3074. Apple Redistribution into Boxes - Python Solution"
from typing import List


# Greedy
def minimumBoxes(apple: List[int], capacity: List[int]) -> int:
    target = sum(apple)
    capacity.sort(reverse=True)
    res = 0

    for box in capacity:
        res += 1
        target -= box
        if target <= 0:
            break

    return res


apple = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
assert minimumBoxes(apple, capacity) == 2

```

```cpp title="3074. Apple Redistribution into Boxes - C++ Solution"
#include <vector>
#include <numeric>
#include <algorithm>
#include <functional>
#include <iostream>

using namespace std;

class Solution
{
public:
    int minimumBoxes(vector<int> &apple, vector<int> &capacity)
    {
        int s = accumulate(apple.begin(), apple.end(), 0);
        sort(capacity.begin(), capacity.end(), greater<int>());

        int i = 0;
        while (s > 0)
        {
            s -= capacity[i++];
        }
        return i;
    }
};

int main()
{
    Solution s;
    vector<int> apple = {1, 3, 2};
    vector<int> capacity = {4, 3, 1, 5, 2};
    cout << s.minimumBoxes(apple, capacity) << endl;
    return 0;
}

```

## 2279. Maximum Bags With Full Capacity of Rocks

-   [LeetCode](https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/) | [LeetCode CH](https://leetcode.cn/problems/maximum-bags-with-full-capacity-of-rocks/) (Medium)

-   Tags: array, greedy, sorting

## 1833. Maximum Ice Cream Bars

-   [LeetCode](https://leetcode.com/problems/maximum-ice-cream-bars/) | [LeetCode CH](https://leetcode.cn/problems/maximum-ice-cream-bars/) (Medium)

-   Tags: array, greedy, sorting, counting sort

## 1005. Maximize Sum Of Array After K Negations

-   [LeetCode](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/) | [LeetCode CH](https://leetcode.cn/problems/maximize-sum-of-array-after-k-negations/) (Easy)

-   Tags: array, greedy, sorting
-   Return the maximum sum of the array after changing at most `k` elements.

```python title="1005. Maximize Sum Of Array After K Negations - Python Solution"
from heapq import heapify, heapreplace
from typing import List


# Greedy
def largestSumAfterKNegationsGreedy(nums: List[int], k: int) -> int:
    nums.sort(key=abs, reverse=True)

    for i in range(len(nums)):
        if nums[i] < 0 and k > 0:
            nums[i] *= -1
            k -= 1

    if k % 2:
        nums[-1] *= -1

    return sum(nums)


# Heap
def largestSumAfterKNegationsHeap(nums: List[int], k: int) -> int:
    heapify(nums)

    while k and nums[0] < 0:
        heapreplace(nums, -nums[0])
        k -= 1

    if k % 2:
        heapreplace(nums, -nums[0])

    return sum(nums)


print(largestSumAfterKNegationsGreedy([4, 2, 3], 1))  # 5
print(largestSumAfterKNegationsHeap([4, 2, 3], 1))

```

## 1481. Least Number of Unique Integers after K Removals

-   [LeetCode](https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/) | [LeetCode CH](https://leetcode.cn/problems/least-number-of-unique-integers-after-k-removals/) (Medium)

-   Tags: array, hash table, greedy, sorting, counting

## 1403. Minimum Subsequence in Non-Increasing Order

-   [LeetCode](https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/) | [LeetCode CH](https://leetcode.cn/problems/minimum-subsequence-in-non-increasing-order/) (Easy)

-   Tags: array, greedy, sorting

## 3010. Divide an Array Into Subarrays With Minimum Cost I

-   [LeetCode](https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/) | [LeetCode CH](https://leetcode.cn/problems/divide-an-array-into-subarrays-with-minimum-cost-i/) (Easy)

-   Tags: array, sorting, enumeration

## 1338. Reduce Array Size to The Half

-   [LeetCode](https://leetcode.com/problems/reduce-array-size-to-the-half/) | [LeetCode CH](https://leetcode.cn/problems/reduce-array-size-to-the-half/) (Medium)

-   Tags: array, hash table, greedy, sorting, heap priority queue

## 1710. Maximum Units on a Truck

-   [LeetCode](https://leetcode.com/problems/maximum-units-on-a-truck/) | [LeetCode CH](https://leetcode.cn/problems/maximum-units-on-a-truck/) (Easy)

-   Tags: array, greedy, sorting

## 3075. Maximize Happiness of Selected Children

-   [LeetCode](https://leetcode.com/problems/maximize-happiness-of-selected-children/) | [LeetCode CH](https://leetcode.cn/problems/maximize-happiness-of-selected-children/) (Medium)

-   Tags: array, greedy, sorting

```python title="3075. Maximize Happiness of Selected Children - Python Solution"
from typing import List


# Greedy
def maximumHappinessSum(happiness: List[int], k: int) -> int:
    selected = 0
    happinessScore = 0
    happiness.sort(reverse=True)

    for score in happiness:
        if selected == k:
            return happinessScore
        happinessScore += max(0, score - selected)
        selected += 1

    return happinessScore


happiness = [1, 2, 3]
k = 2
print(maximumHappinessSum(happiness, k))  # 4

```

## 2554. Maximum Number of Integers to Choose From a Range I

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-integers-to-choose-from-a-range-i/) (Medium)

-   Tags: array, hash table, binary search, greedy, sorting

## 2126. Destroying Asteroids

-   [LeetCode](https://leetcode.com/problems/destroying-asteroids/) | [LeetCode CH](https://leetcode.cn/problems/destroying-asteroids/) (Medium)

-   Tags: array, greedy, sorting

## 2587. Rearrange Array to Maximize Prefix Score

-   [LeetCode](https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/) | [LeetCode CH](https://leetcode.cn/problems/rearrange-array-to-maximize-prefix-score/) (Medium)

-   Tags: array, greedy, sorting, prefix sum

## 976. Largest Perimeter Triangle

-   [LeetCode](https://leetcode.com/problems/largest-perimeter-triangle/) | [LeetCode CH](https://leetcode.cn/problems/largest-perimeter-triangle/) (Easy)

-   Tags: array, math, greedy, sorting

## 1561. Maximum Number of Coins You Can Get

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-coins-you-can-get/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-coins-you-can-get/) (Medium)

-   Tags: array, math, greedy, sorting, game theory

## 3301. Maximize the Total Height of Unique Towers

-   [LeetCode](https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/) | [LeetCode CH](https://leetcode.cn/problems/maximize-the-total-height-of-unique-towers/) (Medium)

-   Tags: array, greedy, sorting

## 945. Minimum Increment to Make Array Unique

-   [LeetCode](https://leetcode.com/problems/minimum-increment-to-make-array-unique/) | [LeetCode CH](https://leetcode.cn/problems/minimum-increment-to-make-array-unique/) (Medium)

-   Tags: array, greedy, sorting, counting

```python title="945. Minimum Increment to Make Array Unique - Python Solution"
from typing import List


# Greedy
def minIncrementForUnique(nums: List[int]) -> int:
    nums.sort()
    moves = 0

    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            moves += nums[i - 1] + 1 - nums[i]
            nums[i] = nums[i - 1] + 1

    return moves


nums = [1, 2, 2]
print(minIncrementForUnique(nums))  # 1

```

## 1846. Maximum Element After Decreasing and Rearranging

-   [LeetCode](https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/) | [LeetCode CH](https://leetcode.cn/problems/maximum-element-after-decreasing-and-rearranging/) (Medium)

-   Tags: array, greedy, sorting

## 1647. Minimum Deletions to Make Character Frequencies Unique

-   [LeetCode](https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/) | [LeetCode CH](https://leetcode.cn/problems/minimum-deletions-to-make-character-frequencies-unique/) (Medium)

-   Tags: hash table, string, greedy, sorting

## 2971. Find Polygon With the Largest Perimeter

-   [LeetCode](https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/) | [LeetCode CH](https://leetcode.cn/problems/find-polygon-with-the-largest-perimeter/) (Medium)

-   Tags: array, greedy, sorting, prefix sum

## 2178. Maximum Split of Positive Even Integers

-   [LeetCode](https://leetcode.com/problems/maximum-split-of-positive-even-integers/) | [LeetCode CH](https://leetcode.cn/problems/maximum-split-of-positive-even-integers/) (Medium)

-   Tags: math, backtracking, greedy

## 2567. Minimum Score by Changing Two Elements

-   [LeetCode](https://leetcode.com/problems/minimum-score-by-changing-two-elements/) | [LeetCode CH](https://leetcode.cn/problems/minimum-score-by-changing-two-elements/) (Medium)

-   Tags: array, greedy, sorting

## 1509. Minimum Difference Between Largest and Smallest Value in Three Moves

-   [LeetCode](https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/) | [LeetCode CH](https://leetcode.cn/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/) (Medium)

-   Tags: array, greedy, sorting

## 3397. Maximum Number of Distinct Elements After Operations

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-distinct-elements-after-operations/) (Medium)

-   Tags: array, greedy, sorting

## 3457. Eat Pizzas!

-   [LeetCode](https://leetcode.com/problems/eat-pizzas/) | [LeetCode CH](https://leetcode.cn/problems/eat-pizzas/) (Medium)

-   Tags: array, greedy, sorting

## 1262. Greatest Sum Divisible by Three

-   [LeetCode](https://leetcode.com/problems/greatest-sum-divisible-by-three/) | [LeetCode CH](https://leetcode.cn/problems/greatest-sum-divisible-by-three/) (Medium)

-   Tags: array, dynamic programming, greedy, sorting

## 948. Bag of Tokens

-   [LeetCode](https://leetcode.com/problems/bag-of-tokens/) | [LeetCode CH](https://leetcode.cn/problems/bag-of-tokens/) (Medium)

-   Tags: array, two pointers, greedy, sorting

## 1775. Equal Sum Arrays With Minimum Number of Operations

-   [LeetCode](https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/) | [LeetCode CH](https://leetcode.cn/problems/equal-sum-arrays-with-minimum-number-of-operations/) (Medium)

-   Tags: array, hash table, greedy, counting

## 2333. Minimum Sum of Squared Difference

-   [LeetCode](https://leetcode.com/problems/minimum-sum-of-squared-difference/) | [LeetCode CH](https://leetcode.cn/problems/minimum-sum-of-squared-difference/) (Medium)

-   Tags: array, binary search, greedy, sorting, heap priority queue

## 3440. Reschedule Meetings for Maximum Free Time II

-   [LeetCode](https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/) | [LeetCode CH](https://leetcode.cn/problems/reschedule-meetings-for-maximum-free-time-ii/) (Medium)

-   Tags: array, greedy, enumeration

## 2141. Maximum Running Time of N Computers

-   [LeetCode](https://leetcode.com/problems/maximum-running-time-of-n-computers/) | [LeetCode CH](https://leetcode.cn/problems/maximum-running-time-of-n-computers/) (Hard)

-   Tags: array, binary search, greedy, sorting

## 1196. How Many Apples Can You Put into the Basket

-   [LeetCode](https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/) | [LeetCode CH](https://leetcode.cn/problems/how-many-apples-can-you-put-into-the-basket/) (Easy)

-   Tags: array, greedy, sorting

## 2214. Minimum Health to Beat Game

-   [LeetCode](https://leetcode.com/problems/minimum-health-to-beat-game/) | [LeetCode CH](https://leetcode.cn/problems/minimum-health-to-beat-game/) (Medium)

-   Tags: array, greedy

## 2098. Subsequence of Size K With the Largest Even Sum

-   [LeetCode](https://leetcode.com/problems/subsequence-of-size-k-with-the-largest-even-sum/) | [LeetCode CH](https://leetcode.cn/problems/subsequence-of-size-k-with-the-largest-even-sum/) (Medium)

-   Tags: array, greedy, sorting

## 2548. Maximum Price to Fill a Bag

-   [LeetCode](https://leetcode.com/problems/maximum-price-to-fill-a-bag/) | [LeetCode CH](https://leetcode.cn/problems/maximum-price-to-fill-a-bag/) (Medium)

-   Tags: array, greedy, sorting

## 3119. Maximum Number of Potholes That Can Be Fixed

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-potholes-that-can-be-fixed/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-potholes-that-can-be-fixed/) (Medium)

-   Tags: string, greedy, sorting

## 2557. Maximum Number of Integers to Choose From a Range II

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-ii/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-integers-to-choose-from-a-range-ii/) (Medium)

-   Tags: array, binary search, greedy, sorting

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

## 910. Smallest Range II

-   [LeetCode](https://leetcode.com/problems/smallest-range-ii/) | [LeetCode CH](https://leetcode.cn/problems/smallest-range-ii/) (Medium)

-   Tags: array, math, greedy, sorting

## 2835. Minimum Operations to Form Subsequence With Target Sum

-   [LeetCode](https://leetcode.com/problems/minimum-operations-to-form-subsequence-with-target-sum/) | [LeetCode CH](https://leetcode.cn/problems/minimum-operations-to-form-subsequence-with-target-sum/) (Hard)

-   Tags: array, greedy, bit manipulation

## 3366. Minimum Array Sum

-   [LeetCode](https://leetcode.com/problems/minimum-array-sum/) | [LeetCode CH](https://leetcode.cn/problems/minimum-array-sum/) (Medium)

-   Tags: array, dynamic programming
