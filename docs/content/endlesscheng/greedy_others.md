---
comments: True
---

# Greedy Others

## Table of Contents

- [ ] [2740. Find the Value of the Partition](https://leetcode.cn/problems/find-the-value-of-the-partition/) (Medium)
- [ ] [1033. Moving Stones Until Consecutive](https://leetcode.cn/problems/moving-stones-until-consecutive/) (Medium)
- [ ] [1864. Minimum Number of Swaps to Make the Binary String Alternating](https://leetcode.cn/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/) (Medium)
- [x] [1899. Merge Triplets to Form Target Triplet](https://leetcode.cn/problems/merge-triplets-to-form-target-triplet/) (Medium)
- [ ] [2498. Frog Jump II](https://leetcode.cn/problems/frog-jump-ii/) (Medium)
- [x] [134. Gas Station](https://leetcode.cn/problems/gas-station/) (Medium)
- [ ] [2311. Longest Binary Subsequence Less Than or Equal to K](https://leetcode.cn/problems/longest-binary-subsequence-less-than-or-equal-to-k/) (Medium)
- [ ] [3443. Maximum Manhattan Distance After K Changes](https://leetcode.cn/problems/maximum-manhattan-distance-after-k-changes/) (Medium)
- [ ] [3002. Maximum Size of a Set After Removals](https://leetcode.cn/problems/maximum-size-of-a-set-after-removals/) (Medium)
- [ ] [2412. Minimum Money Required Before Transactions](https://leetcode.cn/problems/minimum-money-required-before-transactions/) (Hard)
- [ ] [659. Split Array into Consecutive Subsequences](https://leetcode.cn/problems/split-array-into-consecutive-subsequences/) (Medium)
- [ ] [2732. Find a Good Subset of the Matrix](https://leetcode.cn/problems/find-a-good-subset-of-the-matrix/) (Hard)
- [ ] [2790. Maximum Number of Groups With Increasing Length](https://leetcode.cn/problems/maximum-number-of-groups-with-increasing-length/) (Hard)
- [ ] [782. Transform to Chessboard](https://leetcode.cn/problems/transform-to-chessboard/) (Hard)
- [ ] [420. Strong Password Checker](https://leetcode.cn/problems/strong-password-checker/) (Hard)
- [ ] [2753. Count Houses in a Circular Street II](https://leetcode.cn/problems/count-houses-in-a-circular-street-ii/) (Hard) 👑

## 2740. Find the Value of the Partition

-   [LeetCode](https://leetcode.com/problems/find-the-value-of-the-partition/) | [LeetCode CH](https://leetcode.cn/problems/find-the-value-of-the-partition/) (Medium)

-   Tags: array, sorting
## 1033. Moving Stones Until Consecutive

-   [LeetCode](https://leetcode.com/problems/moving-stones-until-consecutive/) | [LeetCode CH](https://leetcode.cn/problems/moving-stones-until-consecutive/) (Medium)

-   Tags: math, brainteaser
## 1864. Minimum Number of Swaps to Make the Binary String Alternating

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/) (Medium)

-   Tags: string, greedy
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

## 2498. Frog Jump II

-   [LeetCode](https://leetcode.com/problems/frog-jump-ii/) | [LeetCode CH](https://leetcode.cn/problems/frog-jump-ii/) (Medium)

-   Tags: array, binary search, greedy
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

## 2311. Longest Binary Subsequence Less Than or Equal to K

-   [LeetCode](https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/) | [LeetCode CH](https://leetcode.cn/problems/longest-binary-subsequence-less-than-or-equal-to-k/) (Medium)

-   Tags: string, dynamic programming, greedy, memoization
## 3443. Maximum Manhattan Distance After K Changes

-   [LeetCode](https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/) | [LeetCode CH](https://leetcode.cn/problems/maximum-manhattan-distance-after-k-changes/) (Medium)

-   Tags: hash table, math, string, counting
## 3002. Maximum Size of a Set After Removals

-   [LeetCode](https://leetcode.com/problems/maximum-size-of-a-set-after-removals/) | [LeetCode CH](https://leetcode.cn/problems/maximum-size-of-a-set-after-removals/) (Medium)

-   Tags: array, hash table, greedy
## 2412. Minimum Money Required Before Transactions

-   [LeetCode](https://leetcode.com/problems/minimum-money-required-before-transactions/) | [LeetCode CH](https://leetcode.cn/problems/minimum-money-required-before-transactions/) (Hard)

-   Tags: array, greedy, sorting
## 659. Split Array into Consecutive Subsequences

-   [LeetCode](https://leetcode.com/problems/split-array-into-consecutive-subsequences/) | [LeetCode CH](https://leetcode.cn/problems/split-array-into-consecutive-subsequences/) (Medium)

-   Tags: array, hash table, greedy, heap priority queue
## 2732. Find a Good Subset of the Matrix

-   [LeetCode](https://leetcode.com/problems/find-a-good-subset-of-the-matrix/) | [LeetCode CH](https://leetcode.cn/problems/find-a-good-subset-of-the-matrix/) (Hard)

-   Tags: array, hash table, bit manipulation, matrix
## 2790. Maximum Number of Groups With Increasing Length

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-groups-with-increasing-length/) (Hard)

-   Tags: array, math, binary search, greedy, sorting
## 782. Transform to Chessboard

-   [LeetCode](https://leetcode.com/problems/transform-to-chessboard/) | [LeetCode CH](https://leetcode.cn/problems/transform-to-chessboard/) (Hard)

-   Tags: array, math, bit manipulation, matrix
## 420. Strong Password Checker

-   [LeetCode](https://leetcode.com/problems/strong-password-checker/) | [LeetCode CH](https://leetcode.cn/problems/strong-password-checker/) (Hard)

-   Tags: string, greedy, heap priority queue
## 2753. Count Houses in a Circular Street II

-   [LeetCode](https://leetcode.com/problems/count-houses-in-a-circular-street-ii/) | [LeetCode CH](https://leetcode.cn/problems/count-houses-in-a-circular-street-ii/) (Hard)
