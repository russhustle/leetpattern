---
comments: True
---

# String

- [x] [344. Reverse String](https://leetcode.cn/problems/reverse-string/) (Easy)
- [x] [541. Reverse String II](https://leetcode.cn/problems/reverse-string-ii/) (Easy)
- [x] [151. Reverse Words in a String](https://leetcode.cn/problems/reverse-words-in-a-string/) (Medium)
- [x] [58. Length of Last Word](https://leetcode.cn/problems/length-of-last-word/) (Easy)
- [x] [844. Backspace String Compare](https://leetcode.cn/problems/backspace-string-compare/) (Easy)
- [x] [2185. Counting Words With a Given Prefix](https://leetcode.cn/problems/counting-words-with-a-given-prefix/) (Easy)
- [x] [2000. Reverse Prefix of Word](https://leetcode.cn/problems/reverse-prefix-of-word/) (Easy)

## 344. Reverse String

-   [LeetCode](https://leetcode.com/problems/reverse-string/) | [LeetCode CH](https://leetcode.cn/problems/reverse-string/) (Easy)

-   Tags: two pointers, string

```python title="344. Reverse String - Python Solution"
from typing import List


def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


s = ["h", "e", "l", "l", "o"]
reverseString(s)
print(s)  # ['o', 'l', 'l', 'e', 'h']

```

## 541. Reverse String II

-   [LeetCode](https://leetcode.com/problems/reverse-string-ii/) | [LeetCode CH](https://leetcode.cn/problems/reverse-string-ii/) (Easy)

-   Tags: two pointers, string

```python title="541. Reverse String II - Python Solution"
def reverseStr(s: str, k: int) -> str:
    def reverse_substring(text):
        left, right = 0, len(text) - 1
        while left < right:
            text[left], text[right] = text[right], text[left]
            left += 1
            right -= 1
        return text

    result = list(s)

    for i in range(0, len(s), 2 * k):
        result[i : i + k] = reverse_substring(result[i : i + k])

    return "".join(result)


s = "abcdefg"
k = 2
print(reverseStr(s, k))  # "bacdfeg"

```

## 151. Reverse Words in a String

-   [LeetCode](https://leetcode.com/problems/reverse-words-in-a-string/) | [LeetCode CH](https://leetcode.cn/problems/reverse-words-in-a-string/) (Medium)

-   Tags: two pointers, string

```python title="151. Reverse Words in a String - Python Solution"
def reverseWords(s: str) -> str:
    words = s.split()

    left, right = 0, len(words) - 1

    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1

    return " ".join(words)


s = "the sky is blue"
print(reverseWords(s))  # "blue is sky the"

```

## 58. Length of Last Word

-   [LeetCode](https://leetcode.com/problems/length-of-last-word/) | [LeetCode CH](https://leetcode.cn/problems/length-of-last-word/) (Easy)

-   Tags: string

```python title="58. Length of Last Word - Python Solution"
def lengthOfLastWord(s: str) -> int:
    n = 0

    for i in range(len(s) - 1, -1, -1):
        if s[i] != " ":
            n += 1
        if s[i] == " " and n > 0:
            return n

    return n


print(lengthOfLastWord("Hello World"))  # 5

```

## 844. Backspace String Compare

-   [LeetCode](https://leetcode.com/problems/backspace-string-compare/) | [LeetCode CH](https://leetcode.cn/problems/backspace-string-compare/) (Easy)

-   Tags: two pointers, string, stack, simulation

```python title="844. Backspace String Compare - Python Solution"
def backspaceCompare(s: str, t: str) -> bool:

    def build(text):
        stack = []

        for char in text:
            if char != "#":
                stack.append(char)
            elif stack:
                stack.pop()

        return "".join(stack)

    return build(s) == build(t)


print(backspaceCompare("ab#c", "ad#c"))  # True

```

## 2185. Counting Words With a Given Prefix

-   [LeetCode](https://leetcode.com/problems/counting-words-with-a-given-prefix/) | [LeetCode CH](https://leetcode.cn/problems/counting-words-with-a-given-prefix/) (Easy)

-   Tags: array, string, string matching

```python title="2185. Counting Words With a Given Prefix - Python Solution"
from typing import List


# 1
def prefixCount1(words: List[str], pref: str) -> int:
    count = 0

    for word in words:
        if word.startswith(pref):
            count += 1

    return count


# 2
def prefixCount2(words: List[str], pref: str) -> int:
    count = 0

    for word in words:
        n = len(pref)

        if len(word) < n:
            continue

        if word[:n] == pref:
            count += 1

    return count


words = ["pay", "attention", "practice", "attend"]
pref = "at"
print(prefixCount1(words, pref))  # 2
print(prefixCount2(words, pref))  # 2

```

## 2000. Reverse Prefix of Word

-   [LeetCode](https://leetcode.com/problems/reverse-prefix-of-word/) | [LeetCode CH](https://leetcode.cn/problems/reverse-prefix-of-word/) (Easy)

-   Tags: two pointers, string, stack

```python title="2000. Reverse Prefix of Word - Python Solution"
def reversePrefix(word: str, ch: str) -> str:
    if ch not in word:
        return word

    wordList = list(word)
    left, right = 0, 0

    for i in range(len(wordList)):
        if wordList[i] == ch:
            right = i
            break

    while left < right:
        wordList[left], wordList[right] = wordList[right], wordList[left]
        left += 1
        right -= 1

    return "".join(wordList)


word = "abcdefd"
ch = "d"
print(reversePrefix(word, ch))  # "dcbaefd"

```
