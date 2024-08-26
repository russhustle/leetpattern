def longestPrefix(s: str) -> str:
    if len(s) <= 1:
        return ""

    def LPS(pattern):
        lps = [0 for _ in range(len(pattern))]
        j = 0

        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            lps[i] = j

        return lps

    lps = LPS(s)

    return s[: lps[-1]]


print(longestPrefix("ababab"))  # abab
