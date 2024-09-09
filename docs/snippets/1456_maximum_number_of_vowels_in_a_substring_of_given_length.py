from typing import List


# Sliding Window - Fixed
def maxVowels(s: str, k: int) -> int:
    vowel = set("aeiou")
    cur = 0

    for i in range(k):
        if s[i] in vowel:
            cur += 1

    max_count = cur

    for i in range(k, len(s)):
        if s[i] in vowel:
            cur += 1
        if s[i - k] in vowel:
            cur -= 1

        max_count = max(max_count, cur)

        if max_count == k:
            break

    return max_count


s = "abciiidef"
k = 3
print(maxVowels(s, k))  # 3
