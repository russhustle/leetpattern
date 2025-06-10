"""
- This problem is a classic example of the Sliding Window Fixed Size technique.
- [Templace tutorial by 灵山茶艾府](https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/solutions/2809359/tao-lu-jiao-ni-jie-jue-ding-chang-hua-ch-fzfo)
  -  Technique: add-update-remove (入-更新-出)
"""


# Template of Sliding Window Fixed Size
def templateMaxVowels(s: str, k: int) -> int:
    res, cnt = 0, 0

    for idx, ch in enumerate(s):
        # ADD
        if ch in "aeiou":
            cnt += 1

        # FORM
        if idx < k - 1:
            continue

        # UPDATE
        res = max(res, cnt)

        # REMOVE
        if s[idx - k + 1] in "aeiou":
            cnt -= 1

    return res


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


if __name__ == "__main__":
    s = "abciiidef"
    k = 3
    assert maxVowels1(s, k) == 3
    assert maxVowels2(s, k) == 3
    assert templateMaxVowels(s, k) == 3
