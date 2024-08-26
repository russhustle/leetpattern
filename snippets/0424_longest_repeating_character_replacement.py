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
