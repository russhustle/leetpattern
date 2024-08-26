def shortestPalindrome(s: str) -> str:
    if not s:
        return s

    def LPS(pattern):
        lps = [0] * len(pattern)
        j = 0

        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            lps[i] = j
        return lps

    new = s + "#" + s[::-1]
    lps = LPS(new)

    add_len = len(s) - lps[-1]

    return s[::-1][:add_len] + s


print(shortestPalindrome("aacecaaa"))  # aaacecaaa
