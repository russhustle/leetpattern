---
comments: True
---

# Sliding Window Variable

## Table of Contents

- [x] [3. Longest Substring Without Repeating Characters](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) (Medium)
- [x] [159. Longest Substring with At Most Two Distinct Characters](https://leetcode.cn/problems/longest-substring-with-at-most-two-distinct-characters/) (Medium) 👑
- [x] [424. Longest Repeating Character Replacement](https://leetcode.cn/problems/longest-repeating-character-replacement/) (Medium)
- [x] [1208. Get Equal Substrings Within Budget](https://leetcode.cn/problems/get-equal-substrings-within-budget/) (Medium)
- [x] [1004. Max Consecutive Ones III](https://leetcode.cn/problems/max-consecutive-ones-iii/) (Medium)
- [x] [438. Find All Anagrams in a String](https://leetcode.cn/problems/find-all-anagrams-in-a-string/) (Medium)
- [x] [992. Subarrays with K Different Integers](https://leetcode.cn/problems/subarrays-with-k-different-integers/) (Hard)
- [x] [2024. Maximize the Confusion of an Exam](https://leetcode.cn/problems/maximize-the-confusion-of-an-exam/) (Medium)

## 3. Longest Substring Without Repeating Characters

-   [LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [LeetCode CH](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) (Medium)

-   Tags: hash table, string, sliding window
- Classic variable sliding window problem. Use a set to keep track of the characters in the current window.
- Return the length of the longest substring without repeating characters.
- [Template tutorial by 灵山茶艾府](https://leetcode.cn/problems/longest-substring-without-repeating-characters/solutions/1959540/xia-biao-zong-suan-cuo-qing-kan-zhe-by-e-iaks)

```python title="3. Longest Substring Without Repeating Characters - Python Solution"
from collections import defaultdict


# Sliding Window Variable Max - HashMap
def lengthOfLongestSubstringHash(s: str) -> int:
    n = len(s)
    if n <= 1:
        return n

    left = 0
    cnt = defaultdict(int)
    res = 0

    for right in range(n):
        cnt[s[right]] += 1

        while cnt[s[right]] > 1:
            cnt[s[left]] -= 1
            left += 1

        res = max(res, right - left + 1)

    return res


# Sliding Window Variable Max - Set
def lengthOfLongestSubstringSet(s: str) -> int:
    n = len(s)
    if n <= 1:
        return n

    left = 0
    res = 0
    window = set()

    for right in range(n):
        while left < right and s[right] in window:
            window.remove(s[left])
            left += 1
        window.add(s[right])
        res = max(res, right - left + 1)

    return res


if __name__ == "__main__":
    s = "abcabcbb"
    assert lengthOfLongestSubstringHash(s) == 3
    assert lengthOfLongestSubstringSet(s) == 3

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

## 159. Longest Substring with At Most Two Distinct Characters

-   [LeetCode](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/) | [LeetCode CH](https://leetcode.cn/problems/longest-substring-with-at-most-two-distinct-characters/) (Medium)

-   Tags: hash table, string, sliding window
-   Prerequisite: 3. Longest Substring Without Repeating Characters

```python title="159. Longest Substring with At Most Two Distinct Characters - Python Solution"
from collections import defaultdict


# Sliding Window - Variable
def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    n = len(s)
    if n <= 2:
        return n

    window = defaultdict(int)
    left, res = 0, 0

    for right in range(n):
        window[s[right]] += 1

        while len(window) > 2:
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1

        res = max(res, right - left + 1)

    return res


s = "ccaabbb"
assert lengthOfLongestSubstringTwoDistinct(s) == 5

```

## 424. Longest Repeating Character Replacement

-   [LeetCode](https://leetcode.com/problems/longest-repeating-character-replacement/) | [LeetCode CH](https://leetcode.cn/problems/longest-repeating-character-replacement/) (Medium)

-   Tags: hash table, string, sliding window
```python title="424. Longest Repeating Character Replacement - Python Solution"
from collections import defaultdict


# Sliding Window - Variable
def characterReplacement(s: str, k: int) -> int:
    left = 0
    maxCount = 0
    counts = defaultdict(int)
    maxLen = 0

    for right in range(len(s)):
        counts[s[right]] += 1
        maxCount = max(maxCount, counts[s[right]])

        while right - left + 1 - maxCount > k:
            counts[s[left]] -= 1
            left += 1

        maxLen = max(maxLen, right - left + 1)

    return maxLen


s = "ABAB"
k = 2
print(characterReplacement(s, k))  # 4

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

## 438. Find All Anagrams in a String

-   [LeetCode](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | [LeetCode CH](https://leetcode.cn/problems/find-all-anagrams-in-a-string/) (Medium)

-   Tags: hash table, string, sliding window
```python title="438. Find All Anagrams in a String - Python Solution"
from typing import List


# Sliding Window Fixed Size
def findAnagrams(s: str, p: str) -> List[int]:
    n, k = len(s), len(p)
    target = [0 for _ in range(26)]
    for ch in p:
        target[ord(ch) - ord("a")] += 1

    count = [0 for _ in range(26)]
    left = 0
    res = []

    for right in range(n):
        count[ord(s[right]) - ord("a")] += 1
        if right < k - 1:
            continue

        if count == target:
            res.append(left)

        count[ord(s[left]) - ord("a")] -= 1
        left += 1

    return res


s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))  # [0, 6]

```

## 992. Subarrays with K Different Integers

-   [LeetCode](https://leetcode.com/problems/subarrays-with-k-different-integers/) | [LeetCode CH](https://leetcode.cn/problems/subarrays-with-k-different-integers/) (Hard)

-   Tags: array, hash table, sliding window, counting
```python title="992. Subarrays with K Different Integers - Python Solution"
from typing import List


# Sliding Window - Variable
def subarraysWithKDistinct(nums: List[int], k: int) -> int:
    def atMost(k: int) -> int:
        count = 0
        left = 0
        freq = {}

        for right in range(len(nums)):
            if nums[right] not in freq:
                freq[nums[right]] = 0
            freq[nums[right]] += 1

            while len(freq) > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            count += right - left + 1

        return count

    return atMost(k) - atMost(k - 1)


nums = [1, 2, 1, 2, 3]
k = 2
print(subarraysWithKDistinct(nums, k))  # 7

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
