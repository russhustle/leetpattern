from collections import defaultdict


# Sliding Window - Variable
def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    n = len(s)
    if n <= 2:
        return n

    window = defaultdict(int)

    left = 0
    res = 0

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
print(lengthOfLongestSubstringTwoDistinct(s))  # 5
