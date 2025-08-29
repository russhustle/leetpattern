from collections import defaultdict


# Sliding Window Variable Size
def numberOfSubstrings(s: str) -> int:
    freqs = defaultdict(int)
    res = 0
    left = 0

    for right in range(len(s)):
        freqs[s[right]] += 1

        while len(freqs) == 3:
            freqs[s[left]] -= 1
            if freqs[s[left]] == 0:
                del freqs[s[left]]
            left += 1

        res += left

    return res


s = "abcabc"
print(numberOfSubstrings(s))  # 10
