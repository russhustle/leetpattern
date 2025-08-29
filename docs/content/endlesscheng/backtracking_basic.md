---
comments: True
---

# Backtracking Basic

## Table of Contents

- [x] [17. Letter Combinations of a Phone Number](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/) (Medium)

## 17. Letter Combinations of a Phone Number

-   [LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | [LeetCode CH](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/) (Medium)

-   Tags: hash table, string, backtracking
-   Return all possible letter combinations that the number could represent.

![17](https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png)

```python title="17. Letter Combinations of a Phone Number - Python Solution"
from typing import List


# Backtracking
def letterCombinations(digits: str) -> List[str]:
    letter_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    n = len(digits)
    if n == 0:
        return []

    res = []

    def dfs(idx, path):
        if idx == n:
            res.append(path)
            return None

        letters = letter_map[digits[idx]]

        for i in range(len(letters)):
            dfs(idx + 1, path + letters[i])

    dfs(0, "")

    return res


if __name__ == "__main__":
    assert letterCombinations("23") == [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf",
    ]

```

