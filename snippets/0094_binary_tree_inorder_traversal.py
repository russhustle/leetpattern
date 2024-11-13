from typing import List, Optional

from binarytree import Node as TreeNode
from binarytree import build


# Recursive
def inorderTraversalRecursive(root: TreeNode) -> List[int]:
    inorder = []

    def dfs(node):
        if not node:
            return

        dfs(node.left)
        inorder.append(node.val)
        dfs(node.right)

    dfs(root)

    return inorder


# Iterative
def inorderTraversalIterative(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    stack = []
    inorder = []
    current = root

    while current or stack:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            inorder.append(current.val)
            current = current.right

    return inorder


tree = build([0, 1, 2, 3, 4, 5, 6])
print(tree)
#     __0__
#    /     \
#   1       2
#  / \     / \
# 3   4   5   6
print(inorderTraversalRecursive(tree))  # [3, 1, 4, 0, 5, 2, 6]
print(inorderTraversalIterative(tree))  # [3, 1, 4, 0, 5, 2, 6]
