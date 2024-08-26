# Greedy
def monotoneIncreasingDigits(n: int) -> int:
    strNum = list(str(n))

    for i in range(len(strNum) - 2, -1, -1):
        if int(strNum[i]) > int(strNum[i + 1]):
            strNum[i] = str(int(strNum[i]) - 1)
            strNum[i + 1 :] = ["9"] * (len(strNum) - (i + 1))

    return int("".join(strNum))


n = 332
print(monotoneIncreasingDigits(n))  # 299
