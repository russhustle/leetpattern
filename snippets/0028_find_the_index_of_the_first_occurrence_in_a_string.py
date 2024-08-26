from helper import LPS


def strStr(haystack: str, needle: str) -> int:
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
print(strStr(haystack, needle))  # 2
