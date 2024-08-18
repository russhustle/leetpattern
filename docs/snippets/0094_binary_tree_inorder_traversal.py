from typing import List, Optional
from binarytree import build
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


tree = build([1, None, 2, None, None, 3])
print(tree)
# 1__
#    \
#     2
#    /
#   3
print(inorderTraversalRecursive(tree))  # [1, 3, 2]
print(inorderTraversalIterative(tree))  # [1, 3, 2]
