from typing import List


def letterCombinations(digits: str) -> List[str]:
    letterMap = [
        "",  # 0
        "",  # 1
        "abc",  # 2
        "def",  # 3
        "ghi",  # 4
        "jkl",  # 5
        "mno",  # 6
        "pqrs",  # 7
        "tuv",  # 8
        "wxyz",  # 9
    ]
    result = []

    def backtracking(index, s):
        if index == len(digits):
            result.append(s)
            return None

        digit = int(digits[index])
        letters = letterMap[digit]

        for i in range(len(letters)):
            backtracking(index + 1, s + letters[i])

    if len(digits) == 0:
        return result

    backtracking(0, "")

    return result


print(letterCombinations("23"))
# ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
