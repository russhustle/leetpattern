# Sliding Window Fixed Size
def maxVowels1(s: str, k: int) -> int:
    res, cnt = 0, 0

    for idx, ch in enumerate(s):
        if ch in "aeiou":
            cnt += 1

        if idx < k - 1:
            continue

        res = max(res, cnt)

        if s[idx - k + 1] in "aeiou":
            cnt -= 1

    return res


# Sliding Window Fixed Size
def maxVowels2(s: str, k: int) -> int:
    vowels = set("aeiou")
    n = len(s)
    cnt, res = 0, 0

    for i in range(k):
        if s[i] in vowels:
            cnt += 1

    res = cnt

    for i in range(k, n):
        if s[i] in vowels:
            cnt += 1
        if s[i - k] in vowels:
            cnt -= 1
        res = max(res, cnt)

    return res


s = "abciiidef"
k = 3
print(maxVowels1(s, k))  # 3
print(maxVowels2(s, k))  # 3
