# Traversal
def scoreOfString(s: str) -> int:
    res = 0

    for i in range(1, len(s)):
        res += abs(ord(s[i]) - ord(s[i - 1]))

    return res


if __name__ == "__main__":
    print(scoreOfString("hello"))  # 13
