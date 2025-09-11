def calculateTime(keyboard: str, word: str) -> int:
    pos = {char: i for i, char in enumerate(keyboard)}
    cur = 0
    res = 0

    for ch in word:
        target = pos[ch]
        res += abs(target - cur)
        cur = target

    return res


if __name__ == "__main__":
    keyboard = "pqrstuvwxyzabcdefghijklmno"
    word = "leetcode"
    print(calculateTime(keyboard, word))  # 73
