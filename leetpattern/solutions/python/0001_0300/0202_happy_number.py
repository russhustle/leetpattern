"""
-   Return `True` if the number is a happy number, otherwise, return `False`.
-   A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
"""


def isHappy(n: int) -> bool:

    def getSum(n):
        sum_of_squares = 0
        while n:
            a, b = divmod(n, 10)
            sum_of_squares += b**2
            n = a
        return sum_of_squares

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
