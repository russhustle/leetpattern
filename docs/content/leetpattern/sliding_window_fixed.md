---
comments: True
---

# Sliding Window Fixed

## Table of Contents

- [x] [643. Maximum Average Subarray I](https://leetcode.cn/problems/maximum-average-subarray-i/) (Easy)
- [x] [219. Contains Duplicate II](https://leetcode.cn/problems/contains-duplicate-ii/) (Easy)
- [x] [1456. Maximum Number of Vowels in a Substring of Given Length](https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) (Medium)
- [x] [567. Permutation in String](https://leetcode.cn/problems/permutation-in-string/) (Medium)
- [x] [713. Subarray Product Less Than K](https://leetcode.cn/problems/subarray-product-less-than-k/) (Medium)
- [x] [1151. Minimum Swaps to Group All 1's Together](https://leetcode.cn/problems/minimum-swaps-to-group-all-1s-together/) (Medium) 👑
- [x] [209. Minimum Size Subarray Sum](https://leetcode.cn/problems/minimum-size-subarray-sum/) (Medium)
- [x] [76. Minimum Window Substring](https://leetcode.cn/problems/minimum-window-substring/) (Hard)

## 643. Maximum Average Subarray I

-   [LeetCode](https://leetcode.com/problems/maximum-average-subarray-i/) | [LeetCode CH](https://leetcode.cn/problems/maximum-average-subarray-i/) (Easy)

-   Tags: array, sliding window

```python title="643. Maximum Average Subarray I - Python Solution"
from typing import List


# Sliding Window Fixed Size
def findMaxAverage1(nums: List[int], k: int) -> float:
    maxSum = float("-inf")
    cur = 0

    for idx, num in enumerate(nums):
        cur += num

        if idx < k - 1:
            continue

        maxSum = max(maxSum, cur)
        cur -= nums[idx - k + 1]

    return maxSum / k


# Sliding Window Fixed Size
def findMaxAverage2(nums: List[int], k: int) -> float:
    n = len(nums)
    if n == 1:
        return float(nums[0])

    cur = sum(nums[:k])

    maxSum = cur
    for i in range(k, n):
        cur += nums[i] - nums[i - k]
        maxSum = max(maxSum, cur)

    return maxSum / k


nums = [1, 12, -5, -6, 50, 3]
k = 4
print(findMaxAverage1(nums, k))  # 12.75
print(findMaxAverage2(nums, k))  # 12.75

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

## 1456. Maximum Number of Vowels in a Substring of Given Length

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) (Medium)

-   Tags: string, sliding window
- [Templace tutorial by 灵山茶艾府](https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/solutions/2809359/tao-lu-jiao-ni-jie-jue-ding-chang-hua-ch-fzfo)


```python title="1456. Maximum Number of Vowels in a Substring of Given Length - Python Solution"
# Sliding Window Fixed Size
def maxVowels1(s: str, k: int) -> int:
    res, cnt = 0, 0

    for idx, ch in enumerate(s):
        if ch in "aeiou":
            cnt += 1

        if idx < k - 1:
            continue

        res = max(res, cnt)

        if s[idx - k + 1] in "aeiou":
            cnt -= 1

    return res


# Sliding Window Fixed Size
def maxVowels2(s: str, k: int) -> int:
    vowels = set("aeiou")
    n = len(s)
    cnt, res = 0, 0

    for i in range(k):
        if s[i] in vowels:
            cnt += 1

    res = cnt

    for i in range(k, n):
        if s[i] in vowels:
            cnt += 1
        if s[i - k] in vowels:
            cnt -= 1
        res = max(res, cnt)

    return res


# Template: Sliding Window Fixed Size
def templateMaxVowels(s: str, k: int) -> int:
    res, cnt = 0, 0

    for idx, ch in enumerate(s):
        # ADD - add new element to window
        if ch in "aeiou":
            cnt += 1

        # FORM - continue until window is fully formed
        if idx < k - 1:
            continue

        # UPDATE - update result with current window
        res = max(res, cnt)

        # REMOVE - remove element leaving the window
        if s[idx - k + 1] in "aeiou":
            cnt -= 1

    return res


if __name__ == "__main__":
    s = "abciiidef"
    k = 3
    assert maxVowels1(s, k) == 3
    assert maxVowels2(s, k) == 3
    assert templateMaxVowels(s, k) == 3
    print("All tests passed!")

```

## 567. Permutation in String

-   [LeetCode](https://leetcode.com/problems/permutation-in-string/) | [LeetCode CH](https://leetcode.cn/problems/permutation-in-string/) (Medium)

-   Tags: hash table, two pointers, string, sliding window

```python title="567. Permutation in String - Python Solution"
def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    count1 = [0] * 26
    count2 = [0] * 26

    for i in range(len(s1)):
        count1[ord(s1[i]) - ord("a")] += 1
        count2[ord(s2[i]) - ord("a")] += 1

    matches = 0
    for i in range(26):
        if count1[i] == count2[i]:
            matches += 1

    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True

        index = ord(s2[r]) - ord("a")
        count2[index] += 1
        if count1[index] == count2[index]:
            matches += 1
        elif count1[index] + 1 == count2[index]:
            matches -= 1

        index = ord(s2[l]) - ord("a")
        count2[index] -= 1
        if count1[index] == count2[index]:
            matches += 1
        elif count1[index] - 1 == count2[index]:
            matches -= 1

        l += 1

    return matches == 26


s1 = "ab"
s2 = "eidba"
print(checkInclusion(s1, s2))  # True

```

## 713. Subarray Product Less Than K

-   [LeetCode](https://leetcode.com/problems/subarray-product-less-than-k/) | [LeetCode CH](https://leetcode.cn/problems/subarray-product-less-than-k/) (Medium)

-   Tags: array, binary search, sliding window, prefix sum

```python title="713. Subarray Product Less Than K - Python Solution"
from typing import List


# Sliding window - Fixed
def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    if k <= 1:
        return 0

    left = 0
    product = 1
    count = 0

    for right in range(len(nums)):
        product *= nums[right]

        while product >= k:
            product //= nums[left]
            left += 1

        count += right - left + 1

    return count


nums = [10, 5, 2, 6]
k = 100
print(numSubarrayProductLessThanK(nums, k))  # 8

```

## 1151. Minimum Swaps to Group All 1's Together

-   [LeetCode](https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/) | [LeetCode CH](https://leetcode.cn/problems/minimum-swaps-to-group-all-1s-together/) (Medium)

-   Tags: array, sliding window

```python title="1151. Minimum Swaps to Group All 1's Together - Python Solution"
from typing import List


def minSwaps(data: List[int]) -> int:
    n = len(data)
    total = sum(data)

    if total == 0 or total == 1 or total == n:
        return 0

    max_count = 0
    cur = 0
    left = 0

    for right in range(n):
        cur += data[right]

        if right - left + 1 > total:
            cur -= data[left]
            left += 1

        max_count = max(max_count, cur)

    return total - max_count


data = [1, 0, 1, 0, 1]
print(minSwaps(data))  # 1

```

## 209. Minimum Size Subarray Sum

-   [LeetCode](https://leetcode.com/problems/minimum-size-subarray-sum/) | [LeetCode CH](https://leetcode.cn/problems/minimum-size-subarray-sum/) (Medium)

-   Tags: array, binary search, sliding window, prefix sum

```python title="209. Minimum Size Subarray Sum - Python Solution"
import bisect
from typing import List


# Prefix Sum
def minSubArrayLenPS(target: int, nums: List[int]) -> int:
    n = len(nums)
    prefix_sums = [0] * (n + 1)

    for i in range(1, n + 1):
        prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]

    minLen = float("inf")

    for i in range(n + 1):
        new_target = target + prefix_sums[i]
        bound = bisect.bisect_left(prefix_sums, new_target)
        if bound != len(prefix_sums):
            minLen = min(minLen, bound - i)

    return 0 if minLen == float("inf") else minLen


# Sliding Window Variable Size
def minSubArrayLenSW(target: int, nums: List[int]) -> int:
    res, cur = float("inf"), 0
    left = 0

    for right in range(len(nums)):
        cur += nums[right]

        while cur >= target:
            res = min(res, right - left + 1)
            cur -= nums[left]
            left += 1

    return res if res != float("inf") else 0


target = 7
nums = [2, 3, 1, 2, 4, 3]
print(minSubArrayLenPS(target, nums))  # 2
print(minSubArrayLenSW(target, nums))  # 2

```

## 76. Minimum Window Substring

-   [LeetCode](https://leetcode.com/problems/minimum-window-substring/) | [LeetCode CH](https://leetcode.cn/problems/minimum-window-substring/) (Hard)

-   Tags: hash table, string, sliding window

```python title="76. Minimum Window Substring - Python Solution"
from collections import Counter


def minWindow(s: str, t: str) -> str:
    if not t or not s:
        return ""

    counts = Counter(t)
    required = len(counts)

    left, right = 0, 0
    formed = 0
    window_counts = dict()

    result = float("inf"), None, None

    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        if char in counts and window_counts[char] == counts[char]:
            formed += 1

        while left <= right and formed == required:
            char = s[left]
            if right - left + 1 < result[0]:
                result = (right - left + 1, left, right)
            window_counts[char] -= 1
            if char in counts and window_counts[char] < counts[char]:
                formed -= 1
            left += 1

        right += 1

    return "" if result[0] == float("inf") else s[result[1] : result[2] + 1]


s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))  # BANC

```
