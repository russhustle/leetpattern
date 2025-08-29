---
comments: True
---

# Single Sequence Pairing

## Table of Contents

- [ ] [2144. Minimum Cost of Buying Candies With Discount](https://leetcode.cn/problems/minimum-cost-of-buying-candies-with-discount/) (Easy)
- [ ] [561. Array Partition](https://leetcode.cn/problems/array-partition/) (Easy)
- [ ] [1877. Minimize Maximum Pair Sum in Array](https://leetcode.cn/problems/minimize-maximum-pair-sum-in-array/) (Medium)
- [x] [881. Boats to Save People](https://leetcode.cn/problems/boats-to-save-people/) (Medium)
- [ ] [2592. Maximize Greatness of an Array](https://leetcode.cn/problems/maximize-greatness-of-an-array/) (Medium)
- [x] [2576. Find the Maximum Number of Marked Indices](https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices/) (Medium)

## 2144. Minimum Cost of Buying Candies With Discount

-   [LeetCode](https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/) | [LeetCode CH](https://leetcode.cn/problems/minimum-cost-of-buying-candies-with-discount/) (Easy)

-   Tags: array, greedy, sorting
## 561. Array Partition

-   [LeetCode](https://leetcode.com/problems/array-partition/) | [LeetCode CH](https://leetcode.cn/problems/array-partition/) (Easy)

-   Tags: array, greedy, sorting, counting sort
## 1877. Minimize Maximum Pair Sum in Array

-   [LeetCode](https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/) | [LeetCode CH](https://leetcode.cn/problems/minimize-maximum-pair-sum-in-array/) (Medium)

-   Tags: array, two pointers, greedy, sorting
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

## 2592. Maximize Greatness of an Array

-   [LeetCode](https://leetcode.com/problems/maximize-greatness-of-an-array/) | [LeetCode CH](https://leetcode.cn/problems/maximize-greatness-of-an-array/) (Medium)

-   Tags: array, two pointers, greedy, sorting
## 2576. Find the Maximum Number of Marked Indices

-   [LeetCode](https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/) | [LeetCode CH](https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices/) (Medium)

-   Tags: array, two pointers, binary search, greedy, sorting
```python title="2576. Find the Maximum Number of Marked Indices - Python Solution"
from typing import List


# Fast Slow Pointers
def maxNumOfMarkedIndices(nums: List[int]) -> int:
    nums.sort()
    n = len(nums)
    slow, fast = 0, n // 2
    count = 0

    while slow < n // 2 and fast < n:
        if nums[fast] >= 2 * nums[slow]:
            count += 2
            slow += 1
        fast += 1

    return count


nums = [3, 5, 2, 4]
print(maxNumOfMarkedIndices(nums))  # 2

```

