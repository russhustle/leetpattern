---
comments: True
---

# Sliding Window

## Table of Contents

- [x] [121. Best Time to Buy and Sell Stock](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/) (Easy)
- [x] [3. Longest Substring Without Repeating Characters](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) (Medium)
- [x] [424. Longest Repeating Character Replacement](https://leetcode.cn/problems/longest-repeating-character-replacement/) (Medium)
- [x] [76. Minimum Window Substring](https://leetcode.cn/problems/minimum-window-substring/) (Hard)
- [x] [567. Permutation in String](https://leetcode.cn/problems/permutation-in-string/) (Medium)
- [x] [239. Sliding Window Maximum](https://leetcode.cn/problems/sliding-window-maximum/) (Hard)

## 121. Best Time to Buy and Sell Stock

-   [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | [LeetCode CH](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/) (Easy)

-   Tags: array, dynamic programming
-   Return the maximum profit that can be achieved from buying on one day and selling on another day.

```python title="121. Best Time to Buy and Sell Stock - Python Solution"
from typing import List


# Brute Force
def maxProfitBF(prices: List[int]) -> int:
    max_profit = 0
    n = len(prices)
    for i in range(n):
        for j in range(i + 1, n):
            max_profit = max(max_profit, prices[j] - prices[i])

    return max_profit


# DP
def maxProfitDP(prices: List[int]) -> int:
    dp = [[0] * 2 for _ in range(len(prices))]
    dp[0][0] = -prices[0]  # buy
    dp[0][1] = 0  # sell

    for i in range(1, len(prices)):
        dp[i][0] = max(dp[i - 1][0], -prices[i])  # the lowest price to buy
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])

    return dp[-1][1]


# Greedy
def maxProfitGreedy(prices: List[int]) -> int:
    max_profit = 0
    seen_min = prices[0]

    for i in range(1, len(prices)):
        max_profit = max(max_profit, prices[i] - seen_min)
        seen_min = min(seen_min, prices[i])

    return max_profit


# Fast Slow Pointers
def maxProfitFS(prices: List[int]) -> int:
    max_profit = 0
    slow, fast = 0, 1

    while fast < len(prices):
        if prices[fast] > prices[slow]:
            max_profit = max(max_profit, prices[fast] - prices[slow])
        else:
            slow = fast
        fast += 1

    return max_profit


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# | Brute Force|  O(n^2)|  O(1)   |
# | DP         |  O(n)  |  O(n)   |
# | Greedy     |  O(n)  |  O(1)   |
# | Fast Slow  |  O(n)  |  O(1)   |
# |------------|--------|---------|


prices = [7, 1, 5, 3, 6, 4]
print(maxProfitBF(prices))  # 5
print(maxProfitDP(prices))  # 5
print(maxProfitGreedy(prices))  # 5
print(maxProfitFS(prices))  # 5

```

```cpp title="121. Best Time to Buy and Sell Stock - C++ Solution"
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        if (prices.size() <= 1)
            return 0;

        int seen_min = prices[0];
        int res = 0;

        for (int &price : prices)
        {
            res = max(res, price - seen_min);
            seen_min = min(seen_min, price);
        }
        return res;
    }
};

int main()
{
    vector<int> prices = {7, 1, 5, 3, 6, 4};
    Solution obj;
    cout << obj.maxProfit(prices) << endl;
    return 0;
}
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

## 239. Sliding Window Maximum

-   [LeetCode](https://leetcode.com/problems/sliding-window-maximum/) | [LeetCode CH](https://leetcode.cn/problems/sliding-window-maximum/) (Hard)

-   Tags: array, queue, sliding window, heap priority queue, monotonic queue
```python title="239. Sliding Window Maximum - Python Solution"
from collections import deque
from typing import List


# Monotonic Queue
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    q = deque()
    res = []

    for i, num in enumerate(nums):
        if q and q[0] < i - k + 1:
            q.popleft()

        while q and nums[q[-1]] < num:
            q.pop()

        q.append(i)

        if i >= k - 1:
            res.append(nums[q[0]])

    return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(maxSlidingWindow(nums, k))  # [3, 3, 5, 5, 6, 7]

```
