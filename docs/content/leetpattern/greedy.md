---
comments: True
---

# Greedy

## Table of Contents

- [x] [455. Assign Cookies](https://leetcode.cn/problems/assign-cookies/) (Easy)
- [x] [1005. Maximize Sum Of Array After K Negations](https://leetcode.cn/problems/maximize-sum-of-array-after-k-negations/) (Easy)
- [x] [860. Lemonade Change](https://leetcode.cn/problems/lemonade-change/) (Easy)
- [x] [2037. Minimum Number of Moves to Seat Everyone](https://leetcode.cn/problems/minimum-number-of-moves-to-seat-everyone/) (Easy)
- [x] [376. Wiggle Subsequence](https://leetcode.cn/problems/wiggle-subsequence/) (Medium)
- [x] [738. Monotone Increasing Digits](https://leetcode.cn/problems/monotone-increasing-digits/) (Medium)
- [x] [122. Best Time to Buy and Sell Stock II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/) (Medium)
- [x] [714. Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) (Medium)
- [x] [135. Candy](https://leetcode.cn/problems/candy/) (Hard)
- [x] [406. Queue Reconstruction by Height](https://leetcode.cn/problems/queue-reconstruction-by-height/) (Medium)
- [x] [3075. Maximize Happiness of Selected Children](https://leetcode.cn/problems/maximize-happiness-of-selected-children/) (Medium)
- [x] [945. Minimum Increment to Make Array Unique](https://leetcode.cn/problems/minimum-increment-to-make-array-unique/) (Medium)
- [x] [53. Maximum Subarray](https://leetcode.cn/problems/maximum-subarray/) (Medium)
- [x] [134. Gas Station](https://leetcode.cn/problems/gas-station/) (Medium)
- [x] [968. Binary Tree Cameras](https://leetcode.cn/problems/binary-tree-cameras/) (Hard)
- [x] [1589. Maximum Sum Obtained of Any Permutation](https://leetcode.cn/problems/maximum-sum-obtained-of-any-permutation/) (Medium)

## 455. Assign Cookies

-   [LeetCode](https://leetcode.com/problems/assign-cookies/) | [LeetCode CH](https://leetcode.cn/problems/assign-cookies/) (Easy)

-   Tags: array, two pointers, greedy, sorting
-   Return the maximum number of your content children that can be satisfied.

```python title="455. Assign Cookies - Python Solution"
from typing import List


# Greedy
def findContentChildren(g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    i, j = 0, 0

    while i < len(g) and j < len(s):
        if g[i] <= s[j]:
            i += 1
        j += 1

    return i


# |-------------|-------------|--------------|
# |   Approach  |    Time     |    Space     |
# |-------------|-------------|--------------|
# |   Greedy    | O(N * logN) |    O(1)      |
# |-------------|-------------|--------------|


g = [1, 2, 3]
s = [1, 1]
print(findContentChildren(g, s))  # 1

```

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

## 860. Lemonade Change

-   [LeetCode](https://leetcode.com/problems/lemonade-change/) | [LeetCode CH](https://leetcode.cn/problems/lemonade-change/) (Easy)

-   Tags: array, greedy
-   Return `True` if and only if you can provide every customer with correct change.

```python title="860. Lemonade Change - Python Solution"
from typing import List


# Greedy
def lemonadeChange(bills: List[int]) -> bool:
    hashmap = {5: 0, 10: 0, 20: 0}

    for i in bills:
        if i == 5:
            hashmap[5] += 1

        if i == 10:
            if hashmap[5] < 1:
                return False

            hashmap[5] -= 1
            hashmap[10] += 1

        if i == 20:
            if hashmap[5] >= 1 and hashmap[10] >= 1:
                hashmap[5] -= 1
                hashmap[10] -= 1
                hashmap[20] += 1

            elif hashmap[5] >= 3:
                hashmap[5] -= 3
                hashmap[20] += 1

            else:
                return False

    return True


print(lemonadeChange([5, 5, 5, 10, 20]))  # True

```

## 2037. Minimum Number of Moves to Seat Everyone

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-moves-to-seat-everyone/) (Easy)

-   Tags: array, greedy, sorting, counting sort
-   Return the minimum number of moves needed to seat everyone.

```python title="2037. Minimum Number of Moves to Seat Everyone - Python Solution"
from typing import List


# Greedy
def minMovesToSeat(seats: List[int], students: List[int]) -> int:
    seats.sort()
    students.sort()
    moves = 0

    for i, j in zip(seats, students):
        moves += abs(i - j)

    return moves


print(minMovesToSeat([3, 1, 5], [2, 7, 4]))  # 4

```

## 376. Wiggle Subsequence

-   [LeetCode](https://leetcode.com/problems/wiggle-subsequence/) | [LeetCode CH](https://leetcode.cn/problems/wiggle-subsequence/) (Medium)

-   Tags: array, dynamic programming, greedy
-   Return the length of the longest wiggle subsequence.
-   `up[n]` stores the length of the longest wiggle subsequence ending at `n` with a rising wiggle.
-   `down[n]` stores the length of the longest wiggle subsequence ending at `n` with a falling wiggle.
-   Initialize `up[0] = 1` and `down[0] = 1`.
-   Example: `nums = [1, 7, 4, 9, 2, 5]`

| `nums[n]` | `nums[n-1]` | `up[n-1]` | `down[n-1]` | `up[n]` | `down[n]` |
| :-------: | :---------: | :-------: | :---------: | :-----: | :-------: |
|     1     |      -      |     -     |      -      |    1    |     1     |
|     7     |      1      |     1     |      1      |    2    |     1     |
|     4     |      7      |     2     |      1      |    2    |     3     |
|     9     |      4      |     2     |      3      |    4    |     3     |
|     2     |      9      |     4     |      3      |    4    |     5     |
|     5     |      2      |     4     |      5      |    6    |     5     |

```python title="376. Wiggle Subsequence - Python Solution"
from typing import List


# DP
def wiggleMaxLengthDP(nums: List[int]) -> int:
    if len(nums) <= 1:
        return len(nums)

    up = [0 for _ in range(len(nums))]
    down = [0 for _ in range(len(nums))]

    up[0], down[0] = 1, 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            up[i] = down[i - 1] + 1
            down[i] = down[i - 1]
        elif nums[i] < nums[i - 1]:
            down[i] = up[i - 1] + 1
            up[i] = up[i - 1]
        else:
            up[i] = up[i - 1]
            down[i] = down[i - 1]

    return max(up[-1], down[-1])


# Greedy
def wiggleMaxLengthGreedy(nums: List[int]) -> int:
    if len(nums) < 2:
        return len(nums)

    prev_diff = nums[1] - nums[0]
    count = 2 if prev_diff != 0 else 1

    for i in range(2, len(nums)):
        diff = nums[i] - nums[i - 1]
        if (diff > 0 and prev_diff <= 0) or (diff < 0 and prev_diff >= 0):
            count += 1
            prev_diff = diff

    return count


# |-------------|-----------------|--------------|
# |  Approach   |      Time       |    Space     |
# |-------------|-----------------|--------------|
# |    DP       |      O(n)       |     O(n)     |
# |  Greedy     |      O(n)       |     O(1)     |
# |-------------|-----------------|--------------|

nums = [1, 7, 4, 9, 2, 5]
print(wiggleMaxLengthDP(nums))  # 6
print(wiggleMaxLengthGreedy(nums))  # 6

```

## 738. Monotone Increasing Digits

-   [LeetCode](https://leetcode.com/problems/monotone-increasing-digits/) | [LeetCode CH](https://leetcode.cn/problems/monotone-increasing-digits/) (Medium)

-   Tags: math, greedy
-   Return the largest number that is less than or equal to `n` with monotone increasing digits.

```python title="738. Monotone Increasing Digits - Python Solution"
# Greedy
def monotoneIncreasingDigits(n: int) -> int:
    strNum = list(str(n))

    for i in range(len(strNum) - 2, -1, -1):
        if int(strNum[i]) > int(strNum[i + 1]):
            strNum[i] = str(int(strNum[i]) - 1)
            strNum[i + 1 :] = ["9"] * (len(strNum) - (i + 1))

    return int("".join(strNum))


n = 332
print(monotoneIncreasingDigits(n))  # 299

```

## 122. Best Time to Buy and Sell Stock II

-   [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | [LeetCode CH](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/) (Medium)

-   Tags: array, dynamic programming, greedy
-   Return the maximum profit you can achieve.

```python title="122. Best Time to Buy and Sell Stock II - Python Solution"
from typing import List


# DP
def maxProfitDP1(prices: List[int]) -> int:
    n = len(prices)
    if n <= 1:
        return 0

    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = -prices[0]
    dp[0][1] = 0

    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])

    return dp[-1][1]


# DP - Optimized
def maxProfitDP2(prices: List[int]) -> int:
    n = len(prices)
    if n <= 1:
        return 0

    hold = -prices[0]
    profit = 0

    for i in range(1, n):
        hold = max(hold, profit - prices[i])
        profit = max(profit, hold + prices[i])

    return profit


# Greedy
def maxProfitGreedy(prices: List[int]) -> int:
    profit = 0

    for i in range(1, len(prices)):
        profit += max(prices[i] - prices[i - 1], 0)

    return profit


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# |     DP1    |  O(n)  |   O(n)  |
# |     DP2    |  O(n)  |   O(1)  |
# |   Greedy   |  O(n)  |   O(1)  |
# |------------|--------|---------|


prices = [7, 1, 5, 3, 6, 4]
print(maxProfitDP1(prices))  # 7
print(maxProfitDP2(prices))  # 7
print(maxProfitGreedy(prices))  # 7

```

## 714. Best Time to Buy and Sell Stock with Transaction Fee

-   [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) | [LeetCode CH](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) (Medium)

-   Tags: array, dynamic programming, greedy
-   Return the maximum profit you can achieve with the given transaction fee.

```python title="714. Best Time to Buy and Sell Stock with Transaction Fee - Python Solution"
from typing import List


# 1. DP
def maxProfitDP(prices: List[int], fee: int) -> int:
    n = len(prices)
    if n <= 1:
        return 0

    dp = [[0] * 2 for _ in range(n)]

    dp[0][0] = -prices[0] - fee
    dp[0][1] = 0

    for i in range(1, n):
        dp[i][0] = max(
            dp[i - 1][0],  # hold
            dp[i - 1][1] - prices[i] - fee,  # buy
        )
        dp[i][1] = max(
            dp[i - 1][1],  # hold
            dp[i - 1][0] + prices[i],  # sell
        )

    return max(dp[-1])


# 2. Greedy
def maxProfitGreedy(prices: List[int], fee: int) -> int:
    n = len(prices)
    if n == 0:
        return 0

    buy = prices[0]
    profit = 0

    for i in range(1, n):
        if prices[i] < buy:
            buy = prices[i]
        elif prices[i] > buy + fee:
            profit += prices[i] - buy - fee
            buy = prices[i] - fee

    return profit


prices = [1, 3, 2, 8, 4, 9]
fee = 2
print(maxProfitDP(prices, fee))  # 8
print(maxProfitGreedy(prices, fee))  # 8

```

## 135. Candy

-   [LeetCode](https://leetcode.com/problems/candy/) | [LeetCode CH](https://leetcode.cn/problems/candy/) (Hard)

-   Tags: array, greedy
-   Return the minimum number of candies you must give.

```python title="135. Candy - Python Solution"
from typing import List


# Greedy
def candy(ratings: List[int]) -> int:
    # TC: O(n)
    # SC: O(n)
    n = len(ratings)

    if n <= 1:
        return n

    candy = [1 for _ in range(n)]

    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candy[i] = candy[i - 1] + 1

    for j in range(n - 2, -1, -1):
        if ratings[j] > ratings[j + 1]:
            candy[j] = max(candy[j], candy[j + 1] + 1)

    return sum(candy)


ratings = [1, 0, 2]
print(candy(ratings))  # 5

```

## 406. Queue Reconstruction by Height

-   [LeetCode](https://leetcode.com/problems/queue-reconstruction-by-height/) | [LeetCode CH](https://leetcode.cn/problems/queue-reconstruction-by-height/) (Medium)

-   Tags: array, binary indexed tree, segment tree, sorting
-   Reconstruct the queue.

```python title="406. Queue Reconstruction by Height - Python Solution"
from typing import List


# Greedy
def reconstructQueue(people: List[List[int]]) -> List[List[int]]:
    queue = []
    people.sort(key=lambda x: (-x[0], x[1]))

    for i in people:
        queue.insert(i[1], i)

    return queue


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(reconstructQueue(people))
# [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

```

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

## 968. Binary Tree Cameras

-   [LeetCode](https://leetcode.com/problems/binary-tree-cameras/) | [LeetCode CH](https://leetcode.cn/problems/binary-tree-cameras/) (Hard)

-   Tags: dynamic programming, tree, depth first search, binary tree
```python title="968. Binary Tree Cameras - Python Solution"
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


def minCameraCover(root: Optional[TreeNode]) -> int:
    res = 0

    def dfs(node, hasParent):
        if not node:
            return -1

        nonlocal res
        left, right = dfs(node.left, True), dfs(node.right, True)

        if left == -1 and right == -1:
            if hasParent:
                return 0
            res += 1
            return 2
        if left == 0 or right == 0:
            res += 1
            return 2
        if left == 2 or right == 2:
            return 1
        if hasParent:
            return 0
        res += 1
        return 2

    dfs(root, False)

    return res


root = build([0, 0, None, 0, 0])
print(root)
print(minCameraCover(root))  # 1

```

## 1589. Maximum Sum Obtained of Any Permutation

-   [LeetCode](https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/) | [LeetCode CH](https://leetcode.cn/problems/maximum-sum-obtained-of-any-permutation/) (Medium)

-   Tags: array, greedy, sorting, prefix sum
```python title="1589. Maximum Sum Obtained of Any Permutation - Python Solution"
from typing import List


# Greedy
def maxSumRangeQuery(nums: List[int], requests: List[List[int]]) -> int:
    n = len(nums)
    freq = [0 for _ in range(n + 1)]

    for start, end in requests:
        freq[start] += 1
        if end + 1 < n:
            freq[end + 1] -= 1

    for i in range(1, n):
        freq[i] += freq[i - 1]

    freq.pop()

    freq.sort(reverse=True)
    nums.sort(reverse=True)

    max_sum = 0
    mod = 10**9 + 7

    for i, j in zip(nums, freq):
        max_sum += i * j
        max_sum %= mod

    return max_sum


nums = [1, 2, 3, 4, 5]
requests = [[1, 3], [0, 1]]
print(maxSumRangeQuery(nums, requests))  # 19

```

