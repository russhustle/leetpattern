"""
- Classic variable sliding window problem. Use a set to keep track of the characters in the current window.
- Return the length of the longest substring without repeating characters.
- [Template tutorial by 灵山茶艾府](https://leetcode.cn/problems/longest-substring-without-repeating-characters/solutions/1959540/xia-biao-zong-suan-cuo-qing-kan-zhe-by-e-iaks)
"""

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
