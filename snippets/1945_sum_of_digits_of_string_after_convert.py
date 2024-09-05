# Math
def getLucky(s: str, k: int) -> int:
    def getSum(n: int) -> int:
        total = 0
        while n != 0:
            n, m = divmod(n, 10)
            total += m
        return total

    result = ""
    for i in s:
        result += str(ord(i) - ord("a") + 1)
    result = int(result)

    for _ in range(k):
        result = getSum(result)

    return result


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# |    Math    |  O(n)  |  O(1)   |
# |------------|--------|---------|


s = "iiii"
k = 1

print(getLucky(s, k))  # 36
