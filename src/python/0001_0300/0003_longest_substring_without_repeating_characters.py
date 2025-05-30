"""
- Classic variable sliding window problem. Use a set to keep track of the characters in the current window.
- Return the length of the longest substring without repeating characters.
"""


# Sliding Window Variable Max
def lengthOfLongestSubstring(s: str) -> int:
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
    assert lengthOfLongestSubstring(s) == 3
