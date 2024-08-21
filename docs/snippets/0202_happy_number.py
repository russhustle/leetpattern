def isHappy(n: int) -> bool:
    def getSum(n):
        result = 0
        while n:
            a, b = divmod(n, 10)
            result += b**2
            n = a
        return result

    record = set()

    while True:
        if n == 1:
            return True

        if n in record:
            return False
        else:
            record.add(n)

        n = getSum(n)


n = 19
print(isHappy(n))  # True
