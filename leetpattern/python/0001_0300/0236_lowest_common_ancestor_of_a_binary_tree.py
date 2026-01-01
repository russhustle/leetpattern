from typing import List, Optional

from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class LowestCommonAncestor:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root or q == root or p == root:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right


if __name__ == "__main__":
    root = build([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print(root)
    #     ______3__
    #    /         \
    #   5__         1
    #  /   \       / \
    # 6     2     0   8
    #      / \
    #     7   4
    p = root.left  # 5
    q = root.right  # 1
    sol = LowestCommonAncestor()
    print(sol.lowestCommonAncestor(root, p, q))
    #     ______3__
    #    /         \
    #   5__         1
    #  /   \       / \
    # 6     2     0   8
    #      / \
    #     7   4
