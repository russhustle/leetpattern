from typing import Optional

from binarytree import build

from helper import TreeNode


# Tree DFS
def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    diameter = 0

    def dfs(node):
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        nonlocal diameter
        diameter = max(diameter, left + right)

        return 1 + max(left, right)

    dfs(root)
    return diameter


# |------------|---------|----------|
# | Approach   | Time    | Space    |
# |------------|---------|----------|
# | DFS        | O(n)    | O(n)     |
# |------------|---------|----------|


root = build([1, 2, 3, 4, 5])
print(root)
#     __1
#    /   \
#   2     3
#  / \
# 4   5
print(diameterOfBinaryTree(root))  # 3
