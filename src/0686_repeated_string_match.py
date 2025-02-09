import math

from template import LPS


# KMP
def repeatedStringMatch(a: str, b: str) -> int:
    min_repeat = math.ceil(len(b) / len(a))

    def kmp(text, pattern):
        n, m = len(text), len(pattern)
        lps = LPS(pattern)
        j = 0

        for i in range(n):
            while j > 0 and text[i] != pattern[j]:
                j = lps[j - 1]
            if text[i] == pattern[j]:
                j += 1
            if j == m:
                return i - j + 1
        return -1

    for i in range(min_repeat, min_repeat + 2):
        if kmp(a * i, b) != -1:
            return i
    return -1


print(repeatedStringMatch("abcd", "cdabcdab"))  # 3
