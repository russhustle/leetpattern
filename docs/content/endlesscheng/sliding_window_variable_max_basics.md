---
comments: True
---

# Sliding Window Variable Max Basics

## Table of Contents

- [x] [3. Longest Substring Without Repeating Characters](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) (Medium)
- [x] [3090. Maximum Length Substring With Two Occurrences](https://leetcode.cn/problems/maximum-length-substring-with-two-occurrences/) (Easy)
- [x] [1493. Longest Subarray of 1's After Deleting One Element](https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/) (Medium)
- [x] [1208. Get Equal Substrings Within Budget](https://leetcode.cn/problems/get-equal-substrings-within-budget/) (Medium)
- [x] [904. Fruit Into Baskets](https://leetcode.cn/problems/fruit-into-baskets/) (Medium)
- [x] [1695. Maximum Erasure Value](https://leetcode.cn/problems/maximum-erasure-value/) (Medium)
- [x] [2958. Length of Longest Subarray With at Most K Frequency](https://leetcode.cn/problems/length-of-longest-subarray-with-at-most-k-frequency/) (Medium)
- [x] [2024. Maximize the Confusion of an Exam](https://leetcode.cn/problems/maximize-the-confusion-of-an-exam/) (Medium)
- [x] [1004. Max Consecutive Ones III](https://leetcode.cn/problems/max-consecutive-ones-iii/) (Medium)
- [ ] [1658. Minimum Operations to Reduce X to Zero](https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero/) (Medium)

## 3. Longest Substring Without Repeating Characters

-   [LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [LeetCode CH](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) (Medium)

-   Tags: hash table, string, sliding window
-   Classic sliding window problem. Use a set to keep track of the characters in the current window.
-   Return the length of the longest substring without repeating characters.

<iframe width="560" height="315" src="https://www.youtube.com/embed/wiGpQwVHdE0?si=GlOc9C5w5Vy71iTN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


```python title="3. Longest Substring Without Repeating Characters - Python Solution"
# Sliding Window Variable Size
def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    if n <= 1:
        return n

    window = set()
    left = 0
    res = 0

    for right in range(n):
        while s[right] in window:
            window.remove(s[left])
            left += 1
        window.add(s[right])
        res = max(res, right - left + 1)

    return res


s = "abcabcbb"
assert lengthOfLongestSubstring(s) == 3

```

```cpp title="3. Longest Substring Without Repeating Characters - C++ Solution"
#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;

int lengthOfLongestSubstring(string s) {
    int n = s.length();
    int res = 0;
    int left = 0;
    unordered_set<char> window;

    for (int right = 0; right < n; right++) {
        char ch = s[right];

        while (window.find(ch) != window.end()) {
            window.erase(s[left]);
            left++;
        }

        window.insert(ch);
        res = max(res, right - left + 1);
    }
    return (int)res;
}

int main() {
    string s = "abcabcbb";
    cout << lengthOfLongestSubstring(s) << endl;  // 3
    s = "bbbbb";
    cout << lengthOfLongestSubstring(s) << endl;  // 1
    s = "pwwkew";
    cout << lengthOfLongestSubstring(s) << endl;  // 3
    return 0;
}

```

## 3090. Maximum Length Substring With Two Occurrences

-   [LeetCode](https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/) | [LeetCode CH](https://leetcode.cn/problems/maximum-length-substring-with-two-occurrences/) (Easy)

-   Tags: hash table, string, sliding window

```python title="3090. Maximum Length Substring With Two Occurrences - Python Solution"
from collections import defaultdict


# Sliding Window Variable Size
def maximumLengthSubstring(s: str) -> int:
    n = len(s)
    if n <= 2:
        return n

    counts = defaultdict(int)
    left = 0
    res = 0

    for right in range(n):
        while left < right and counts[s[right]] == 2:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1

        res = max(res, right - left + 1)
        counts[s[right]] += 1

    return res


s = "bcbbbcba"
print(maximumLengthSubstring(s))  # 4

```

## 1493. Longest Subarray of 1's After Deleting One Element

-   [LeetCode](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/) | [LeetCode CH](https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/) (Medium)

-   Tags: array, dynamic programming, sliding window

```python title="1493. Longest Subarray of 1's After Deleting One Element - Python Solution"
from typing import List


# Sliding Window Variable Size
def longestSubarray(nums: List[int]) -> int:
    zeroCount = 0
    res = 0
    left = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeroCount += 1

        while zeroCount > 1:
            if nums[left] == 0:
                zeroCount -= 1
            left += 1

        res = max(res, right - left)

    return res


nums = [1, 1, 0, 1]
print(longestSubarray(nums))  # 3

```

## 1208. Get Equal Substrings Within Budget

-   [LeetCode](https://leetcode.com/problems/get-equal-substrings-within-budget/) | [LeetCode CH](https://leetcode.cn/problems/get-equal-substrings-within-budget/) (Medium)

-   Tags: string, binary search, sliding window, prefix sum

```python title="1208. Get Equal Substrings Within Budget - Python Solution"
# Sliding Window - Variable
def equalSubstring(s: str, t: str, maxCost: int) -> int:
    left = 0
    maxLen = 0
    currentCost = 0

    for right in range(len(s)):
        currentCost += abs(ord(s[right]) - ord(t[right]))

        while currentCost > maxCost:
            currentCost -= abs(ord(s[left]) - ord(t[left]))
            left += 1

        maxLen = max(maxLen, right - left + 1)

    return maxLen


s = "abcd"
t = "bcdf"
maxCost = 3
print(equalSubstring(s, t, maxCost))  # 3

```

## 904. Fruit Into Baskets

-   [LeetCode](https://leetcode.com/problems/fruit-into-baskets/) | [LeetCode CH](https://leetcode.cn/problems/fruit-into-baskets/) (Medium)

-   Tags: array, hash table, sliding window

```python title="904. Fruit Into Baskets - Python Solution"
from collections import defaultdict
from typing import List


# Sliding Window Variable Size
def totalFruit(fruits: List[int]) -> int:
    n = len(fruits)
    if n <= 2:
        return n

    baskets = defaultdict(int)
    res, left = 0, 0

    for right in range(n):
        baskets[fruits[right]] += 1

        while len(baskets) > 2:
            baskets[fruits[left]] -= 1
            if baskets[fruits[left]] == 0:
                del baskets[fruits[left]]
            left += 1

        res = max(res, right - left + 1)

    return res


fruits = [1, 2, 3, 2, 2]
print(totalFruit(fruits))  # 4

```

## 1695. Maximum Erasure Value

-   [LeetCode](https://leetcode.com/problems/maximum-erasure-value/) | [LeetCode CH](https://leetcode.cn/problems/maximum-erasure-value/) (Medium)

-   Tags: array, hash table, sliding window

```python title="1695. Maximum Erasure Value - Python Solution"
from typing import List


# Sliding Window Variable Size
def maximumUniqueSubarray(nums: List[int]) -> int:
    n = len(nums)
    left = 0
    cur, res = 0, 0
    sub = set()

    for right in range(n):
        while left < right and nums[right] in sub:
            sub.remove(nums[left])
            cur -= nums[left]
            left += 1

        sub.add(nums[right])
        cur += nums[right]
        res = max(res, cur)

    return res


nums = [4, 2, 4, 5, 6]
print(maximumUniqueSubarray(nums))  # 17

```

## 2958. Length of Longest Subarray With at Most K Frequency

-   [LeetCode](https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/) | [LeetCode CH](https://leetcode.cn/problems/length-of-longest-subarray-with-at-most-k-frequency/) (Medium)

-   Tags: array, hash table, sliding window

```python title="2958. Length of Longest Subarray With at Most K Frequency - Python Solution"
from collections import defaultdict
from typing import List


# Sliding Window Variable Size
def maxSubarrayLength(nums: List[int], k: int) -> int:
    n = len(nums)
    freqs = defaultdict(int)  # num -> freq
    left = 0
    res = 0

    for right in range(n):
        freqs[nums[right]] += 1

        while freqs[nums[right]] > k:
            freqs[nums[left]] -= 1
            left += 1

        res = max(res, right - left + 1)

    return res


nums = [1, 2, 1, 2, 1, 2, 1, 2]
k = 2
print(maxSubarrayLength(nums, k))  # 4

```

## 2024. Maximize the Confusion of an Exam

-   [LeetCode](https://leetcode.com/problems/maximize-the-confusion-of-an-exam/) | [LeetCode CH](https://leetcode.cn/problems/maximize-the-confusion-of-an-exam/) (Medium)

-   Tags: string, binary search, sliding window, prefix sum

```python title="2024. Maximize the Confusion of an Exam - Python Solution"
# Sliding Window - Variable
def maxConsecutiveAnswers1(answerKey: str, k: int) -> int:
    def maxConsecutiveChar(s: str, k: int, char: str) -> int:
        max_len = 0
        left = 0
        count = 0  # num of str != char

        for right in range(len(s)):
            if s[right] != char:
                count += 1

            while count > k:
                if s[left] != char:
                    count -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

    max_t = maxConsecutiveChar(answerKey, k, "T")
    max_f = maxConsecutiveChar(answerKey, k, "F")

    return max(max_t, max_f)


# Sliding Window - Variable
def maxConsecutiveAnswers2(answerKey: str, k: int) -> int:
    def maxConsecutiveChar(s: str, k: int, char: str) -> int:
        max_len = 0
        left, right = 0, 0

        while right < len(s):
            if s[right] != char:
                k -= 1

            while k < 0:
                if s[left] != char:
                    k += 1
                left += 1

            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len

    max_t = maxConsecutiveChar(answerKey, k, "T")
    max_f = maxConsecutiveChar(answerKey, k, "F")

    return max(max_t, max_f)


# |-----------------|---------|------------|
# |  Approach       |  Time   |  Space     |
# |-----------------|---------|------------|
# | Sliding Window  |  O(N)   |  O(1)      |
# |-----------------|---------|------------|


answerKey = "TTFF"
k = 2
print(maxConsecutiveAnswers1(answerKey, k))  # 4
print(maxConsecutiveAnswers2(answerKey, k))  # 4

```

## 1004. Max Consecutive Ones III

-   [LeetCode](https://leetcode.com/problems/max-consecutive-ones-iii/) | [LeetCode CH](https://leetcode.cn/problems/max-consecutive-ones-iii/) (Medium)

-   Tags: array, binary search, sliding window, prefix sum

```python title="1004. Max Consecutive Ones III - Python Solution"
from typing import List


# Sliding Window - Variable
def longestOnes(nums: List[int], k: int) -> int:
    left = 0
    maxLen = 0
    zero_count = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        maxLen = max(maxLen, right - left + 1)

    return maxLen


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
print(longestOnes(nums, k))  # 6

```

## 1658. Minimum Operations to Reduce X to Zero

-   [LeetCode](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/) | [LeetCode CH](https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero/) (Medium)

-   Tags: array, hash table, binary search, sliding window, prefix sum
