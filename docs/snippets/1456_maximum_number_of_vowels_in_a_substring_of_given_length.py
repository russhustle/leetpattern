from typing import List


# Sliding Window - Fixed
def maxVowels(s: str, k: int) -> int:
    vowel = set("aeiou")
    count = 0

    for i in range(k):
        if s[i] in vowel:
            count += 1

    max_count = count

    for i in range(k, len(s)):
        if s[i] in vowel:
            count += 1
        if s[i - k] in vowel:
            count -= 1

        max_count = max(max_count, count)

        if max_count == k:
            break

    return max_count


s = "abciiidef"
k = 3
print(maxVowels(s, k))  # 3
