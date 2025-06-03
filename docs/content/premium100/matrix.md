---
comments: True
---

# Matrix

## Table of Contents

- [x] [422. Valid Word Square](https://leetcode.cn/problems/valid-word-square/) (Easy) 👑
- [ ] [531. Lonely Pixel I](https://leetcode.cn/problems/lonely-pixel-i/) (Medium) 👑
- [ ] [311. Sparse Matrix Multiplication](https://leetcode.cn/problems/sparse-matrix-multiplication/) (Medium) 👑
- [ ] [723. Candy Crush](https://leetcode.cn/problems/candy-crush/) (Medium) 👑

## 422. Valid Word Square

-   [LeetCode](https://leetcode.com/problems/valid-word-square/) | [LeetCode CH](https://leetcode.cn/problems/valid-word-square/) (Easy)

-   Tags: array, matrix

```python title="422. Valid Word Square - Python Solution"
from typing import List


def validWordSquare(words: List[str]) -> bool:
    n = len(words)

    for i in range(n):
        for j in range(len(words[i])):
            if j >= n or i >= len(words[j]) or words[i][j] != words[j][i]:
                return False
    return True


# Zip
def validWordSquareZip(words: List[str]) -> bool:
    max_len = max(len(word) for word in words)
    padded_words = [word.ljust(max_len) for word in words]
    transposed = ["".join(col) for col in zip(*padded_words)]
    return padded_words == transposed


if __name__ == "__main__":
    words1 = ["abcd", "bnrt", "crmy", "dtye"]
    assert validWordSquare(words1)
    assert validWordSquareZip(words1)

    words2 = ["abcd", "bnrt", "crm", "dt"]
    assert validWordSquare(words2)
    assert validWordSquareZip(words2)

    words3 = ["ball", "area", "read", "lady"]
    assert not validWordSquare(words3)
    assert not validWordSquareZip(words3)

```

## 531. Lonely Pixel I

-   [LeetCode](https://leetcode.com/problems/lonely-pixel-i/) | [LeetCode CH](https://leetcode.cn/problems/lonely-pixel-i/) (Medium)

-   Tags: array, hash table, matrix
## 311. Sparse Matrix Multiplication

-   [LeetCode](https://leetcode.com/problems/sparse-matrix-multiplication/) | [LeetCode CH](https://leetcode.cn/problems/sparse-matrix-multiplication/) (Medium)

-   Tags: array, hash table, matrix
## 723. Candy Crush

-   [LeetCode](https://leetcode.com/problems/candy-crush/) | [LeetCode CH](https://leetcode.cn/problems/candy-crush/) (Medium)

-   Tags: array, two pointers, matrix, simulation
