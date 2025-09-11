def minSwaps(s: str) -> int:
    res, balance = 0, 0

    for char in s:
        if char == "[":
            balance += 1
        elif balance > 0:
            balance -= 1
        else:
            res += 1
            balance += 1

    return res


if __name__ == "__main__":
    print(minSwaps("][]["))  # 1
    print(minSwaps("]]][[["))  # 2
