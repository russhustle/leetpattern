from template import LPS


# KMP
def shortestPalindrome(s: str) -> str:
    if not s:
        return s

    new = s + "#" + s[::-1]
    lps = LPS(new)

    add_len = len(s) - lps[-1]

    return s[::-1][:add_len] + s


print(shortestPalindrome("aacecaaa"))  # aaacecaaa
