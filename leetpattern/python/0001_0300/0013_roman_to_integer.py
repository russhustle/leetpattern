from itertools import pairwise


# Arrays
def romanToInt(s: str) -> int:
    ROMAN = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    res = 0

    for x, y in pairwise(s):
        x, y = ROMAN[x], ROMAN[y]
        res += x if x >= y else -x

    return res + ROMAN[s[-1]]


if __name__ == "__main__":
    assert romanToInt("III") == 3
    assert romanToInt("IV") == 4
    assert romanToInt("IX") == 9
    assert romanToInt("LVIII") == 58
    assert romanToInt("MCMXCIV") == 1994
    assert romanToInt("MMXXIII") == 2023
