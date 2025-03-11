---
comments: True
---

# Backtracking Basic

- [x] [17. Letter Combinations of a Phone Number](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/) (Medium)

## 17. Letter Combinations of a Phone Number

-   [LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | [LeetCode CH](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/) (Medium)

-   Tags: hash table, string, backtracking

```python title="17. Letter Combinations of a Phone Number - Python Solution"
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

```
