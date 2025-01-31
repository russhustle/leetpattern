from typing import Optional

from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. Recursive
def searchBSTRecursive(
    root: Optional[TreeNode], val: int
) -> Optional[TreeNode]:
    if not root:
        return None

    if root.val > val:
        return searchBSTRecursive(root.left, val)

    elif root.val < val:
        return searchBSTRecursive(root.right, val)

    else:
        return root


# 2. Iterative
def searchBSTIterative(
    root: Optional[TreeNode], val: int
) -> Optional[TreeNode]:
    while root:
        if root.val > val:
            root = root.left
        elif root.val < val:
            root = root.right
        else:
            return root
    return None


root = [4, 2, 7, 1, 3]
val = 2
root = build(root)
print(root)
#     __4
#    /   \
#   2     7
#  / \
# 1   3
print(searchBSTRecursive(root, val))
#   2
#  / \
# 1   3
print(searchBSTIterative(root, val))
#   2
#  / \
# 1   3
