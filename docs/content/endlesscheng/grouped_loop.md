---
comments: True
---

# Grouped Loop

## Table of Contents

- [ ] [1446. Consecutive Characters](https://leetcode.cn/problems/consecutive-characters/) (Easy)
- [ ] [1869. Longer Contiguous Segments of Ones than Zeros](https://leetcode.cn/problems/longer-contiguous-segments-of-ones-than-zeros/) (Easy)
- [ ] [2414. Length of the Longest Alphabetical Continuous Substring](https://leetcode.cn/problems/length-of-the-longest-alphabetical-continuous-substring/) (Medium)
- [ ] [3456. Find Special Substring of Length K](https://leetcode.cn/problems/find-special-substring-of-length-k/) (Easy)
- [ ] [1957. Delete Characters to Make Fancy String](https://leetcode.cn/problems/delete-characters-to-make-fancy-string/) (Easy)
- [x] [674. Longest Continuous Increasing Subsequence](https://leetcode.cn/problems/longest-continuous-increasing-subsequence/) (Easy)
- [x] [978. Longest Turbulent Subarray](https://leetcode.cn/problems/longest-turbulent-subarray/) (Medium)
- [ ] [2110. Number of Smooth Descent Periods of a Stock](https://leetcode.cn/problems/number-of-smooth-descent-periods-of-a-stock/) (Medium)
- [x] [228. Summary Ranges](https://leetcode.cn/problems/summary-ranges/) (Easy)
- [ ] [2760. Longest Even Odd Subarray With Threshold](https://leetcode.cn/problems/longest-even-odd-subarray-with-threshold/) (Easy)
- [ ] [1887. Reduction Operations to Make the Array Elements Equal](https://leetcode.cn/problems/reduction-operations-to-make-the-array-elements-equal/) (Medium)
- [x] [845. Longest Mountain in Array](https://leetcode.cn/problems/longest-mountain-in-array/) (Medium)
- [ ] [2038. Remove Colored Pieces if Both Neighbors are the Same Color](https://leetcode.cn/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/) (Medium)
- [ ] [1759. Count Number of Homogenous Substrings](https://leetcode.cn/problems/count-number-of-homogenous-substrings/) (Medium)
- [ ] [3011. Find if Array Can Be Sorted](https://leetcode.cn/problems/find-if-array-can-be-sorted/) (Medium)
- [ ] [1578. Minimum Time to Make Rope Colorful](https://leetcode.cn/problems/minimum-time-to-make-rope-colorful/) (Medium)
- [ ] [1839. Longest Substring Of All Vowels in Order](https://leetcode.cn/problems/longest-substring-of-all-vowels-in-order/) (Medium)
- [ ] [2765. Longest Alternating Subarray](https://leetcode.cn/problems/longest-alternating-subarray/) (Easy)
- [ ] [3255. Find the Power of K-Size Subarrays II](https://leetcode.cn/problems/find-the-power-of-k-size-subarrays-ii/) (Medium)
- [ ] [3350. Adjacent Increasing Subarrays Detection II](https://leetcode.cn/problems/adjacent-increasing-subarrays-detection-ii/) (Medium)
- [ ] [3105. Longest Strictly Increasing or Strictly Decreasing Subarray](https://leetcode.cn/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/) (Easy)
- [ ] [467. Unique Substrings in Wraparound String](https://leetcode.cn/problems/unique-substrings-in-wraparound-string/) (Medium)
- [ ] [2948. Make Lexicographically Smallest Array by Swapping Elements](https://leetcode.cn/problems/make-lexicographically-smallest-array-by-swapping-elements/) (Medium)
- [ ] [2593. Find Score of an Array After Marking All Elements](https://leetcode.cn/problems/find-score-of-an-array-after-marking-all-elements/) (Medium)
- [ ] [2393. Count Strictly Increasing Subarrays](https://leetcode.cn/problems/count-strictly-increasing-subarrays/) (Medium) 👑
- [ ] [2436. Minimum Split Into Subarrays With GCD Greater Than One](https://leetcode.cn/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/) (Medium) 👑
- [ ] [2495. Number of Subarrays Having Even Product](https://leetcode.cn/problems/number-of-subarrays-having-even-product/) (Medium) 👑
- [ ] [3063. Linked List Frequency](https://leetcode.cn/problems/linked-list-frequency/) (Easy) 👑

## 1446. Consecutive Characters

-   [LeetCode](https://leetcode.com/problems/consecutive-characters/) | [LeetCode CH](https://leetcode.cn/problems/consecutive-characters/) (Easy)

-   Tags: string
## 1869. Longer Contiguous Segments of Ones than Zeros

-   [LeetCode](https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/) | [LeetCode CH](https://leetcode.cn/problems/longer-contiguous-segments-of-ones-than-zeros/) (Easy)

-   Tags: string
## 2414. Length of the Longest Alphabetical Continuous Substring

-   [LeetCode](https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/) | [LeetCode CH](https://leetcode.cn/problems/length-of-the-longest-alphabetical-continuous-substring/) (Medium)

-   Tags: string
## 3456. Find Special Substring of Length K

-   [LeetCode](https://leetcode.com/problems/find-special-substring-of-length-k/) | [LeetCode CH](https://leetcode.cn/problems/find-special-substring-of-length-k/) (Easy)

-   Tags: string
## 1957. Delete Characters to Make Fancy String

-   [LeetCode](https://leetcode.com/problems/delete-characters-to-make-fancy-string/) | [LeetCode CH](https://leetcode.cn/problems/delete-characters-to-make-fancy-string/) (Easy)

-   Tags: string
## 674. Longest Continuous Increasing Subsequence

-   [LeetCode](https://leetcode.com/problems/longest-continuous-increasing-subsequence/) | [LeetCode CH](https://leetcode.cn/problems/longest-continuous-increasing-subsequence/) (Easy)

-   Tags: array

```python title="674. Longest Continuous Increasing Subsequence - Python Solution"
from typing import List


def findLengthOfLCIS(nums: List[int]) -> int:
    n = len(nums)
    if n <= 1:
        return n

    dp = [1 for _ in range(n)]

    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            dp[i] = dp[i - 1] + 1

    return max(dp)


print(findLengthOfLCIS([1, 3, 5, 4, 7]))  # 3

```

## 978. Longest Turbulent Subarray

-   [LeetCode](https://leetcode.com/problems/longest-turbulent-subarray/) | [LeetCode CH](https://leetcode.cn/problems/longest-turbulent-subarray/) (Medium)

-   Tags: array, dynamic programming, sliding window

```python title="978. Longest Turbulent Subarray - Python Solution"
from typing import List


# DP - Kadane
def maxTurbulenceSize(arr: List[int]) -> int:
    n = len(arr)
    up = [1 for _ in range(n)]
    down = [1 for _ in range(n)]
    maxLen = 1

    for i in range(1, n):
        if arr[i - 1] < arr[i]:
            up[i] = down[i - 1] + 1
            down[i] = 1
        elif arr[i - 1] > arr[i]:
            down[i] = up[i - 1] + 1
            up[i] = 1
        else:
            up[i] = 1
            down[i] = 1

        maxLen = max(maxLen, up[i], down[i])

    return maxLen


arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
print(maxTurbulenceSize(arr))  # 5

```

## 2110. Number of Smooth Descent Periods of a Stock

-   [LeetCode](https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/) | [LeetCode CH](https://leetcode.cn/problems/number-of-smooth-descent-periods-of-a-stock/) (Medium)

-   Tags: array, math, dynamic programming
## 228. Summary Ranges

-   [LeetCode](https://leetcode.com/problems/summary-ranges/) | [LeetCode CH](https://leetcode.cn/problems/summary-ranges/) (Easy)

-   Tags: array

```python title="228. Summary Ranges - Python Solution"
from typing import List


# Variable Sliding Window
def summaryRanges(nums: List[int]) -> List[str]:
    left, right = 0, 0
    n = len(nums)
    res = []

    while left < n:
        while right + 1 < n and nums[right] + 1 == nums[right + 1]:
            right += 1

        if left == right:
            res.append(f"{nums[left]}")
        else:
            res.append(f"{nums[left]}->{nums[right]}")

        right += 1
        left = right

    return res


if __name__ == "__main__":
    print(summaryRanges([0, 1, 2, 4, 5, 7]))
    # ["0->2", "4->5", "7"]
    print(summaryRanges([0, 2, 3, 4, 6, 8, 9]))
    # ["0", "2->4", "6", "8->9"]

```

## 2760. Longest Even Odd Subarray With Threshold

-   [LeetCode](https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/) | [LeetCode CH](https://leetcode.cn/problems/longest-even-odd-subarray-with-threshold/) (Easy)

-   Tags: array, sliding window
## 1887. Reduction Operations to Make the Array Elements Equal

-   [LeetCode](https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/) | [LeetCode CH](https://leetcode.cn/problems/reduction-operations-to-make-the-array-elements-equal/) (Medium)

-   Tags: array, sorting
## 845. Longest Mountain in Array

-   [LeetCode](https://leetcode.com/problems/longest-mountain-in-array/) | [LeetCode CH](https://leetcode.cn/problems/longest-mountain-in-array/) (Medium)

-   Tags: array, two pointers, dynamic programming, enumeration

```python title="845. Longest Mountain in Array - Python Solution"
from typing import List


# Left Right Pointers
def longestMountain(arr: List[int]) -> int:
    n = len(arr)
    res = 0
    left = 0

    while left < n:
        right = left

        if right < n - 1 and arr[right] < arr[right + 1]:
            while right < n - 1 and arr[right] < arr[right + 1]:
                right += 1

            if right < n - 1 and arr[right] > arr[right + 1]:
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1
                res = max(res, right - left + 1)

        left = max(right, left + 1)

    return res


arr = [2, 1, 4, 7, 3, 2, 5]
print(longestMountain(arr))  # 5

```

## 2038. Remove Colored Pieces if Both Neighbors are the Same Color

-   [LeetCode](https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/) | [LeetCode CH](https://leetcode.cn/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/) (Medium)

-   Tags: math, string, greedy, game theory
## 1759. Count Number of Homogenous Substrings

-   [LeetCode](https://leetcode.com/problems/count-number-of-homogenous-substrings/) | [LeetCode CH](https://leetcode.cn/problems/count-number-of-homogenous-substrings/) (Medium)

-   Tags: math, string
## 3011. Find if Array Can Be Sorted

-   [LeetCode](https://leetcode.com/problems/find-if-array-can-be-sorted/) | [LeetCode CH](https://leetcode.cn/problems/find-if-array-can-be-sorted/) (Medium)

-   Tags: array, bit manipulation, sorting
## 1578. Minimum Time to Make Rope Colorful

-   [LeetCode](https://leetcode.com/problems/minimum-time-to-make-rope-colorful/) | [LeetCode CH](https://leetcode.cn/problems/minimum-time-to-make-rope-colorful/) (Medium)

-   Tags: array, string, dynamic programming, greedy
## 1839. Longest Substring Of All Vowels in Order

-   [LeetCode](https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/) | [LeetCode CH](https://leetcode.cn/problems/longest-substring-of-all-vowels-in-order/) (Medium)

-   Tags: string, sliding window
## 2765. Longest Alternating Subarray

-   [LeetCode](https://leetcode.com/problems/longest-alternating-subarray/) | [LeetCode CH](https://leetcode.cn/problems/longest-alternating-subarray/) (Easy)

-   Tags: array, enumeration
## 3255. Find the Power of K-Size Subarrays II

-   [LeetCode](https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/) | [LeetCode CH](https://leetcode.cn/problems/find-the-power-of-k-size-subarrays-ii/) (Medium)

-   Tags: array, sliding window
## 3350. Adjacent Increasing Subarrays Detection II

-   [LeetCode](https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/) | [LeetCode CH](https://leetcode.cn/problems/adjacent-increasing-subarrays-detection-ii/) (Medium)

-   Tags: array, binary search
## 3105. Longest Strictly Increasing or Strictly Decreasing Subarray

-   [LeetCode](https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/) | [LeetCode CH](https://leetcode.cn/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/) (Easy)

-   Tags: array
## 467. Unique Substrings in Wraparound String

-   [LeetCode](https://leetcode.com/problems/unique-substrings-in-wraparound-string/) | [LeetCode CH](https://leetcode.cn/problems/unique-substrings-in-wraparound-string/) (Medium)

-   Tags: string, dynamic programming
## 2948. Make Lexicographically Smallest Array by Swapping Elements

-   [LeetCode](https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/) | [LeetCode CH](https://leetcode.cn/problems/make-lexicographically-smallest-array-by-swapping-elements/) (Medium)

-   Tags: array, union find, sorting
## 2593. Find Score of an Array After Marking All Elements

-   [LeetCode](https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/) | [LeetCode CH](https://leetcode.cn/problems/find-score-of-an-array-after-marking-all-elements/) (Medium)

-   Tags: array, hash table, sorting, heap priority queue, simulation
## 2393. Count Strictly Increasing Subarrays

-   [LeetCode](https://leetcode.com/problems/count-strictly-increasing-subarrays/) | [LeetCode CH](https://leetcode.cn/problems/count-strictly-increasing-subarrays/) (Medium)

-   Tags: array, math, dynamic programming
## 2436. Minimum Split Into Subarrays With GCD Greater Than One

-   [LeetCode](https://leetcode.com/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/) | [LeetCode CH](https://leetcode.cn/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/) (Medium)

-   Tags: array, math, dynamic programming, greedy, number theory
## 2495. Number of Subarrays Having Even Product

-   [LeetCode](https://leetcode.com/problems/number-of-subarrays-having-even-product/) | [LeetCode CH](https://leetcode.cn/problems/number-of-subarrays-having-even-product/) (Medium)

-   Tags: array, math, dynamic programming
## 3063. Linked List Frequency

-   [LeetCode](https://leetcode.com/problems/linked-list-frequency/) | [LeetCode CH](https://leetcode.cn/problems/linked-list-frequency/) (Easy)

-   Tags: hash table, linked list, counting
