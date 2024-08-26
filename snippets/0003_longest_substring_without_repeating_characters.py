# Sliding Window - Variable
def lengthOfLongestSubstring(s: str) -> int:
    hashmap = dict()  # char: last index
    left = 0
    maxLen = 0

    for right in range(len(s)):
        if s[right] in hashmap and hashmap[s[right]] >= left:
            left = hashmap[s[right]] + 1

        hashmap[s[right]] = right
        maxLen = max(maxLen, right - left + 1)

    return maxLen


s = "abcabcbb"
print(lengthOfLongestSubstring(s))  # 3
