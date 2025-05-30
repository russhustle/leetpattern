---
comments: True
---

# Sliding Window Fixed Size Basics

## Table of Contents

- [x] [1456. Maximum Number of Vowels in a Substring of Given Length](https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) (Medium)
- [x] [643. Maximum Average Subarray I](https://leetcode.cn/problems/maximum-average-subarray-i/) (Easy)
- [x] [1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](https://leetcode.cn/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/) (Medium)
- [x] [2090. K Radius Subarray Averages](https://leetcode.cn/problems/k-radius-subarray-averages/) (Medium)
- [x] [2379. Minimum Recolors to Get K Consecutive Black Blocks](https://leetcode.cn/problems/minimum-recolors-to-get-k-consecutive-black-blocks/) (Easy)
- [x] [2841. Maximum Sum of Almost Unique Subarray](https://leetcode.cn/problems/maximum-sum-of-almost-unique-subarray/) (Medium)
- [x] [2461. Maximum Sum of Distinct Subarrays With Length K](https://leetcode.cn/problems/maximum-sum-of-distinct-subarrays-with-length-k/) (Medium)
- [x] [1423. Maximum Points You Can Obtain from Cards](https://leetcode.cn/problems/maximum-points-you-can-obtain-from-cards/) (Medium)
- [x] [1052. Grumpy Bookstore Owner](https://leetcode.cn/problems/grumpy-bookstore-owner/) (Medium)
- [x] [1652. Defuse the Bomb](https://leetcode.cn/problems/defuse-the-bomb/) (Easy)
- [x] [1176. Diet Plan Performance](https://leetcode.cn/problems/diet-plan-performance/) (Easy) 👑
- [x] [1100. Find K-Length Substrings With No Repeated Characters](https://leetcode.cn/problems/find-k-length-substrings-with-no-repeated-characters/) (Medium) 👑
- [x] [1852. Distinct Numbers in Each Subarray](https://leetcode.cn/problems/distinct-numbers-in-each-subarray/) (Medium) 👑
- [x] [1151. Minimum Swaps to Group All 1's Together](https://leetcode.cn/problems/minimum-swaps-to-group-all-1s-together/) (Medium) 👑
- [x] [2107. Number of Unique Flavors After Sharing K Candies](https://leetcode.cn/problems/number-of-unique-flavors-after-sharing-k-candies/) (Medium) 👑

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

## 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

-   [LeetCode](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/) | [LeetCode CH](https://leetcode.cn/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/) (Medium)

-   Tags: array, sliding window

```python title="1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold - Python Solution"
from typing import List


# Sliding Window Fixed Size
def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
    target = k * threshold
    res, cur = 0, 0

    for idx, num in enumerate(arr):
        cur += num

        if idx < k - 1:
            continue

        if cur >= target:
            res += 1

        cur -= arr[idx - k + 1]

    return res


arr = [2, 2, 2, 2, 5, 5, 5, 8]
k = 3
threshold = 4
print(numOfSubarrays(arr, k, threshold))  # 3

```

## 2090. K Radius Subarray Averages

-   [LeetCode](https://leetcode.com/problems/k-radius-subarray-averages/) | [LeetCode CH](https://leetcode.cn/problems/k-radius-subarray-averages/) (Medium)

-   Tags: array, sliding window

```python title="2090. K Radius Subarray Averages - Python Solution"
from typing import List


# Sliding Window Fixed Size
def getAverages(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    res = [-1 for _ in range(n)]
    size = 2 * k + 1

    if size > n:
        return res
    if k == 0:
        return nums

    cur = 0
    for idx, num in enumerate(nums):
        cur += num

        if idx < 2 * k:
            continue

        res[idx - k] = cur // size
        cur -= nums[idx - 2 * k]

    return res


nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
k = 3
print(getAverages(nums, k))
# [-1, -1, -1, 5, 4, 4, -1, -1, -1]

```

## 2379. Minimum Recolors to Get K Consecutive Black Blocks

-   [LeetCode](https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/) | [LeetCode CH](https://leetcode.cn/problems/minimum-recolors-to-get-k-consecutive-black-blocks/) (Easy)

-   Tags: string, sliding window

```python title="2379. Minimum Recolors to Get K Consecutive Black Blocks - Python Solution"
# Sliding Window Fixed Size
def minimumRecolors(blocks: str, k: int) -> int:
    cnt, res = 0, float("inf")

    for idx, block in enumerate(blocks):
        if block == "W":
            cnt += 1

        if idx < k - 1:
            continue

        res = min(res, cnt)

        if blocks[idx - k + 1] == "W":
            cnt -= 1

    return res


blocks = "WBBWWBBWBW"
k = 7
print(minimumRecolors(blocks, k))  # 3

```

## 2841. Maximum Sum of Almost Unique Subarray

-   [LeetCode](https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/) | [LeetCode CH](https://leetcode.cn/problems/maximum-sum-of-almost-unique-subarray/) (Medium)

-   Tags: array, hash table, sliding window

```python title="2841. Maximum Sum of Almost Unique Subarray - Python Solution"
from collections import defaultdict
from typing import List


# Sliding Window Fixed Size
def maxSum(nums: List[int], m: int, k: int) -> int:
    counts = defaultdict(int)
    cur, res = 0, 0

    for idx, num in enumerate(nums):
        counts[num] += 1
        cur += num

        if idx < k - 1:
            continue

        if len(counts) >= m:
            res = max(res, cur)

        first = idx - k + 1
        cur -= nums[first]
        counts[nums[first]] -= 1
        if counts[nums[first]] == 0:
            del counts[nums[first]]

    return res


nums = [2, 6, 7, 3, 1, 7]
m = 3
k = 4
print(maxSum(nums, m, k))  # 18

```

## 2461. Maximum Sum of Distinct Subarrays With Length K

-   [LeetCode](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/) | [LeetCode CH](https://leetcode.cn/problems/maximum-sum-of-distinct-subarrays-with-length-k/) (Medium)

-   Tags: array, hash table, sliding window

```python title="2461. Maximum Sum of Distinct Subarrays With Length K - Python Solution"
from collections import defaultdict
from typing import List


# Sliding Window Fixed Size
def maximumSubarraySum(nums: List[int], k: int) -> int:
    counts = defaultdict(int)
    res = 0
    cur = 0

    for idx, num in enumerate(nums):
        counts[num] += 1
        cur += num

        if idx < k - 1:
            continue

        if len(counts) == k:
            res = max(res, cur)

        first = idx - k + 1
        cur -= nums[first]
        counts[nums[first]] -= 1
        if counts[nums[first]] == 0:
            del counts[nums[first]]

    return res


nums = [1, 5, 4, 2, 9, 9, 9]
k = 3
print(maximumSubarraySum(nums, k))  # 15

```

## 1423. Maximum Points You Can Obtain from Cards

-   [LeetCode](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/) | [LeetCode CH](https://leetcode.cn/problems/maximum-points-you-can-obtain-from-cards/) (Medium)

-   Tags: array, sliding window, prefix sum

```python title="1423. Maximum Points You Can Obtain from Cards - Python Solution"
from typing import List


# Sliding Window Fixed Size
def maxScore(cardPoints: List[int], k: int) -> int:
    n = len(cardPoints)
    j = n - k
    total = sum(cardPoints)

    if j == 0:
        return total

    curSum, minSum = 0, float("inf")

    for idx, point in enumerate(cardPoints):
        curSum += point

        if idx < j - 1:
            continue

        minSum = min(minSum, curSum)
        curSum -= cardPoints[idx - j + 1]

    return total - minSum


cardPoints = [1, 2, 3, 4, 5, 6, 1]
k = 3
print(maxScore(cardPoints, k))  # 12

```

## 1052. Grumpy Bookstore Owner

-   [LeetCode](https://leetcode.com/problems/grumpy-bookstore-owner/) | [LeetCode CH](https://leetcode.cn/problems/grumpy-bookstore-owner/) (Medium)

-   Tags: array, sliding window
-   Hint: Maximize the number of _unsatisfied customers_ in the fixed window of `minutes`.


```python title="1052. Grumpy Bookstore Owner - Python Solution"
from typing import List


# Sliding Window Fixed Size
def maxSatisfied(customers: List[int], grumpy: List[int], minutes: int) -> int:
    n = len(customers)
    k = minutes
    if k >= n:
        return sum(customers)

    total_satisfied = sum(customers[i] for i in range(n) if not grumpy[i])

    cur, maxGrumpy = 0, 0

    for idx, customer in enumerate(customers):
        cur += customer if grumpy[idx] else 0

        if idx < k - 1:
            continue

        maxGrumpy = max(maxGrumpy, cur)

        cur -= customers[idx - k + 1] if grumpy[idx - k + 1] else 0

    return total_satisfied + maxGrumpy


customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
minutes = 3
print(maxSatisfied(customers, grumpy, minutes))  # 16

```

## 1652. Defuse the Bomb

-   [LeetCode](https://leetcode.com/problems/defuse-the-bomb/) | [LeetCode CH](https://leetcode.cn/problems/defuse-the-bomb/) (Easy)

-   Tags: array, sliding window
-   How to deal with the _circular array_?
    -   Trick: mod (index % length)


```python title="1652. Defuse the Bomb - Python Solution"
from typing import List


# Sliding Window Fixed Size
def decrypt(code: List[int], k: int) -> List[int]:
    n = len(code)
    res = [0 for _ in range(n)]
    if k == 0:
        return res

    left, right = (1, k) if k > 0 else (n + k, n - 1)

    curSum = 0
    for i in range(left, right + 1):
        curSum += code[i % n]

    for i in range(n):
        res[i] = curSum

        curSum -= code[left % n]
        left += 1
        right += 1
        curSum += code[right % n]

    return res


code = [2, 4, 9, 3]
k = -2
print(decrypt(code, k))  # [12, 5, 6, 13]

```

## 1176. Diet Plan Performance

-   [LeetCode](https://leetcode.com/problems/diet-plan-performance/) | [LeetCode CH](https://leetcode.cn/problems/diet-plan-performance/) (Easy)

-   Tags: array, sliding window

```python title="1176. Diet Plan Performance - Python Solution"
from typing import List


# Sliding Window Fixed Size
def dietPlanPerformance(
    calories: List[int], k: int, lower: int, upper: int
) -> int:
    res, T = 0, 0

    for i in range(len(calories)):
        T += calories[i]

        if i < k - 1:
            continue

        if T < lower:
            res -= 1
        elif T > upper:
            res += 1

        T -= calories[i - k + 1]

    return res


if __name__ == "__main__":
    calories = [1, 2, 3, 4, 5]
    k = 1
    lower = 3
    upper = 3

    assert dietPlanPerformance(calories, k, lower, upper) == 0

```

## 1100. Find K-Length Substrings With No Repeated Characters

-   [LeetCode](https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/) | [LeetCode CH](https://leetcode.cn/problems/find-k-length-substrings-with-no-repeated-characters/) (Medium)

-   Tags: hash table, string, sliding window

```python title="1100. Find K-Length Substrings With No Repeated Characters - Python Solution"
from collections import defaultdict


# Sliding Window Fixed Size
def numKLenSubstrNoRepeats(s: str, k: int) -> int:
    n = len(s)
    if k > n:
        return 0

    counts = defaultdict(int)
    res = 0

    for i, ch in enumerate(s):
        # add to the window
        counts[ch] += 1

        # form a valid window
        if i < k - 1:
            continue

        # update
        res += 1 if len(counts) == k else 0

        # remove from the window
        first = i - k + 1
        counts[s[first]] -= 1
        if counts[s[first]] == 0:
            del counts[s[first]]

    return res


if __name__ == "__main__":
    s = "havefunonleetcode"
    k = 5

    assert numKLenSubstrNoRepeats(s, k) == 6

```

## 1852. Distinct Numbers in Each Subarray

-   [LeetCode](https://leetcode.com/problems/distinct-numbers-in-each-subarray/) | [LeetCode CH](https://leetcode.cn/problems/distinct-numbers-in-each-subarray/) (Medium)

-   Tags: array, hash table, sliding window

```python title="1852. Distinct Numbers in Each Subarray - Python Solution"
from collections import defaultdict
from typing import List


# Sliding Window Fixed Size
def distinctNumbers(nums: List[int], k: int) -> List[int]:
    res = []
    counts = defaultdict(int)

    for right in range(len(nums)):
        counts[nums[right]] += 1  # add

        if right < k - 1:  # form
            continue

        res.append(len(counts))  # update

        left = right - k + 1  # remove
        counts[nums[left]] -= 1
        if counts[nums[left]] == 0:
            del counts[nums[left]]

    return res


if __name__ == "__main__":
    nums = [1, 2, 3, 2, 2, 1, 3]
    k = 3
    assert distinctNumbers(nums, k) == [3, 2, 2, 2, 3]

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

## 2107. Number of Unique Flavors After Sharing K Candies

-   [LeetCode](https://leetcode.com/problems/number-of-unique-flavors-after-sharing-k-candies/) | [LeetCode CH](https://leetcode.cn/problems/number-of-unique-flavors-after-sharing-k-candies/) (Medium)

-   Tags: array, hash table, sliding window

```python title="2107. Number of Unique Flavors After Sharing K Candies - Python Solution"
from collections import Counter
from typing import List


# Sliding Window Fixed Size
def shareCandies(candies: List[int], k: int) -> int:
    res = 0
    n = len(candies)
    counts = Counter(candies)

    if k >= n:
        return 0
    if k == 0:
        return len(counts)

    for right in range(n):
        counts[candies[right]] -= 1  # remove
        if counts[candies[right]] == 0:
            del counts[candies[right]]

        if right < k - 1:  # form the window
            continue

        res = max(res, len(counts))  # update

        left = right - k + 1  # add
        counts[candies[left]] += 1

    return res


if __name__ == "__main__":
    candies = [1, 2, 2, 3, 4, 3]
    k = 3
    assert shareCandies(candies, k) == 3

```
