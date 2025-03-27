from typing import List


def countPrefixes(words: List[str], s: str) -> int:
    res = 0
    for word in words:
        if s.startswith(word):
            res += 1
    return res


if __name__ == "__main__":
    words = ["a", "b", "c", "ab", "bc", "abc"]
    s = "abc"
    print(countPrefixes(words, s))  # 3
