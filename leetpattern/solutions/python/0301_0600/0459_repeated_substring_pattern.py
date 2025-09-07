from leetpattern.utils import LPS


# KMP
def repeatedSubstringPattern(s: str) -> bool:
    lps = LPS(s)
    length = len(s)

    if lps[-1] != 0 and length % (length - lps[-1]) == 0:
        return True

    return False


s = "abab"
print(repeatedSubstringPattern(s))  # True
