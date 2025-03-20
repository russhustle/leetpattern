---
comments: True
---

# N-ary Tree

## Table of Contents

- [ ] [1490. Clone N-ary Tree](https://leetcode.cn/problems/clone-n-ary-tree/) (Medium) 👑
- [ ] [1506. Find Root of N-Ary Tree](https://leetcode.cn/problems/find-root-of-n-ary-tree/) (Medium) 👑
- [x] [1522. Diameter of N-Ary Tree](https://leetcode.cn/problems/diameter-of-n-ary-tree/) (Medium) 👑

## 1490. Clone N-ary Tree

-   [LeetCode](https://leetcode.com/problems/clone-n-ary-tree/) | [LeetCode CH](https://leetcode.cn/problems/clone-n-ary-tree/) (Medium)

-   Tags: hash table, tree, depth first search, breadth first search

## 1506. Find Root of N-Ary Tree

-   [LeetCode](https://leetcode.com/problems/find-root-of-n-ary-tree/) | [LeetCode CH](https://leetcode.cn/problems/find-root-of-n-ary-tree/) (Medium)

-   Tags: hash table, bit manipulation, tree, depth first search

## 1522. Diameter of N-Ary Tree

-   [LeetCode](https://leetcode.com/problems/diameter-of-n-ary-tree/) | [LeetCode CH](https://leetcode.cn/problems/diameter-of-n-ary-tree/) (Medium)

-   Tags: tree, depth first search

```python title="1522. Diameter of N-Ary Tree - Python Solution"
from typing import List, Optional


class Node:
    def __init__(
        self,
        val: Optional[int] = None,
        children: Optional[List["Node"]] = None,
    ):
        self.val = val
        self.children = children if children is not None else []


def diameter(root: "Node") -> int:

    def dfs(node):
        if not node.children:
            return 1, 1
        mx0, mx1 = 0, 0
        mxf = 0
        for child in node.children:
            hl, fl = dfs(child)
            mxf = max(mxf, fl)
            if hl > mx1:
                if hl < mx0:
                    mx1 = hl
                else:
                    mx0, mx1 = hl, mx0
        return mx0 + 1, max(mxf, mx0 + mx1 + 1)

    return dfs(root)[1] - 1


root = [1, None, 2, None, 3, 4, None, 5, None, 6]
root = Node(1)
root.children = [Node(2)]
root.children[0].children = [Node(3), Node(4)]
root.children[0].children[0].children = [Node(5)]
root.children[0].children[1].children = [Node(6)]
print(diameter(root))  # 4

```
