---
comments: True
---

# Tree DP Minimum Dominating Set

## Table of Contents

- [x] [968. Binary Tree Cameras](https://leetcode.cn/problems/binary-tree-cameras/) (Hard)

## 968. Binary Tree Cameras

-   [LeetCode](https://leetcode.com/problems/binary-tree-cameras/) | [LeetCode CH](https://leetcode.cn/problems/binary-tree-cameras/) (Hard)

-   Tags: dynamic programming, tree, depth first search, binary tree
```python title="968. Binary Tree Cameras - Python Solution"
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


def minCameraCover(root: Optional[TreeNode]) -> int:
    res = 0

    def dfs(node, hasParent):
        if not node:
            return -1

        nonlocal res
        left, right = dfs(node.left, True), dfs(node.right, True)

        if left == -1 and right == -1:
            if hasParent:
                return 0
            res += 1
            return 2
        if left == 0 or right == 0:
            res += 1
            return 2
        if left == 2 or right == 2:
            return 1
        if hasParent:
            return 0
        res += 1
        return 2

    dfs(root, False)

    return res


root = build([0, 0, None, 0, 0])
print(root)
print(minCameraCover(root))  # 1

```

