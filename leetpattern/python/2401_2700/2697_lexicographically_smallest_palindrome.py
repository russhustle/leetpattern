def makeSmallestPalindrome(s: str) -> str:
    n = len(s)
    s = list(s)
    left, right = 0, n - 1

    while left < right:
        if s[left] < s[right]:
            s[right] = s[left]
        elif s[left] > s[right]:
            s[left] = s[right]
        left += 1
        right -= 1

    return "".join(s)


s = "egcfe"
print(makeSmallestPalindrome(s))  # "efcfe"
