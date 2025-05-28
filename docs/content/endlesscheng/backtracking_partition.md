---
comments: True
---

# Backtracking Partition

## Table of Contents

- [x] [131. Palindrome Partitioning](https://leetcode.cn/problems/palindrome-partitioning/) (Medium)
- [ ] [2698. Find the Punishment Number of an Integer](https://leetcode.cn/problems/find-the-punishment-number-of-an-integer/) (Medium)
- [ ] [1593. Split a String Into the Max Number of Unique Substrings](https://leetcode.cn/problems/split-a-string-into-the-max-number-of-unique-substrings/) (Medium)
- [ ] [1849. Splitting a String Into Descending Consecutive Values](https://leetcode.cn/problems/splitting-a-string-into-descending-consecutive-values/) (Medium)
- [ ] [306. Additive Number](https://leetcode.cn/problems/additive-number/) (Medium)
- [ ] [842. Split Array into Fibonacci Sequence](https://leetcode.cn/problems/split-array-into-fibonacci-sequence/) (Medium)
- [x] [93. Restore IP Addresses](https://leetcode.cn/problems/restore-ip-addresses/) (Medium)
- [ ] [816. Ambiguous Coordinates](https://leetcode.cn/problems/ambiguous-coordinates/) (Medium)
- [ ] [140. Word Break II](https://leetcode.cn/problems/word-break-ii/) (Hard)
- [ ] [291. Word Pattern II](https://leetcode.cn/problems/word-pattern-ii/) (Medium) 👑

## 131. Palindrome Partitioning

-   [LeetCode](https://leetcode.com/problems/palindrome-partitioning/) | [LeetCode CH](https://leetcode.cn/problems/palindrome-partitioning/) (Medium)

-   Tags: string, dynamic programming, backtracking

```python title="131. Palindrome Partitioning - Python Solution"
from typing import List


# Backtracking
def partition(s: str) -> List[List[str]]:
    n = len(s)
    res, path = [], []

    def dfs(start):
        if start == n:
            res.append(path.copy())
            return

        for end in range(start, n):
            cur = s[start : end + 1]
            if cur == cur[::-1]:
                path.append(cur)
                dfs(end + 1)
                path.pop()

    dfs(0)

    return res


if __name__ == "__main__":
    print(partition("aab"))
    # [['a', 'a', 'b'], ['aa', 'b']]

```

## 2698. Find the Punishment Number of an Integer

-   [LeetCode](https://leetcode.com/problems/find-the-punishment-number-of-an-integer/) | [LeetCode CH](https://leetcode.cn/problems/find-the-punishment-number-of-an-integer/) (Medium)

-   Tags: math, backtracking
## 1593. Split a String Into the Max Number of Unique Substrings

-   [LeetCode](https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/) | [LeetCode CH](https://leetcode.cn/problems/split-a-string-into-the-max-number-of-unique-substrings/) (Medium)

-   Tags: hash table, string, backtracking
## 1849. Splitting a String Into Descending Consecutive Values

-   [LeetCode](https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/) | [LeetCode CH](https://leetcode.cn/problems/splitting-a-string-into-descending-consecutive-values/) (Medium)

-   Tags: string, backtracking
## 306. Additive Number

-   [LeetCode](https://leetcode.com/problems/additive-number/) | [LeetCode CH](https://leetcode.cn/problems/additive-number/) (Medium)

-   Tags: string, backtracking
## 842. Split Array into Fibonacci Sequence

-   [LeetCode](https://leetcode.com/problems/split-array-into-fibonacci-sequence/) | [LeetCode CH](https://leetcode.cn/problems/split-array-into-fibonacci-sequence/) (Medium)

-   Tags: string, backtracking
## 93. Restore IP Addresses

-   [LeetCode](https://leetcode.com/problems/restore-ip-addresses/) | [LeetCode CH](https://leetcode.cn/problems/restore-ip-addresses/) (Medium)

-   Tags: string, backtracking

```python title="93. Restore IP Addresses - Python Solution"
from typing import List


def restoreIpAddresses(s: str) -> List[str]:
    result = []

    def backtracking(start_index, point_num, current, result):
        # stop condition
        if point_num == 3:
            if is_valid(s, start_index, len(s) - 1):
                current += s[start_index:]
                result.append(current)
            return

        for i in range(start_index, len(s)):
            if is_valid(s, start_index, i):
                sub = s[start_index : i + 1]
                backtracking(i + 1, point_num + 1, current + sub + ".", result)
            else:
                break

    def is_valid(s, start, end):
        if start > end:
            return False

        if s[start] == "0" and start != end:
            return False

        num = 0
        for i in range(start, end + 1):
            if not s[i].isdigit():
                return False
            num = num * 10 + int(s[i])
            if num > 255:
                return False
        return True

    backtracking(0, 0, "", result)

    return result


print(restoreIpAddresses("25525511135"))
# ['255.255.11.135', '255.255.111.35']

```

## 816. Ambiguous Coordinates

-   [LeetCode](https://leetcode.com/problems/ambiguous-coordinates/) | [LeetCode CH](https://leetcode.cn/problems/ambiguous-coordinates/) (Medium)

-   Tags: string, backtracking, enumeration
## 140. Word Break II

-   [LeetCode](https://leetcode.com/problems/word-break-ii/) | [LeetCode CH](https://leetcode.cn/problems/word-break-ii/) (Hard)

-   Tags: array, hash table, string, dynamic programming, backtracking, trie, memoization
## 291. Word Pattern II

-   [LeetCode](https://leetcode.com/problems/word-pattern-ii/) | [LeetCode CH](https://leetcode.cn/problems/word-pattern-ii/) (Medium)

-   Tags: hash table, string, backtracking
