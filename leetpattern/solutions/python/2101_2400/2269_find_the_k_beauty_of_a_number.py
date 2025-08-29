def divisorSubstrings(num: int, k: int) -> int:
    numStr = str(num)
    n = len(numStr)
    res = 0

    for i in range(n - k + 1):
        x = int(numStr[i : i + k])
        if x > 0 and num % x == 0:
            res += 1

    return res


num = 240
k = 2
print(divisorSubstrings(num, k))  # 2
