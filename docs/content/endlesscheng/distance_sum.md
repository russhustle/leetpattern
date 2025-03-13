---
comments: True
---

# Distance Sum

- [x] [1685. Sum of Absolute Differences in a Sorted Array](https://leetcode.cn/problems/sum-of-absolute-differences-in-a-sorted-array/) (Medium)
- [ ] [2615. Sum of Distances](https://leetcode.cn/problems/sum-of-distances/) (Medium)
- [ ] [2602. Minimum Operations to Make All Array Elements Equal](https://leetcode.cn/problems/minimum-operations-to-make-all-array-elements-equal/) (Medium)
- [ ] [2968. Apply Operations to Maximize Frequency Score](https://leetcode.cn/problems/apply-operations-to-maximize-frequency-score/) (Hard)
- [ ] [1703. Minimum Adjacent Swaps for K Consecutive Ones](https://leetcode.cn/problems/minimum-adjacent-swaps-for-k-consecutive-ones/) (Hard)
- [ ] [3086. Minimum Moves to Pick K Ones](https://leetcode.cn/problems/minimum-moves-to-pick-k-ones/) (Hard)
- [ ] [3422. Minimum Operations to Make Subarray Elements Equal](https://leetcode.cn/problems/minimum-operations-to-make-subarray-elements-equal/) (Medium) 👑

## 1685. Sum of Absolute Differences in a Sorted Array

-   [LeetCode](https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-absolute-differences-in-a-sorted-array/) (Medium)

-   Tags: array, math, prefix sum

```python title="1685. Sum of Absolute Differences in a Sorted Array - Python Solution"
from typing import List


# Prefix Sum
def getSumAbsoluteDifferences(nums: List[int]) -> List[int]:
    n = len(nums)
    totalSum = sum(nums)
    prefixSum = 0
    res = [0 for _ in range(n)]

    for i in range(n):
        leftSum = prefixSum
        rightSum = totalSum - prefixSum - nums[i]

        leftCount = i
        rightCount = n - i - 1

        res[i] = (nums[i] * leftCount - leftSum) + (rightSum - nums[i] * rightCount)
        prefixSum += nums[i]

    return res


nums = [1, 4, 6, 8, 10]
print(getSumAbsoluteDifferences(nums))  # [24, 15, 13, 15, 21]

```

## 2615. Sum of Distances

-   [LeetCode](https://leetcode.com/problems/sum-of-distances/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-distances/) (Medium)

-   Tags: array, hash table, prefix sum

## 2602. Minimum Operations to Make All Array Elements Equal

-   [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/) | [LeetCode CH](https://leetcode.cn/problems/minimum-operations-to-make-all-array-elements-equal/) (Medium)

-   Tags: array, binary search, sorting, prefix sum

## 2968. Apply Operations to Maximize Frequency Score

-   [LeetCode](https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/) | [LeetCode CH](https://leetcode.cn/problems/apply-operations-to-maximize-frequency-score/) (Hard)

-   Tags: array, binary search, sliding window, sorting, prefix sum

## 1703. Minimum Adjacent Swaps for K Consecutive Ones

-   [LeetCode](https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/) | [LeetCode CH](https://leetcode.cn/problems/minimum-adjacent-swaps-for-k-consecutive-ones/) (Hard)

-   Tags: array, greedy, sliding window, prefix sum

## 3086. Minimum Moves to Pick K Ones

-   [LeetCode](https://leetcode.com/problems/minimum-moves-to-pick-k-ones/) | [LeetCode CH](https://leetcode.cn/problems/minimum-moves-to-pick-k-ones/) (Hard)

-   Tags: array, greedy, sliding window, prefix sum

## 3422. Minimum Operations to Make Subarray Elements Equal

-   [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-subarray-elements-equal/) | [LeetCode CH](https://leetcode.cn/problems/minimum-operations-to-make-subarray-elements-equal/) (Medium)

-   Tags: array, hash table, math, sliding window, heap priority queue
