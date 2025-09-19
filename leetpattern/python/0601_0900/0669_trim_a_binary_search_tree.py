from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def trimBST(root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
    if root is None:
        return None

    if root.val < low:
        return trimBST(root.right, low, high)
    if root.val > high:
        return trimBST(root.left, low, high)

    root.left = trimBST(root.left, low, high)
    root.right = trimBST(root.right, low, high)

    return root


root = TreeNode(3)
root.left = TreeNode(0)
root.right = TreeNode(4)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(1)
#     __3
#    /   \
#   0     4
#    \
#     2
#    /
#   1

trimBST(root, 1, 3)
#     __3
#    /
#   2
#  /
# 1
