def isPalindrome(x: int) -> bool:
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


x = 121
print(isPalindrome(x))  # True
