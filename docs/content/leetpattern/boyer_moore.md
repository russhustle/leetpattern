---
comments: True
---

# Boyer Moore

- [x] [169. Majority Element](https://leetcode.cn/problems/majority-element/) (Easy)
- [x] [229. Majority Element II](https://leetcode.cn/problems/majority-element-ii/) (Medium)
- [x] [287. Find the Duplicate Number](https://leetcode.cn/problems/find-the-duplicate-number/) (Medium)
- [ ] [1150. Check If a Number Is Majority Element in a Sorted Array](https://leetcode.cn/problems/check-if-a-number-is-majority-element-in-a-sorted-array/) (Easy) 👑
- [ ] [1157. Online Majority Element In Subarray](https://leetcode.cn/problems/online-majority-element-in-subarray/) (Hard)
- [ ] [495. Teemo Attacking](https://leetcode.cn/problems/teemo-attacking/) (Easy)

## 169. Majority Element

-   [LeetCode](https://leetcode.com/problems/majority-element/) | [LeetCode CH](https://leetcode.cn/problems/majority-element/) (Easy)

-   Tags: array, hash table, divide and conquer, sorting, counting
-   Return the majority element in an array. The majority element is the element that appears more than `n // 2` times.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7pnhv842keE?si=fBYlNfKzdkiLgkF1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

| `num` | `count` | `res` |
| ----- | ------- | ----- |
| 2     | 1       | 2     |
| 2     | 2       | 2     |
| 1     | 1       | 2     |
| 1     | 0       | 2     |
| 1     | 1       | 1     |
| 2     | 0       | 1     |
| 2     | 1       | 2     |

```python title="169. Majority Element - Python Solution"
from collections import defaultdict
from typing import List


# Hash Map
def majorityElementHashMap(nums: List[int]) -> int:
    n = len(nums)
    freq = defaultdict(int)

    for num in nums:
        freq[num] += 1
        if freq[num] > n // 2:
            return num


# Array - Boyer-Moore Voting Algorithm
def majorityElementArray(nums: List[int]) -> int:
    res = None
    count = 0

    for num in nums:
        if count == 0:
            res = num
        count += 1 if num == res else -1

    return res


# | Algorithm | Time Complexity | Space Complexity |
# |-----------|-----------------|------------------|
# | HashMap   | O(N)            | O(N)             |
# | Array     | O(N)            | O(1)             |
# |-----------|-----------------|------------------|


nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElementArray(nums))  # 2
print(majorityElementHashMap(nums))  # 2

```

## 229. Majority Element II

-   [LeetCode](https://leetcode.com/problems/majority-element-ii/) | [LeetCode CH](https://leetcode.cn/problems/majority-element-ii/) (Medium)

-   Tags: array, hash table, sorting, counting

```python title="229. Majority Element II - Python Solution"
from collections import Counter
from typing import List


# Hash Map
def majorityElementHash(nums: List[int]) -> List[int]:
    counts = Counter(nums)
    target = len(nums) // 3
    res = []

    for num in nums:
        if counts[num] > target and num not in res:
            res.append(num)

    return res


# Boyer-Moore
def majorityElementMoore(nums: List[int]) -> List[int]:
    if not nums:
        return []

    cdt1, cnt1 = None, 0
    cdt2, cnt2 = None, 0

    for num in nums:
        if num == cdt1:
            cnt1 += 1
        elif num == cdt2:
            cnt2 += 1
        elif cnt1 == 0:
            cdt1, cnt1 = num, 1
        elif cnt2 == 0:
            cdt2, cnt2 = num, 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    return [n for n in (cdt1, cdt2) if nums.count(n) > len(nums) // 3]


nums = [3, 2, 3]
print(majorityElementHash(nums))  # [3]
print(majorityElementMoore(nums))  # [3]

```

## 287. Find the Duplicate Number

-   [LeetCode](https://leetcode.com/problems/find-the-duplicate-number/) | [LeetCode CH](https://leetcode.cn/problems/find-the-duplicate-number/) (Medium)

-   Tags: array, two pointers, binary search, bit manipulation
-   Find the duplicate number in an array containing `n + 1` integers where each integer is between `1` and `n` inclusive.

```python title="287. Find the Duplicate Number - Python Solution"
from typing import List


# Fast Slow Pointer
def findDuplicate(nums: List[int]) -> int:
    fast, slow = nums[0], nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums))  # 2

```

## 1150. Check If a Number Is Majority Element in a Sorted Array

-   [LeetCode](https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/) | [LeetCode CH](https://leetcode.cn/problems/check-if-a-number-is-majority-element-in-a-sorted-array/) (Easy)

-   Tags: array, binary search

## 1157. Online Majority Element In Subarray

-   [LeetCode](https://leetcode.com/problems/online-majority-element-in-subarray/) | [LeetCode CH](https://leetcode.cn/problems/online-majority-element-in-subarray/) (Hard)

-   Tags: array, binary search, design, binary indexed tree, segment tree

## 495. Teemo Attacking

-   [LeetCode](https://leetcode.com/problems/teemo-attacking/) | [LeetCode CH](https://leetcode.cn/problems/teemo-attacking/) (Easy)

-   Tags: array, simulation
