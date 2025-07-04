---
comments: True
---

# Greedy

## Table of Contents

- [x] [53. Maximum Subarray](https://leetcode.cn/problems/maximum-subarray/) (Medium)
- [x] [55. Jump Game](https://leetcode.cn/problems/jump-game/) (Medium)
- [x] [45. Jump Game II](https://leetcode.cn/problems/jump-game-ii/) (Medium)
- [x] [134. Gas Station](https://leetcode.cn/problems/gas-station/) (Medium)
- [x] [846. Hand of Straights](https://leetcode.cn/problems/hand-of-straights/) (Medium)
- [x] [1899. Merge Triplets to Form Target Triplet](https://leetcode.cn/problems/merge-triplets-to-form-target-triplet/) (Medium)
- [x] [763. Partition Labels](https://leetcode.cn/problems/partition-labels/) (Medium)
- [x] [678. Valid Parenthesis String](https://leetcode.cn/problems/valid-parenthesis-string/) (Medium)

## 53. Maximum Subarray

-   [LeetCode](https://leetcode.com/problems/maximum-subarray/) | [LeetCode CH](https://leetcode.cn/problems/maximum-subarray/) (Medium)

-   Tags: array, divide and conquer, dynamic programming

```python title="53. Maximum Subarray - Python Solution"
from typing import List


# DP Kadane
def maxSubArrayDP(nums: List[int]) -> int:
    dp = [0 for _ in range(len(nums))]

    dp[0] = nums[0]
    maxSum = nums[0]

    for i in range(1, len(nums)):
        dp[i] = max(
            dp[i - 1] + nums[i],  # continue the previous subarray
            nums[i],  # start a new subarray
        )
        maxSum = max(maxSum, dp[i])

    return maxSum


# Greedy
def maxSubArrayGreedy(nums: List[int]) -> int:
    max_sum = nums[0]
    cur_sum = 0

    for num in nums:
        cur_sum = max(cur_sum + num, num)
        max_sum = max(max_sum, cur_sum)

    return max_sum


# Prefix Sum
def maxSubArrayPrefixSum(nums: List[int]) -> int:
    prefix_sum = 0
    prefix_sum_min = 0
    res = float("-inf")

    for num in nums:
        prefix_sum += num
        res = max(res, prefix_sum - prefix_sum_min)
        prefix_sum_min = min(prefix_sum_min, prefix_sum)

    return res


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArrayDP(nums))  # 6
print(maxSubArrayGreedy(nums))  # 6
print(maxSubArrayPrefixSum(nums))  # 6

```

## 55. Jump Game

-   [LeetCode](https://leetcode.com/problems/jump-game/) | [LeetCode CH](https://leetcode.cn/problems/jump-game/) (Medium)

-   Tags: array, dynamic programming, greedy
- Return `True` if you can reach the last index, otherwise `False`.


```python title="55. Jump Game - Python Solution"
from typing import List


# Greedy - Interval
def canJump(nums: List[int]) -> bool:
    n = len(nums)
    reach = 0
    i = 0

    while reach >= i:
        if reach >= n - 1:
            return True
        reach = max(reach, i + nums[i])
        i += 1

    return False


if __name__ == "__main__":
    assert canJump([2, 3, 1, 1, 4]) is True
    assert canJump([3, 2, 1, 0, 4]) is False

```

```cpp title="55. Jump Game - C++ Solution"
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
   public:
    bool canJump(vector<int>& nums) {
        int canReach = 0;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            if (i > canReach) return false;
            canReach = max(canReach, i + nums[i]);
        }
        return true;
    }
};

int main() {
    Solution obj;
    vector<int> nums = {2, 3, 1, 1, 4};
    cout << obj.canJump(nums) << endl;
    return 0;
}

```

## 45. Jump Game II

-   [LeetCode](https://leetcode.com/problems/jump-game-ii/) | [LeetCode CH](https://leetcode.cn/problems/jump-game-ii/) (Medium)

-   Tags: array, dynamic programming, greedy
- Return the minimum number of jumps to reach the last index.


```python title="45. Jump Game II - Python Solution"
from typing import List


# Greedy - Interval
def jump(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return 0

    reach = 0
    left, right = 0, 0
    res = 0

    while right < n - 1:
        for i in range(left, right + 1):
            reach = max(reach, i + nums[i])

        left = right + 1
        right = reach
        res += 1

    return res


if __name__ == "__main__":
    assert jump([2, 3, 1, 1, 4]) == 2
    assert jump([2, 3, 0, 1, 4]) == 2

```

## 134. Gas Station

-   [LeetCode](https://leetcode.com/problems/gas-station/) | [LeetCode CH](https://leetcode.cn/problems/gas-station/) (Medium)

-   Tags: array, greedy

```python title="134. Gas Station - Python Solution"
from typing import List


# Greedy
def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    curSum = 0
    totalSum = 0
    start = 0

    for i in range(len(gas)):
        curSum += gas[i] - cost[i]
        totalSum += gas[i] - cost[i]

        if curSum < 0:
            start = i + 1
            curSum = 0

    if totalSum < 0:
        return -1

    return start


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(canCompleteCircuit(gas, cost))  # 3

```

## 846. Hand of Straights

-   [LeetCode](https://leetcode.com/problems/hand-of-straights/) | [LeetCode CH](https://leetcode.cn/problems/hand-of-straights/) (Medium)

-   Tags: array, hash table, greedy, sorting

```python title="846. Hand of Straights - Python Solution"
from collections import Counter
from typing import List


# Greedy
def isNStraightHand(hand: List[int], groupSize: int) -> bool:
    if len(hand) % groupSize != 0:
        return False

    count = Counter(hand)

    while count:
        minVal = min(count)
        for i in range(minVal, minVal + groupSize):
            if count[i] == 0:
                return False
            count[i] -= 1
            if count[i] == 0:
                del count[i]
    return True


hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3
print(isNStraightHand(hand, groupSize))  # True

```

## 1899. Merge Triplets to Form Target Triplet

-   [LeetCode](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) | [LeetCode CH](https://leetcode.cn/problems/merge-triplets-to-form-target-triplet/) (Medium)

-   Tags: array, greedy

```python title="1899. Merge Triplets to Form Target Triplet - Python Solution"
from typing import List


def mergeTriplets(triplets: List[List[int]], target: List[int]) -> bool:
    can_form = [False, False, False]

    for triplet in triplets:
        if all(triplet[i] <= target[i] for i in range(3)):
            for i in range(3):
                if triplet[i] == target[i]:
                    can_form[i] = True

    return all(can_form)


triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
target = [2, 7, 5]
print(mergeTriplets(triplets, target))  # True

```

## 763. Partition Labels

-   [LeetCode](https://leetcode.com/problems/partition-labels/) | [LeetCode CH](https://leetcode.cn/problems/partition-labels/) (Medium)

-   Tags: hash table, two pointers, string, greedy

```python title="763. Partition Labels - Python Solution"
from typing import List


# 1. Hashmap
def partitionLabels1(s: str) -> List[int]:
    hashmap = {}

    for i, j in enumerate(s):
        if j not in hashmap:
            hashmap[j] = [i, i]
        else:
            hashmap[j][1] = i

    intervals = list(hashmap.values())
    intervals.sort(key=lambda x: x[0])

    if len(intervals) < 2:
        return len(intervals)

    res = []
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            intervals[i][1] = max(intervals[i][1], intervals[i - 1][1])
        else:
            res.append(intervals[i][0])

    res.append(intervals[-1][1] + 1)

    if len(res) == 1:
        return res
    else:
        for i in range(len(res) - 1, 0, -1):
            res[i] -= res[i - 1]
        return res


# Single Pass Partitioning
def partitionLabels2(s: str) -> List[int]:
    last = {c: i for i, c in enumerate(s)}
    res = []
    start, end = 0, 0

    for i, c in enumerate(s):
        end = max(end, last[c])
        if end == i:
            res.append(end - start + 1)
            start = i + 1

    return res


print(partitionLabels1("abaccd"))  # [3, 2, 1]
print(partitionLabels2("abaccd"))  # [3, 2, 1]

```

## 678. Valid Parenthesis String

-   [LeetCode](https://leetcode.com/problems/valid-parenthesis-string/) | [LeetCode CH](https://leetcode.cn/problems/valid-parenthesis-string/) (Medium)

-   Tags: string, dynamic programming, stack, greedy

```python title="678. Valid Parenthesis String - Python Solution"
# Greedy
def checkValidString(s: str) -> bool:
    min_open, max_open = 0, 0

    for char in s:
        if char == "(":
            min_open += 1
            max_open += 1
        elif char == ")":
            min_open = max(min_open - 1, 0)
            max_open -= 1
        elif char == "*":
            min_open = max(min_open - 1, 0)
            max_open += 1

        if max_open < 0:
            return False

    return min_open == 0


s = "(*))"
print(checkValidString(s))  # True

```
