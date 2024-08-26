# Sliding Window - Variable
def equalSubstring(s: str, t: str, maxCost: int) -> int:
    left = 0
    maxLen = 0
    currentCost = 0

    for right in range(len(s)):
        currentCost += abs(ord(s[right]) - ord(t[right]))

        while currentCost > maxCost:
            currentCost -= abs(ord(s[left]) - ord(t[left]))
            left += 1

        maxLen = max(maxLen, right - left + 1)

    return maxLen


s = "abcd"
t = "bcdf"
maxCost = 3
print(equalSubstring(s, t, maxCost))  # 3
