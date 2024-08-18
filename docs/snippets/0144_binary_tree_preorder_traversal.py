from typing import List, Optional
from binarytree import build
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive
def preorderTraversalRecursive(root: Optional[TreeNode]) -> List[int]:
    preorder = []

    def dfs(node):
        if not node:
            return None

        preorder.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)

    return preorder


# Iterative
def preorderTraversalIterative(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    stack = [root]
    preorder = []

    while stack:
        node = stack.pop()
        preorder.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return preorder


tree = build([1, None, 2, None, None, 3])
print(tree)
# 1__
#    \
#     2
#    /
#   3
print(preorderTraversalRecursive(tree))  # [1, 2, 3]
print(preorderTraversalIterative(tree))  # [1, 2, 3]
