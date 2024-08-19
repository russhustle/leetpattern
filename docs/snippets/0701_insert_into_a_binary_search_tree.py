from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertIntoBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root is None:
        return TreeNode(val)

    if root.val > val:
        root.left = insertIntoBST(root.left, val)
    if root.val < val:
        root.right = insertIntoBST(root.right, val)

    return root


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
#     __4
#    /   \
#   2     6
#  / \
# 1   3

insertIntoBST(root, 5)
#     __4
#    /   \
#   2     6
#  / \   /
# 1   3 5
