from typing import List, Optional
from binarytree import build
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive
def postorderTraversalRecursive(root: Optional[TreeNode]) -> List[int]:
    postorder = []

    def dfs(node):
        if not node:
            return

        dfs(node.left)
        dfs(node.right)
        postorder.append(node.val)

    dfs(root)

    return postorder


# Iterative
def postorderTraversalIterative(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    postorder = []
    stack = [root]

    while stack:
        node = stack.pop()
        postorder.append(node.val)

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return postorder[::-1]


tree = build([1, None, 2, None, None, 3])
print(tree)
# 1__
#    \
#     2
#    /
#   3
print(postorderTraversalRecursive(tree))  # [3, 2, 1]
print(postorderTraversalIterative(tree))  # [3, 2, 1]
