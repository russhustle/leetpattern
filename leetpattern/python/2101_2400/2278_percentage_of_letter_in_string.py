from collections import Counter


def percentageLetter(s: str, letter: str) -> int:
    cnt = Counter(s)
    n = len(s)

    if letter in cnt.keys():
        return int(cnt[letter] / n * 100)

    return 0


if __name__ == "__main__":
    s = "foobar"
    letter = "o"
    print(percentageLetter(s, letter))  # 33
