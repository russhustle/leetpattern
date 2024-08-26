from typing import Optional

from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative
def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    stack = [root]
    sumLL = 0

    while stack:
        node = stack.pop()

        if node.left and not node.left.left and not node.left.right:
            sumLL += node.left.val

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return sumLL


# Left Leave None:
#   - node.left is not None
#   - node.left.left is None
#   - node.left.right is None

root = build([3, 9, 20, None, None, 15, 7])
print(root)
#   3___
#  /    \
# 9     _20
#      /   \
#     15    7
print(sumOfLeftLeaves(root))  # 24
