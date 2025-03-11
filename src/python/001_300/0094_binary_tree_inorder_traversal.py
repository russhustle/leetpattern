from typing import List, Optional

from binarytree import Node as TreeNode
from binarytree import build


# Recursive
def inorderTraversalRecursive(root: TreeNode) -> List[int]:
    res = []

    def dfs(node):
        if not node:
            return

        dfs(node.left)
        res.append(node.val)  # <--
        dfs(node.right)

    dfs(root)

    return res


# Iterative
def inorderTraversalIterative(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    stack = []
    res = []
    cur = root

    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right

    return res


tree = build([0, 1, 2, 3, 4, 5, 6])
print(tree)
#     __0__
#    /     \
#   1       2
#  / \     / \
# 3   4   5   6
print(inorderTraversalRecursive(tree))  # [3, 1, 4, 0, 5, 2, 6]
print(inorderTraversalIterative(tree))  # [3, 1, 4, 0, 5, 2, 6]
