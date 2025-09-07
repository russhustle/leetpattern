---
comments: True
---

# Stack

## Table of Contents

- [x] [20. Valid Parentheses](https://leetcode.cn/problems/valid-parentheses/) (Easy)

## 20. Valid Parentheses

-   [LeetCode](https://leetcode.com/problems/valid-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/valid-parentheses/) (Easy)

-   Tags: string, stack
```python title="20. Valid Parentheses - Python Solution"
# Stack
def is_valid(s: str) -> bool:
    if len(s) % 2:
        return False

    pairs = {
        "(": ")",
        "{": "}",
        "[": "]",
    }
    stack = []
    for ch in s:
        if ch in pairs:
            stack.append(ch)
        elif not stack or ch != pairs[stack.pop()]:
            return False

    return True if not stack else False


def test_is_valid():
    assert is_valid("()[]{}")
    assert not is_valid("(]")
    assert not is_valid("([)]")
    assert is_valid("{[]}")

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
