---
comments: True
---

# String

- [x] [125. Valid Palindrome](https://leetcode.cn/problems/valid-palindrome/) (Easy)
- [x] [242. Valid Anagram](https://leetcode.cn/problems/valid-anagram/) (Easy)
- [x] [409. Longest Palindrome](https://leetcode.cn/problems/longest-palindrome/) (Easy)
- [x] [3. Longest Substring Without Repeating Characters](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) (Medium)
- [ ] [8. String to Integer (atoi)](https://leetcode.cn/problems/string-to-integer-atoi/) (Medium)
- [x] [5. Longest Palindromic Substring](https://leetcode.cn/problems/longest-palindromic-substring/) (Medium)
- [x] [438. Find All Anagrams in a String](https://leetcode.cn/problems/find-all-anagrams-in-a-string/) (Medium)
- [x] [76. Minimum Window Substring](https://leetcode.cn/problems/minimum-window-substring/) (Hard)

## 125. Valid Palindrome

-   [LeetCode](https://leetcode.com/problems/valid-palindrome/) | [LeetCode CH](https://leetcode.cn/problems/valid-palindrome/) (Easy)

-   Tags: two pointers, string

```python title="125. Valid Palindrome - Python Solution"
# List Comprehension
def isPalindrome(s: str) -> bool:
    s = [char.lower() for char in s if char.isalnum()]
    return s == s[::-1]


# Left Right Pointers
def isPalindromeLR(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))  # True
print(isPalindromeLR(s))  # True

```

## 242. Valid Anagram

-   [LeetCode](https://leetcode.com/problems/valid-anagram/) | [LeetCode CH](https://leetcode.cn/problems/valid-anagram/) (Easy)

-   Tags: hash table, string, sorting
-   Return true if an input string is an anagram of another string.
-   An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once, e.g., `listen` is an anagram of `silent`.

```python title="242. Valid Anagram - Python Solution"
from collections import Counter


# Hashmap
def isAnagramHash(s: str, t: str) -> bool:
    """Return True if t is an anagram of s, False otherwise."""
    if len(s) != len(t):
        return False

    count = dict()

    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for j in t:
        if j in count:
            count[j] -= 1
        else:
            return False

    for count in count.values():
        if count != 0:
            return False

    return True


# Array
def isAnagramArray(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = [0 for _ in range(26)]

    for i in s:
        count[ord(i) - ord("a")] += 1

    for j in t:
        count[ord(j) - ord("a")] -= 1

    for i in count:
        if i != 0:
            return False

    return True


# Counter
def isAnagramCounter(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


# |-------------|-----------------|--------------|
# |  Approach   |      Time       |    Space     |
# |-------------|-----------------|--------------|
# |   Hashmap   |       O(n)      |     O(1)     |
# |    Array    |       O(n)      |     O(1)     |
# |   Counter   |       O(n)      |     O(1)     |
# |-------------|-----------------|--------------|


s = "anagram"
t = "nagaram"
print(isAnagramHash(s, t))  # True
print(isAnagramArray(s, t))  # True
print(isAnagramCounter(s, t))  # True

```

## 409. Longest Palindrome

-   [LeetCode](https://leetcode.com/problems/longest-palindrome/) | [LeetCode CH](https://leetcode.cn/problems/longest-palindrome/) (Easy)

-   Tags: hash table, string, greedy
-   Return the length of the longest palindrome that can be built with the characters in the string.

```python title="409. Longest Palindrome - Python Solution"
def longestPalindrome(s: str) -> int:
    hashmap = dict()
    result = 0

    for char in s:
        if char not in hashmap or hashmap[char] == 0:
            hashmap[char] = 1
        else:
            result += 2
            hashmap[char] = 0

    if any(hashmap.values()):
        result += 1

    return result


print(longestPalindrome("abccccdd"))  # 7

```

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

## 8. String to Integer (atoi)

-   [LeetCode](https://leetcode.com/problems/string-to-integer-atoi/) | [LeetCode CH](https://leetcode.cn/problems/string-to-integer-atoi/) (Medium)

-   Tags: string

## 5. Longest Palindromic Substring

-   [LeetCode](https://leetcode.com/problems/longest-palindromic-substring/) | [LeetCode CH](https://leetcode.cn/problems/longest-palindromic-substring/) (Medium)

-   Tags: two pointers, string, dynamic programming
-   Return the longest palindromic substring in `s`.

```python title="5. Longest Palindromic Substring - Python Solution"
# DP - Interval
def longestPalindromeDP(s: str) -> str:
    n = len(s)
    if n <= 1:
        return s

    start, maxLen = 0, 1

    # Init
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1

    for j in range(1, n):
        for i in range(j):
            if s[i] == s[j]:
                if j - i <= 2:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    start = i

    return s[start : start + maxLen]


# Expand Around Center
def longestPalindromeCenter(s: str) -> str:
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    if len(s) <= 1:
        return s

    start, end = 0, 0
    for i in range(len(s)):
        len1 = expand_around_center(i, i)  # odd
        len2 = expand_around_center(i, i + 1)  # even

        maxLen = max(len1, len2)
        if maxLen > end - start:
            start = i - (maxLen - 1) // 2
            end = i + maxLen // 2

    return s[start : end + 1]


s = "babad"
print(longestPalindromeDP(s))  # "bab"
print(longestPalindromeCenter(s))  # "aba"

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
