---
comments: True
---

# String Minimal Representation

## Table of Contents

- [ ] [1163. Last Substring in Lexicographical Order](https://leetcode.cn/problems/last-substring-in-lexicographical-order/) (Hard)
- [ ] [899. Orderly Queue](https://leetcode.cn/problems/orderly-queue/) (Hard)
- [x] [3403. Find the Lexicographically Largest String From the Box I](https://leetcode.cn/problems/find-the-lexicographically-largest-string-from-the-box-i/) (Medium)

## 1163. Last Substring in Lexicographical Order

-   [LeetCode](https://leetcode.com/problems/last-substring-in-lexicographical-order/) | [LeetCode CH](https://leetcode.cn/problems/last-substring-in-lexicographical-order/) (Hard)

-   Tags: two pointers, string
## 899. Orderly Queue

-   [LeetCode](https://leetcode.com/problems/orderly-queue/) | [LeetCode CH](https://leetcode.cn/problems/orderly-queue/) (Hard)

-   Tags: math, string, sorting
## 3403. Find the Lexicographically Largest String From the Box I

-   [LeetCode](https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/) | [LeetCode CH](https://leetcode.cn/problems/find-the-lexicographically-largest-string-from-the-box-i/) (Medium)

-   Tags: two pointers, string, enumeration

```python title="3403. Find the Lexicographically Largest String From the Box I - Python Solution"
# Lexicographically Smallest/Largest
def answerString(word: str, numFriends: int) -> str:
    if numFriends == 1:
        return word

    n = len(word)
    return max(word[i : i + n - numFriends + 1] for i in range(n))


if __name__ == "__main__":
    assert answerString("dbca", 2) == "dbc"

```
