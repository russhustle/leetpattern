---
comments: True
---

# Lexicographically Smallest

## Table of Contents

- [ ] [402. Remove K Digits](https://leetcode.cn/problems/remove-k-digits/) (Medium)
- [ ] [1673. Find the Most Competitive Subsequence](https://leetcode.cn/problems/find-the-most-competitive-subsequence/) (Medium)
- [x] [316. Remove Duplicate Letters](https://leetcode.cn/problems/remove-duplicate-letters/) (Medium)
- [ ] [1081. Smallest Subsequence of Distinct Characters](https://leetcode.cn/problems/smallest-subsequence-of-distinct-characters/) (Medium)
- [ ] [321. Create Maximum Number](https://leetcode.cn/problems/create-maximum-number/) (Hard)
- [ ] [2030. Smallest K-Length Subsequence With Occurrences of a Letter](https://leetcode.cn/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/) (Hard)

## 402. Remove K Digits

-   [LeetCode](https://leetcode.com/problems/remove-k-digits/) | [LeetCode CH](https://leetcode.cn/problems/remove-k-digits/) (Medium)

-   Tags: string, stack, greedy, monotonic stack
## 1673. Find the Most Competitive Subsequence

-   [LeetCode](https://leetcode.com/problems/find-the-most-competitive-subsequence/) | [LeetCode CH](https://leetcode.cn/problems/find-the-most-competitive-subsequence/) (Medium)

-   Tags: array, stack, greedy, monotonic stack
## 316. Remove Duplicate Letters

-   [LeetCode](https://leetcode.com/problems/remove-duplicate-letters/) | [LeetCode CH](https://leetcode.cn/problems/remove-duplicate-letters/) (Medium)

-   Tags: string, stack, greedy, monotonic stack

```python title="316. Remove Duplicate Letters - Python Solution"
# Monotonic Stack
def removeDuplicateLetters(s: str) -> str:
    stack = []
    seen = set()
    last = {c: i for i, c in enumerate(s)}

    for i, c in enumerate(s):
        if c not in seen:
            while stack and c < stack[-1] and i < last[stack[-1]]:
                seen.discard(stack.pop())
            seen.add(c)
            stack.append(c)

    return "".join(stack)


s = "cbacdcbc"
print(removeDuplicateLetters(s))  # acdb

```

## 1081. Smallest Subsequence of Distinct Characters

-   [LeetCode](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/) | [LeetCode CH](https://leetcode.cn/problems/smallest-subsequence-of-distinct-characters/) (Medium)

-   Tags: string, stack, greedy, monotonic stack
## 321. Create Maximum Number

-   [LeetCode](https://leetcode.com/problems/create-maximum-number/) | [LeetCode CH](https://leetcode.cn/problems/create-maximum-number/) (Hard)

-   Tags: array, two pointers, stack, greedy, monotonic stack
## 2030. Smallest K-Length Subsequence With Occurrences of a Letter

-   [LeetCode](https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/) | [LeetCode CH](https://leetcode.cn/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/) (Hard)

-   Tags: string, stack, greedy, monotonic stack
