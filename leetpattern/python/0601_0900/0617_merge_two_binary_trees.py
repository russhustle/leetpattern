from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mergeTrees(
    root1: Optional[TreeNode], root2: Optional[TreeNode]
) -> Optional[TreeNode]:

    if not root1:
        return root2
    if not root2:
        return root1

    root = TreeNode()

    root.val += root1.val + root2.val
    root.left = mergeTrees(root1.left, root2.left)
    root.right = mergeTrees(root1.right, root2.right)

    return root


root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)
#     1
#    / \
#   3   2
#  /
# 5

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)
#     2
#    / \
#   1   3
#    \   \
#     4   7

root = mergeTrees(root1, root2)
#     3
#    / \
#   4   5
#  / \   \
# 5   4   7
