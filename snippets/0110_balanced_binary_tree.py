from typing import Optional

from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive
def isBalanced(root: Optional[TreeNode]) -> bool:
    def getHeight(node):
        if not node:
            return 0

        # post order
        leftHeight = getHeight(node.left)
        rightHeight = getHeight(node.right)

        if leftHeight == -1 or rightHeight == -1:
            return -1

        if abs(leftHeight - rightHeight) > 1:
            return -1
        else:
            return 1 + max(leftHeight, rightHeight)

    if getHeight(root) != -1:
        return True
    else:
        return False


root = [3, 9, 20, None, None, 15, 7]
root = build(root)
print(root)
#   3___
#  /    \
# 9     _20
#      /   \
#     15    7
print(isBalanced(root))  # True
