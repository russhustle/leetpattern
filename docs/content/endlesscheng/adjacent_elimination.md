---
comments: True
---

# Adjacent Elimination

## Table of Contents

- [ ] [2696. Minimum String Length After Removing Substrings](https://leetcode.cn/problems/minimum-string-length-after-removing-substrings/) (Easy)
- [ ] [1047. Remove All Adjacent Duplicates In String](https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/) (Easy)
- [x] [1544. Make The String Great](https://leetcode.cn/problems/make-the-string-great/) (Easy)
- [ ] [1003. Check If Word Is Valid After Substitutions](https://leetcode.cn/problems/check-if-word-is-valid-after-substitutions/) (Medium)
- [ ] [2216. Minimum Deletions to Make Array Beautiful](https://leetcode.cn/problems/minimum-deletions-to-make-array-beautiful/) (Medium)
- [ ] [1209. Remove All Adjacent Duplicates in String II](https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string-ii/) (Medium)
- [ ] [2211. Count Collisions on a Road](https://leetcode.cn/problems/count-collisions-on-a-road/) (Medium)
- [ ] [735. Asteroid Collision](https://leetcode.cn/problems/asteroid-collision/) (Medium)
- [ ] [1717. Maximum Score From Removing Substrings](https://leetcode.cn/problems/maximum-score-from-removing-substrings/) (Medium)
- [ ] [2197. Replace Non-Coprime Numbers in Array](https://leetcode.cn/problems/replace-non-coprime-numbers-in-array/) (Hard)
- [ ] [2751. Robot Collisions](https://leetcode.cn/problems/robot-collisions/) (Hard)

## 2696. Minimum String Length After Removing Substrings

-   [LeetCode](https://leetcode.com/problems/minimum-string-length-after-removing-substrings/) | [LeetCode CH](https://leetcode.cn/problems/minimum-string-length-after-removing-substrings/) (Easy)

-   Tags: string, stack, simulation
## 1047. Remove All Adjacent Duplicates In String

-   [LeetCode](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/) | [LeetCode CH](https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/) (Easy)

-   Tags: string, stack
## 1544. Make The String Great

-   [LeetCode](https://leetcode.com/problems/make-the-string-great/) | [LeetCode CH](https://leetcode.cn/problems/make-the-string-great/) (Easy)

-   Tags: string, stack
-   Remove all adjacent characters that are the same and have different cases.
-   Steps for the string `leEeetcode`:

| char | action | stack      |
| ---- | ------ | ---------- |
| l    | push   | "l"        |
| e    | push   | "le"       |
| E    | pop    | "l"        |
| e    | push   | "le"       |
| e    | push   | "lee"      |
| t    | push   | "leet"     |
| c    | push   | "leetc"    |
| o    | push   | "leetco"   |
| d    | push   | "leetcod"  |
| e    | push   | "leetcode" |


```python title="1544. Make The String Great - Python Solution"
# Stack
def makeGood(s: str) -> str:
    stack = []

    for i in range(len(s)):
        if stack and stack[-1] == s[i].swapcase():
            stack.pop()
        else:
            stack.append(s[i])
    return "".join(stack)


print(makeGood("leEeetcode"))  # "leetcode"

```

## 1003. Check If Word Is Valid After Substitutions

-   [LeetCode](https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/) | [LeetCode CH](https://leetcode.cn/problems/check-if-word-is-valid-after-substitutions/) (Medium)

-   Tags: string, stack
## 2216. Minimum Deletions to Make Array Beautiful

-   [LeetCode](https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/) | [LeetCode CH](https://leetcode.cn/problems/minimum-deletions-to-make-array-beautiful/) (Medium)

-   Tags: array, stack, greedy
## 1209. Remove All Adjacent Duplicates in String II

-   [LeetCode](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/) | [LeetCode CH](https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string-ii/) (Medium)

-   Tags: string, stack
## 2211. Count Collisions on a Road

-   [LeetCode](https://leetcode.com/problems/count-collisions-on-a-road/) | [LeetCode CH](https://leetcode.cn/problems/count-collisions-on-a-road/) (Medium)

-   Tags: string, stack, simulation
## 735. Asteroid Collision

-   [LeetCode](https://leetcode.com/problems/asteroid-collision/) | [LeetCode CH](https://leetcode.cn/problems/asteroid-collision/) (Medium)

-   Tags: array, stack, simulation
## 1717. Maximum Score From Removing Substrings

-   [LeetCode](https://leetcode.com/problems/maximum-score-from-removing-substrings/) | [LeetCode CH](https://leetcode.cn/problems/maximum-score-from-removing-substrings/) (Medium)

-   Tags: string, stack, greedy
## 2197. Replace Non-Coprime Numbers in Array

-   [LeetCode](https://leetcode.com/problems/replace-non-coprime-numbers-in-array/) | [LeetCode CH](https://leetcode.cn/problems/replace-non-coprime-numbers-in-array/) (Hard)

-   Tags: array, math, stack, number theory
## 2751. Robot Collisions

-   [LeetCode](https://leetcode.com/problems/robot-collisions/) | [LeetCode CH](https://leetcode.cn/problems/robot-collisions/) (Hard)

-   Tags: array, stack, sorting, simulation
