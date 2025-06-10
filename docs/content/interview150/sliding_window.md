---
comments: True
---

# Sliding Window

## Table of Contents

- [x] [209. Minimum Size Subarray Sum](https://leetcode.cn/problems/minimum-size-subarray-sum/) (Medium)
- [x] [3. Longest Substring Without Repeating Characters](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) (Medium)
- [ ] [30. Substring with Concatenation of All Words](https://leetcode.cn/problems/substring-with-concatenation-of-all-words/) (Hard)
- [x] [76. Minimum Window Substring](https://leetcode.cn/problems/minimum-window-substring/) (Hard)

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

## 30. Substring with Concatenation of All Words

-   [LeetCode](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) | [LeetCode CH](https://leetcode.cn/problems/substring-with-concatenation-of-all-words/) (Hard)

-   Tags: hash table, string, sliding window
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
