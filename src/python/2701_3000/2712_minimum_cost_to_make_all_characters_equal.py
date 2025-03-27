def minimumCost(s: str) -> int:
    n = len(s)
    res = 0
    for i in range(1, n):
        if s[i - 1] != s[i]:
            res += min(i, n - i)

    return res


if __name__ == "__main__":
    s = "0011"
    print(minimumCost(s))  # 2
