from template import LPS


# KMP
def longestPrefix(s: str) -> str:
    if len(s) <= 1:
        return ""

    lps = LPS(s)

    return s[: lps[-1]]


print(longestPrefix("ababab"))  # abab
