from typing import List


# 1
def prefixCount1(words: List[str], pref: str) -> int:
    count = 0

    for word in words:
        if word.startswith(pref):
            count += 1

    return count


# 2
def prefixCount2(words: List[str], pref: str) -> int:
    count = 0

    for word in words:
        n = len(pref)

        if len(word) < n:
            continue

        if word[:n] == pref:
            count += 1

    return count


words = ["pay", "attention", "practice", "attend"]
pref = "at"
print(prefixCount1(words, pref))  # 2
print(prefixCount2(words, pref))  # 2
