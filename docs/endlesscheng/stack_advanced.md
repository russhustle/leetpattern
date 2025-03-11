---
comments: True
---

# Stack Advanced

- [ ] [3170. Lexicographically Minimum String After Removing Stars](https://leetcode.cn/problems/lexicographically-minimum-string-after-removing-stars/) (Medium)
- [x] [155. Min Stack](https://leetcode.cn/problems/min-stack/) (Medium)
- [ ] [1381. Design a Stack With Increment Operation](https://leetcode.cn/problems/design-a-stack-with-increment-operation/) (Medium)
- [ ] [636. Exclusive Time of Functions](https://leetcode.cn/problems/exclusive-time-of-functions/) (Medium)
- [ ] [2434. Using a Robot to Print the Lexicographically Smallest String](https://leetcode.cn/problems/using-a-robot-to-print-the-lexicographically-smallest-string/) (Medium)
- [ ] [895. Maximum Frequency Stack](https://leetcode.cn/problems/maximum-frequency-stack/) (Hard)
- [ ] [1172. Dinner Plate Stacks](https://leetcode.cn/problems/dinner-plate-stacks/) (Hard)
- [ ] [2589. Minimum Time to Complete All Tasks](https://leetcode.cn/problems/minimum-time-to-complete-all-tasks/) (Hard)
- [ ] [716. Max Stack](https://leetcode.cn/problems/max-stack/) (Hard) 👑

## 3170. Lexicographically Minimum String After Removing Stars

-   [LeetCode](https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/) | [LeetCode CH](https://leetcode.cn/problems/lexicographically-minimum-string-after-removing-stars/) (Medium)

-   Tags: hash table, string, stack, greedy, heap priority queue

## 155. Min Stack

-   [LeetCode](https://leetcode.com/problems/min-stack/) | [LeetCode CH](https://leetcode.cn/problems/min-stack/) (Medium)

-   Tags: stack, design
-   Implement a stack that supports push, pop, top, and retrieving the minimum element in constant time.

```python title="155. Min Stack - Python Solution"
# Stack
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append((val, min(val, self.getMin())))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


obj = MinStack()
obj.push(3)
obj.push(2)
obj.pop()
print(obj.top())  # 3
print(obj.getMin())  # 3

```

```cpp title="155. Min Stack - C++ Solution"
#include <algorithm>
#include <climits>
#include <iostream>
#include <stack>
#include <utility>
using namespace std;

class MinStack {
    stack<pair<int, int>> st;

   public:
    MinStack() { st.emplace(0, INT_MAX); }

    void push(int val) { st.emplace(val, min(getMin(), val)); }

    void pop() { st.pop(); }

    int top() { return st.top().first; }

    int getMin() { return st.top().second; }
};

int main() {
    MinStack minStack;
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    cout << minStack.getMin() << endl;  // -3
    minStack.pop();
    cout << minStack.top() << endl;     // 0
    cout << minStack.getMin() << endl;  // -2
    return 0;
}

```

## 1381. Design a Stack With Increment Operation

-   [LeetCode](https://leetcode.com/problems/design-a-stack-with-increment-operation/) | [LeetCode CH](https://leetcode.cn/problems/design-a-stack-with-increment-operation/) (Medium)

-   Tags: array, stack, design

## 636. Exclusive Time of Functions

-   [LeetCode](https://leetcode.com/problems/exclusive-time-of-functions/) | [LeetCode CH](https://leetcode.cn/problems/exclusive-time-of-functions/) (Medium)

-   Tags: array, stack

## 2434. Using a Robot to Print the Lexicographically Smallest String

-   [LeetCode](https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/) | [LeetCode CH](https://leetcode.cn/problems/using-a-robot-to-print-the-lexicographically-smallest-string/) (Medium)

-   Tags: hash table, string, stack, greedy

## 895. Maximum Frequency Stack

-   [LeetCode](https://leetcode.com/problems/maximum-frequency-stack/) | [LeetCode CH](https://leetcode.cn/problems/maximum-frequency-stack/) (Hard)

-   Tags: hash table, stack, design, ordered set

## 1172. Dinner Plate Stacks

-   [LeetCode](https://leetcode.com/problems/dinner-plate-stacks/) | [LeetCode CH](https://leetcode.cn/problems/dinner-plate-stacks/) (Hard)

-   Tags: hash table, stack, design, heap priority queue

## 2589. Minimum Time to Complete All Tasks

-   [LeetCode](https://leetcode.com/problems/minimum-time-to-complete-all-tasks/) | [LeetCode CH](https://leetcode.cn/problems/minimum-time-to-complete-all-tasks/) (Hard)

-   Tags: array, binary search, stack, greedy, sorting

## 716. Max Stack

-   [LeetCode](https://leetcode.com/problems/max-stack/) | [LeetCode CH](https://leetcode.cn/problems/max-stack/) (Hard)

-   Tags: linked list, stack, design, doubly linked list, ordered set
