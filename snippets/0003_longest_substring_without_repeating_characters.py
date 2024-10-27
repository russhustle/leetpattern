# Sliding Window - Variable
def lengthOfLongestSubstring(s: str) -> int:
    window = set()
    left = 0
    res = 0

    for right in range(len(s)):
        while s[right] in window:
            window.remove(s[left])
            left += 1
        window.add(s[right])
        res = max(res, right - left + 1)

    return res


s = "abcabcbb"
print(lengthOfLongestSubstring(s))  # 3
