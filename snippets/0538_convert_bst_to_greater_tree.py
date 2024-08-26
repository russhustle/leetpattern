from typing import Optional

from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def convertBST(root: Optional[TreeNode]) -> Optional[TreeNode]:
    prev = 0

    def dfs(node):
        if not node:
            return None
        nonlocal prev

        dfs(node.right)

        node.val += prev
        prev = node.val

        dfs(node.left)

    dfs(root)

    return root


root = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
root = build(root)
print(root)
#     ____4__
#    /       \
#   1         6
#  / \       / \
# 0   2     5   7
#      \         \
#       3         8
greater_tree = convertBST(root)
print(greater_tree)
#      _______30___
#     /            \
#   _36            _21
#  /   \          /   \
# 36    35       26    15
#         \              \
#          33             8
