# Sliding Window Variable Size
def shortestBeautifulSubstring(s: str, k: int) -> str:
    n = len(s)
    left = 0
    oneCount = 0
    minLen = float("inf")
    res = ""

    for right in range(n):
        if s[right] == "1":
            oneCount += 1

        while oneCount == k:
            size = right - left + 1

            if size < minLen:
                minLen = size
                res = s[left : right + 1]
            elif size == minLen:
                res = min(res, s[left : right + 1])

            if s[left] == "1":
                oneCount -= 1
            left += 1

    return res


s = "100011001"
k = 3
print(shortestBeautifulSubstring(s, k))  # 11001
