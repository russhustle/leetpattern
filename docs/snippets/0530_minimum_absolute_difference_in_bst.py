from typing import Optional

from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getMinimumDifference(root: Optional[TreeNode]) -> int:

    inorder = []
    result = float("inf")

    def dfs(node):
        if not node:
            return None
        dfs(node.left)
        inorder.append(node.val)
        dfs(node.right)

    dfs(root)

    for i in range(1, len(inorder)):
        result = min(result, abs(inorder[i] - inorder[i - 1]))

    return result


root = [4, 2, 6, 1, 3]
root = build(root)
print(root)
#     __4
#    /   \
#   2     6
#  / \
# 1   3
print(getMinimumDifference(root))  # 1
