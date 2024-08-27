# 1. Filter + Reverse
def isPalindrome(s: str) -> bool:
    s = "".join(filter(str.isalnum, s)).lower()
    return s == s[::-1]


# 2. Left Right Pointers
def isPalindromeLR(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))  # True
print(isPalindromeLR(s))  # True
