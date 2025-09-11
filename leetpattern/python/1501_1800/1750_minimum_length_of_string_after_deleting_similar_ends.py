# Sliding Window Variable Size
def minimumLength(s: str) -> int:
    left, right = 0, len(s) - 1

    while left < right and s[left] == s[right]:
        val = s[left]

        while left <= right and s[left] == val:
            left += 1
        while left <= right and s[right] == val:
            right -= 1

    return right - left + 1


print(minimumLength("cabaabac"))  # 0
print(minimumLength("aabccabba"))  # 3
