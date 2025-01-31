from typing import Optional

from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive
def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False

    if not root.left and not root.right:
        return root.val == targetSum

    targetSum -= root.val

    return hasPathSum(root.left, targetSum) or hasPathSum(
        root.right, targetSum
    )


root = build([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1])
print(root)
#          5___
#         /    \
#     ___4     _8
#    /        /  \
#   11       13   4
#  /  \            \
# 7    2            1
print(hasPathSum(root, 22))  # True
