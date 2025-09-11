from itertools import pairwise
from math import inf
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


def isValidBST1(root: Optional[TreeNode]) -> bool:
    inorder = []  # inorder traversal

    def dfs(node):
        if not node:
            return None
        dfs(node.left)
        inorder.append(node.val)
        dfs(node.right)

    dfs(root)

    for a, b in pairwise(inorder):
        if a >= b:
            return False

    return True


def isValidBST2(root: Optional[TreeNode]) -> bool:
    if not root:
        return True
    pre = -inf

    def dfs(node):
        if not node:
            return True
        if not dfs(node.left):
            return False

        nonlocal pre
        if node.val <= pre:
            return False
        pre = node.val

        return dfs(node.right)

    return dfs(root)


if __name__ == "__main__":
    root = [5, 1, 4, None, None, 3, 6]
    root = build(root)
    print(root)
    #   5__
    #  /   \
    # 1     4
    #      / \
    #     3   6
    assert not isValidBST1(root)  # [1, 5, 3, 4, 6]
    assert not isValidBST2(root)  # [1, 5, 3, 4, 6]
