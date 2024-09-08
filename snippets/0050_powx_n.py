# Iterative
def myPowIterative(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n

    result = 1
    cur = x

    while n > 0:
        if n % 2 == 1:
            result *= cur

        cur *= cur
        n //= 2

    return result


# Recursive
def myPowRecursive(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n

    if n % 2 == 0:
        return myPowRecursive(x * x, n // 2)
    else:
        return x * myPowRecursive(x * x, n // 2)


x = 2.00000
n = 10
print(myPowIterative(x, n))  # 1024.0
print(myPowRecursive(x, n))  # 1024.0
