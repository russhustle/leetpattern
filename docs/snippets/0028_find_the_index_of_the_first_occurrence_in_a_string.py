def strStr(haystack: str, needle: str) -> int:
    def LPS(needle):
        lps = [0] * len(needle)
        j = 0
        for i in range(1, len(needle)):
            while j > 0 and needle[i] != needle[j]:
                j = lps[j - 1]
            if needle[i] == needle[j]:
                j += 1
            lps[i] = j
        return lps

    lps = LPS(needle)

    j = 0
    for i in range(len(haystack)):
        while j > 0 and haystack[i] != needle[j]:
            j = lps[j - 1]
        if haystack[i] == needle[j]:
            j += 1
        if j == len(needle):
            return i - len(needle) + 1
    return -1


haystack = "hello"
needle = "ll"
print(strStr(haystack, needle))  # 2
