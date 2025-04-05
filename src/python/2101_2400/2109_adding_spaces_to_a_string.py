from typing import List


def addSpaces(s: str, spaces: List[int]) -> str:
    res = []
    spaces.sort()
    n = len(spaces)
    j = 0

    for i, ch in enumerate(s):
        if j < n and i == spaces[j]:
            res.append(" ")
            j += 1
        res.append(ch)

    return "".join(res)


if __name__ == "__main__":
    s = "LeetcodeHelpsMeLearn"
    spaces = [8, 13, 15]
    print(addSpaces(s, spaces))  # Leetcode Helps Me Learn
