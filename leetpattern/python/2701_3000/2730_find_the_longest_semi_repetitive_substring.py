# Sliding Window Variable Max
def longestSemiRepetitiveSubstring(s: str) -> int:
    n = len(s)
    left = 0
    repeat = 0
    res = 1

    for right in range(1, n):
        if s[right] == s[right - 1]:
            repeat += 1

        while repeat > 1:
            if s[left] == s[left + 1]:
                repeat -= 1
            left += 1

        res = max(res, right - left + 1)

    return res


if __name__ == "__main__":
    assert longestSemiRepetitiveSubstring("abacaba") == 7
    assert longestSemiRepetitiveSubstring("aa") == 2
    assert longestSemiRepetitiveSubstring("a") == 1
    assert longestSemiRepetitiveSubstring("abcde") == 5
