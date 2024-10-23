# Reverse
def isPalindromeReverse(x: int) -> bool:
    if x < 0:
        return False

    return str(x) == str(x)[::-1]


# Left Right Pointers
def isPalindromeLR(x: int) -> bool:
    if x < 0:
        return False

    x = list(str(x))  # 121 -> ['1', '2', '1']

    left, right = 0, len(x) - 1

    while left < right:
        if x[left] != x[right]:
            return False
        left += 1
        right -= 1

    return True


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# |  Reverse   |  O(N)  |   O(N)  |
# | Left Right |  O(N)  |   O(1)  |
# |------------|--------|---------|


x = 121
print(isPalindromeReverse(x))  # True
print(isPalindromeLR(x))  # True
