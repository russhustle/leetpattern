from typing import Optional

from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node: Optional[TreeNode]) -> list[int, bool]:
            if not node:
                return [0, True]

            hl, bl = dfs(node.left)
            hr, br = dfs(node.right)

            height = 1 + max(hl, hr)
            balanced = bl and br and (abs(hl - hr) <= 1)

            return [height, balanced]

        return dfs(root)[1]


root = [3, 9, 20, None, None, 15, 7]
root = build(root)
print(root)
#   3___
#  /    \
# 9     _20
#      /   \
#     15    7
solution = Solution()
print(solution.isBalanced(root))  # True
