---
comments: True
---

# Valid Parentheses Strings

- [x] [20. Valid Parentheses](https://leetcode.cn/problems/valid-parentheses/) (Easy)
- [ ] [921. Minimum Add to Make Parentheses Valid](https://leetcode.cn/problems/minimum-add-to-make-parentheses-valid/) (Medium)
- [ ] [1021. Remove Outermost Parentheses](https://leetcode.cn/problems/remove-outermost-parentheses/) (Easy)
- [ ] [1614. Maximum Nesting Depth of the Parentheses](https://leetcode.cn/problems/maximum-nesting-depth-of-the-parentheses/) (Easy)
- [ ] [1190. Reverse Substrings Between Each Pair of Parentheses](https://leetcode.cn/problems/reverse-substrings-between-each-pair-of-parentheses/) (Medium)
- [ ] [856. Score of Parentheses](https://leetcode.cn/problems/score-of-parentheses/) (Medium)
- [ ] [1249. Minimum Remove to Make Valid Parentheses](https://leetcode.cn/problems/minimum-remove-to-make-valid-parentheses/) (Medium)
- [x] [1963. Minimum Number of Swaps to Make the String Balanced](https://leetcode.cn/problems/minimum-number-of-swaps-to-make-the-string-balanced/) (Medium)
- [x] [678. Valid Parenthesis String](https://leetcode.cn/problems/valid-parenthesis-string/) (Medium)
- [ ] [1111. Maximum Nesting Depth of Two Valid Parentheses Strings](https://leetcode.cn/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/) (Medium)
- [ ] [1541. Minimum Insertions to Balance a Parentheses String](https://leetcode.cn/problems/minimum-insertions-to-balance-a-parentheses-string/) (Medium)
- [ ] [2116. Check if a Parentheses String Can Be Valid](https://leetcode.cn/problems/check-if-a-parentheses-string-can-be-valid/) (Medium)
- [ ] [32. Longest Valid Parentheses](https://leetcode.cn/problems/longest-valid-parentheses/) (Hard)

## 20. Valid Parentheses

-   [LeetCode](https://leetcode.com/problems/valid-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/valid-parentheses/) (Easy)

-   Tags: string, stack
-   Determine if the input string is valid.
-   Steps for the string `()[]{}`:

| char | action | stack |
| ---- | ------ | ----- |
| `(`  | push   | "\("  |
| `)`  | pop    | ""    |
| `[`  | push   | "\["  |
| `]`  | pop    | ""    |
| `{`  | push   | "\{"  |
| `}`  | pop    | ""    |

```python title="20. Valid Parentheses - Python Solution"
# Stack
def isValid(s: str) -> bool:
    hashmap = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    stack = []

    for c in s:
        if c in hashmap:
            if stack and stack[-1] == hashmap[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return True if not stack else False


print(isValid("()"))  # True
print(isValid("()[]{}"))  # True
print(isValid("(]"))  # False

```

```cpp title="20. Valid Parentheses - C++ Solution"
#include <cassert>
#include <stack>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
   public:
    bool isValid(string s) {
        unordered_map<char, char> map{{')', '('}, {'}', '{'}, {']', '['}};
        stack<char> stack;
        if (s.length() % 2 == 1) return false;

        for (char& ch : s) {
            if (stack.empty() || map.find(ch) == map.end()) {
                stack.push(ch);
            } else {
                if (map[ch] != stack.top()) {
                    return false;
                }
                stack.pop();
            }
        }
        return stack.empty();
    }
};

int main() {
    Solution s;
    assert(s.isValid("()") == true);
    assert(s.isValid("()[]{}") == true);
    assert(s.isValid("(]") == false);
    assert(s.isValid("([)]") == false);
    assert(s.isValid("{[]}") == true);
    return 0;
}

```

## 921. Minimum Add to Make Parentheses Valid

-   [LeetCode](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/) | [LeetCode CH](https://leetcode.cn/problems/minimum-add-to-make-parentheses-valid/) (Medium)

-   Tags: string, stack, greedy

## 1021. Remove Outermost Parentheses

-   [LeetCode](https://leetcode.com/problems/remove-outermost-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/remove-outermost-parentheses/) (Easy)

-   Tags: string, stack

## 1614. Maximum Nesting Depth of the Parentheses

-   [LeetCode](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/maximum-nesting-depth-of-the-parentheses/) (Easy)

-   Tags: string, stack

## 1190. Reverse Substrings Between Each Pair of Parentheses

-   [LeetCode](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/reverse-substrings-between-each-pair-of-parentheses/) (Medium)

-   Tags: string, stack

## 856. Score of Parentheses

-   [LeetCode](https://leetcode.com/problems/score-of-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/score-of-parentheses/) (Medium)

-   Tags: string, stack

## 1249. Minimum Remove to Make Valid Parentheses

-   [LeetCode](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/minimum-remove-to-make-valid-parentheses/) (Medium)

-   Tags: string, stack

## 1963. Minimum Number of Swaps to Make the String Balanced

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-swaps-to-make-the-string-balanced/) (Medium)

-   Tags: two pointers, string, stack, greedy

```python title="1963. Minimum Number of Swaps to Make the String Balanced - Python Solution"
def minSwaps(s: str) -> int:
    res, balance = 0, 0

    for char in s:
        if char == "[":
            balance += 1
        elif balance > 0:
            balance -= 1
        else:
            res += 1
            balance += 1

    return res


if __name__ == "__main__":
    print(minSwaps("][]["))  # 1
    print(minSwaps("]]][[["))  # 2

```

## 678. Valid Parenthesis String

-   [LeetCode](https://leetcode.com/problems/valid-parenthesis-string/) | [LeetCode CH](https://leetcode.cn/problems/valid-parenthesis-string/) (Medium)

-   Tags: string, dynamic programming, stack, greedy

```python title="678. Valid Parenthesis String - Python Solution"
# Greedy
def checkValidString(s: str) -> bool:
    min_open, max_open = 0, 0

    for char in s:
        if char == "(":
            min_open += 1
            max_open += 1
        elif char == ")":
            min_open = max(min_open - 1, 0)
            max_open -= 1
        elif char == "*":
            min_open = max(min_open - 1, 0)
            max_open += 1

        if max_open < 0:
            return False

    return min_open == 0


s = "(*))"
print(checkValidString(s))  # True

```

## 1111. Maximum Nesting Depth of Two Valid Parentheses Strings

-   [LeetCode](https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/) | [LeetCode CH](https://leetcode.cn/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/) (Medium)

-   Tags: string, stack

## 1541. Minimum Insertions to Balance a Parentheses String

-   [LeetCode](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/) | [LeetCode CH](https://leetcode.cn/problems/minimum-insertions-to-balance-a-parentheses-string/) (Medium)

-   Tags: string, stack, greedy

## 2116. Check if a Parentheses String Can Be Valid

-   [LeetCode](https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/) | [LeetCode CH](https://leetcode.cn/problems/check-if-a-parentheses-string-can-be-valid/) (Medium)

-   Tags: string, stack, greedy

## 32. Longest Valid Parentheses

-   [LeetCode](https://leetcode.com/problems/longest-valid-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/longest-valid-parentheses/) (Hard)

-   Tags: string, dynamic programming, stack
