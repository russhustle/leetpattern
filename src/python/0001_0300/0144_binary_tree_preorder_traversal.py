"""
![tree_traversal](../../assets/tree_traversal_dfs_bfs.png)

### Example 1

```mermaid
graph TD
A(( ))
B(( ))
C(( ))
D(( ))
E(( ))
F(( ))
G(( ))
A --- B
A --- E
B --- C
B --- D
E --- F
E --- G
```

Pre-order Traversal

```mermaid
graph TD
0((0))
1((1))
2((2))
3((3))
4((4))
5((5))
6((6))
0 --- 1
0 --- 4
1 --- 2
1 --- 3
4 --- 5
4 --- 6
```

In-order Traversal

```mermaid
graph TD
0((0))
1((1))
2((2))
3((3))
4((4))
5((5))
6((6))
3 --- 1
3 --- 5
1 --- 0
1 --- 2
5 --- 4
5 --- 6
```

Post-order Traversal

```mermaid
graph TD
0((0))
1((1))
2((2))
3((3))
4((4))
5((5))
6((6))
6 --- 2
6 --- 5
2 --- 0
2 --- 1
5 --- 3
5 --- 4
```

Level Order Traversal

```mermaid
graph TD
0((0))
1((1))
2((1))
3((2))
4((2))
5((2))
6((2))
0 --- 1
0 --- 2
1 --- 3
1 --- 4
2 --- 5
2 --- 6
```

### Example 2

```mermaid
graph TD
0((0))
1((1))
2((2))
3((3))
4((4))
5((5))
6((6))
0 --- 1
0 --- 2
1 --- 3
1 --- 4
2 --- 5
2 --- 6
```

| Traversal   | Order             | Method         | Result                        |
| ----------- | ----------------- | -------------- | ----------------------------- |
| Preorder    | Root, Left, Right | DFS or Stack   | `[0, 1, 3, 4, 2, 5, 6]`       |
| Inorder     | Left, Root, Right | DFS or Stack   | `[3, 1, 4, 0, 5, 2, 6]`       |
| Postorder   | Left, Right, Root | DFS or Stack   | `[3, 4, 1, 5, 6, 2, 0]`       |
| Level Order | Level by Level    | BFS with Queue | `[[0], [1, 2], [3, 4, 5, 6]]` |
"""

from typing import List, Optional

from binarytree import Node as TreeNode
from binarytree import build


# Recursive
def preorderTraversalRecursive(root: Optional[TreeNode]) -> List[int]:
    res = []

    def dfs(node):
        if not node:
            return None

        res.append(node.val)  # <--
        dfs(node.left)
        dfs(node.right)

    dfs(root)

    return res


# Iterative
def preorderTraversalIterative(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    stack = [root]
    res = []

    while stack:
        node = stack.pop()
        res.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return res


tree = build([0, 1, 2, 3, 4, 5, 6])
print(tree)
#     __0__
#    /     \
#   1       2
#  / \     / \
# 3   4   5   6
print(preorderTraversalRecursive(tree))  # [0, 1, 3, 4, 2, 5, 6]
print(preorderTraversalIterative(tree))  # [0, 1, 3, 4, 2, 5, 6]
