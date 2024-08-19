from typing import Optional

from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: Optional[TreeNode]) -> bool:

    inorder = []  # inorder traversal of BST

    def dfs(node):
        if not node:
            return None
        dfs(node.left)
        inorder.append(node.val)
        dfs(node.right)

    dfs(root)

    for i in range(1, len(inorder)):
        if inorder[i] <= inorder[i - 1]:
            return False

    return True


root = [5, 1, 4, None, None, 3, 6]
root = build(root)
print(root)
#   5__
#  /   \
# 1     4
#      / \
#     3   6
print(isValidBST(root))  # False
