from typing import Optional

from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getMinimumDifference(root: Optional[TreeNode]) -> int:
    res = float("inf")
    pre = float("-inf")

    def dfs(node):  # inorder traversal
        if not node:
            return

        dfs(node.left)

        nonlocal res, pre
        res = min(res, node.val - pre)
        pre = node.val

        if res == 1:  # the minimum possible difference
            return

        dfs(node.right)

    dfs(root)

    return res


if __name__ == "__main__":
    root = [4, 2, 6, 1, 3]
    root = build(root)
    print(root)
    #     __4
    #    /   \
    #   2     6
    #  / \
    # 1   3
    assert getMinimumDifference(root) == 1
