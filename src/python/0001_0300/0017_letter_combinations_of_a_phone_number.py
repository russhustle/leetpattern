from typing import List


# Backtracking
def letterCombinations(digits: str) -> List[str]:
    letterMap = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz",
    }

    res = []

    def backtrack(idx, s):
        if idx == len(digits):
            res.append(s)
            return None

        digit = int(digits[idx])
        letters = letterMap[digit]

        for i in range(len(letters)):
            backtrack(idx + 1, s + letters[i])

    if len(digits) == 0:
        return res

    backtrack(0, "")

    return res


print(letterCombinations("23"))
# ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
