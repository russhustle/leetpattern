def isBalanced1(num: str) -> bool:
    nums = [int(c) for c in num]
    odd = nums[::2]
    even = nums[1::2]

    return sum(odd) == sum(even)


def isBalanced2(num: str) -> bool:
    cur = 0
    n = len(num)

    for i in range(0, n, 2):
        cur += int(num[i])

    for i in range(1, n, 2):
        cur -= int(num[i])

    return cur == 0


if __name__ == "__main__":
    print(isBalanced1("1234"))  # False
    print(isBalanced1("24123"))  # True
    print(isBalanced2("1234"))  # False
    print(isBalanced2("24123"))  # True
