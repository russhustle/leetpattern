---
comments: True
---

# Binary Tree Level Order

## Table of Contents

- [x] [199. Binary Tree Right Side View](https://leetcode.cn/problems/binary-tree-right-side-view/) (Medium)
- [x] [637. Average of Levels in Binary Tree](https://leetcode.cn/problems/average-of-levels-in-binary-tree/) (Easy)
- [x] [102. Binary Tree Level Order Traversal](https://leetcode.cn/problems/binary-tree-level-order-traversal/) (Medium)
- [x] [103. Binary Tree Zigzag Level Order Traversal](https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/) (Medium)

## 199. Binary Tree Right Side View

-   [LeetCode](https://leetcode.com/problems/binary-tree-right-side-view/) | [LeetCode CH](https://leetcode.cn/problems/binary-tree-right-side-view/) (Medium)

-   Tags: tree, depth first search, breadth first search, binary tree
```python title="199. Binary Tree Right Side View - Python Solution"
from collections import deque
from typing import List, Optional

from binarytree import Node as TreeNode
from binarytree import build


# Binary Tree BFS
def rightSideViewBFS(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    q = deque([root])
    res = []

    while q:
        n = len(q)
        for i in range(n):
            node = q.popleft()
            if i == n - 1:
                res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return res


# Binary Tree DFS
def rightSideViewDFS(root: Optional[TreeNode]) -> List[int]:
    """后序遍历，先右后左，遇到的第一个节点就是该深度的最右侧节点"""
    ans = []

    def dfs(node, depth):
        if node is None:
            return
        if depth == len(ans):  # 这个深度首次遇到
            ans.append(node.val)

        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)

    dfs(root, 0)

    return ans


if __name__ == "__main__":
    root = [1, 2, 2, 3, 4, None, 3, None, None, 5]
    root = build(root)
    print(root)
    #     ____1
    #    /     \
    #   2__     2
    #  /   \     \
    # 3     4     3
    #      /
    #     5
    assert rightSideViewBFS(root) == [1, 2, 3, 5]
    assert rightSideViewDFS(root) == [1, 2, 3, 5]

```

## 637. Average of Levels in Binary Tree

-   [LeetCode](https://leetcode.com/problems/average-of-levels-in-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/average-of-levels-in-binary-tree/) (Easy)

-   Tags: tree, depth first search, breadth first search, binary tree
```python title="637. Average of Levels in Binary Tree - Python Solution"
from collections import deque
from typing import List, Optional

from binarytree import Node as TreeNode
from binarytree import build


# Binary Tree BFS
def averageOfLevels(root: Optional[TreeNode]) -> List[float]:
    if not root:
        return []

    q = deque([root])
    res = []

    while q:
        n = len(q)
        level = 0
        for _ in range(n):
            cur = q.popleft()
            level += cur.val

            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        res.append(float(level / n))

    return res


if __name__ == "__main__":
    root = [3, 9, 20, None, None, 15, 7]
    root = build(root)
    print(root)
    #   3___
    #  /    \
    # 9     _20
    #      /   \
    #     15    7
    assert averageOfLevels(root) == [3.00000, 14.50000, 11.00000]

```

## 102. Binary Tree Level Order Traversal

-   [LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [LeetCode CH](https://leetcode.cn/problems/binary-tree-level-order-traversal/) (Medium)

-   Tags: tree, breadth first search, binary tree
```python title="102. Binary Tree Level Order Traversal - Python Solution"
from collections import deque
from typing import List, Optional

from binarytree import Node as TreeNode
from binarytree import build


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    q = deque([root])
    res = []

    while q:
        level = []
        size = len(q)

        for _ in range(size):
            cur = q.popleft()
            level.append(cur.val)

            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        res.append(level)

    return res


tree = build([3, 9, 20, None, None, 15, 7])
print(tree)
#   3___
#  /    \
# 9     _20
#      /   \
#     15    7
print(levelOrder(tree))  # [[3], [9, 20], [15, 7]]

```

## 103. Binary Tree Zigzag Level Order Traversal

-   [LeetCode](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) | [LeetCode CH](https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/) (Medium)

-   Tags: tree, breadth first search, binary tree
```python title="103. Binary Tree Zigzag Level Order Traversal - Python Solution"
from collections import deque
from typing import List, Optional

from binarytree import Node as TreeNode
from binarytree import build


def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    q = deque([root])
    res = []

    while q:
        level = []
        n = len(q)

        for _ in range(n):
            cur = q.popleft()
            level.append(cur.val)

            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        res.append(level if len(res) % 2 == 0 else level[::-1])

    return res


tree = build([3, 9, 20, None, None, 15, 7])
print(tree)
#   3___
#  /    \
# 9     _20
#      /   \
#     15    7
print(zigzagLevelOrder(tree))  # [[3], [20, 9], [15, 7]]

```
