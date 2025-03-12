---
comments: True
---

# Sliding Window

- [x] [3. Longest Substring Without Repeating Characters](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) (Medium)
- [x] [438. Find All Anagrams in a String](https://leetcode.cn/problems/find-all-anagrams-in-a-string/) (Medium)

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
