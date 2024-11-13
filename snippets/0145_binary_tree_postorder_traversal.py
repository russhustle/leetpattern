from typing import List, Optional

from binarytree import Node as TreeNode
from binarytree import build


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


tree = build([0, 1, 2, 3, 4, 5, 6])
print(tree)
#     __0__
#    /     \
#   1       2
#  / \     / \
# 3   4   5   6
print(postorderTraversalRecursive(tree))  # [3, 4, 1, 5, 6, 2, 0]
print(postorderTraversalIterative(tree))  # [3, 4, 1, 5, 6, 2, 0]
