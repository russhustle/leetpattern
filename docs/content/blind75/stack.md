---
comments: True
---

# Stack

## Table of Contents

- [x] [20. Valid Parentheses](https://leetcode.cn/problems/valid-parentheses/) (Easy)

## 20. Valid Parentheses

-   [LeetCode](https://leetcode.com/problems/valid-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/valid-parentheses/) (Easy)

-   Tags: string, stack
-   Determine if the input string is valid.
-   Steps for the string `()[]{}`:

| char | action | stack |
| ---- | ------ | ----- |
| `(`  | push   | "("   |
| `)`  | pop    | ""    |
| `[`  | push   | "["   |
| `]`  | pop    | ""    |
| `{`  | push   | "{"   |
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

    for ch in s:
        if ch in hashmap:
            if stack and stack[-1] == hashmap[ch]:
                stack.pop()
            else:
                return False
        else:
            stack.append(ch)

    return True if not stack else False


if __name__ == "__main__":
    assert isValid("()[]{}")
    assert not isValid("(]")
    assert not isValid("([)]")
    assert isValid("{[]}")
    assert isValid("")

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
