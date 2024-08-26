def reverseStr(s: str, k: int) -> str:
    def reverse_substring(text):
        left, right = 0, len(text) - 1
        while left < right:
            text[left], text[right] = text[right], text[left]
            left += 1
            right -= 1
        return text

    result = list(s)

    for i in range(0, len(s), 2 * k):
        result[i : i + k] = reverse_substring(result[i : i + k])

    return "".join(result)


s = "abcdefg"
k = 2
print(reverseStr(s, k))  # "bacdfeg"
