from typing import Optional

from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive
def evaluateTree(root: Optional[TreeNode]) -> bool:
    if not root.left and not root.right:
        return root.val

    left = evaluateTree(root.left)
    right = evaluateTree(root.right)

    if root.val == 2:
        return left or right
    elif root.val == 3:
        return left and right


root = build([2, 1, 3, None, None, 0, 1])
print(root)
#   2__
#  /   \
# 1     3
#      / \
#     0   1
boolTree = build(["OR", "True", "AND", None, None, "False", "True"])
print(boolTree)
#    __OR_______
#   /           \
# True        __AND_
#            /      \
#         False     True
print(evaluateTree(root))  # 1
