from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# Tree
def leafSimilar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

    def dfs(node, leaf):
        if not node:
            return
        if not node.left and not node.right:
            leaf.append(node.val)
        dfs(node.left, leaf)
        dfs(node.right, leaf)

    leaf1, leaf2 = [], []
    dfs(root1, leaf1)
    dfs(root2, leaf2)

    return leaf1 == leaf2


root1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
root2 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
root1 = build(root1)

root2 = build(root2)
print(root1)
#     ______3__
#    /         \
#   5__         1
#  /   \       / \
# 6     2     9   8
#      / \
#     7   4
print(root2)
#     __3__
#    /     \
#   5       1__
#  / \     /   \
# 6   7   4     2
#              / \
#             9   8
print(leafSimilar(root1, root2))  # True
