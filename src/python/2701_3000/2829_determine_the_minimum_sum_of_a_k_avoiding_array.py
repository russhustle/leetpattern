def minimumSum(n: int, k: int) -> int:
    m = min(k // 2, n)
    return (m * (m + 1) + (k * 2 + n - m - 1) * (n - m)) // 2


if __name__ == "__main__":
    n = 5
    k = 4
    print(minimumSum(n, k))  # 18
