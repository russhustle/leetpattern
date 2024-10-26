# List Comprehension
def isPalindrome(s: str) -> bool:
    s = [char.lower() for char in s if char.isalnum()]
    return s == s[::-1]


# Left Right Pointers
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


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# | Left Right |  O(n)  |  O(1)   |
# |------------|--------|---------|


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))  # True
print(isPalindromeLR(s))  # True
