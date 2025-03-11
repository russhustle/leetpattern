---
comments: True
---

# Tree DP

- [ ] [337. House Robber III](https://leetcode.cn/problems/house-robber-iii/) (Medium)
- [x] [968. Binary Tree Cameras](https://leetcode.cn/problems/binary-tree-cameras/) (Hard)
- [ ] [2313. Minimum Flips in Binary Tree to Get Result](https://leetcode.cn/problems/minimum-flips-in-binary-tree-to-get-result/) (Hard) 👑

## 337. House Robber III

-   [LeetCode](https://leetcode.com/problems/house-robber-iii/) | [LeetCode CH](https://leetcode.cn/problems/house-robber-iii/) (Medium)

-   Tags: dynamic programming, tree, depth first search, binary tree

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

## 2313. Minimum Flips in Binary Tree to Get Result

-   [LeetCode](https://leetcode.com/problems/minimum-flips-in-binary-tree-to-get-result/) | [LeetCode CH](https://leetcode.cn/problems/minimum-flips-in-binary-tree-to-get-result/) (Hard)

-   Tags: dynamic programming, tree, depth first search, binary tree
