from helper import LPS


# 1. Brute Force
def strStrBF(haystack: str, needle: str) -> int:
    # TC: O((m - n) * n)
    # SC: O(1)

    m, n = len(haystack), len(needle)
    for i in range(m - n + 1):
        if haystack[i : i + n] == needle:
            return i
    return -1


# 2. KMP
def strStrKMP(haystack: str, needle: str) -> int:
    # TC: O(m + n)
    # SC: O(n)

    lps = LPS(needle)
    m, n = len(haystack), len(needle)
    j = 0

    for i in range(m):
        while j > 0 and haystack[i] != needle[j]:
            j = lps[j - 1]
        if haystack[i] == needle[j]:
            j += 1
        if j == n:
            return i - n + 1
    return -1


haystack = "hello"
needle = "ll"
print(strStrBF(haystack, needle))  # 2
print(strStrKMP(haystack, needle))  # 2
