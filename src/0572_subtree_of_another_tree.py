from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# DFS - Tree
def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def isSameTree(p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

    if not root:
        return False

    return (
        isSameTree(root, subRoot)
        or isSubtree(root.left, subRoot)
        or isSubtree(root.right, subRoot)
    )


# |------------|---------|----------|
# | Approach   | Time    | Space    |
# |------------|---------|----------|
# | DFS        | O(n * m)| O(n)     |
# |------------|---------|----------|


root = build([3, 4, 5, 1, 2, None, None, None, None, 0])
subRoot = build([4, 1, 2])
print(root)
#     ____3
#    /     \
#   4__     5
#  /   \
# 1     2
#      /
#     0
print(subRoot)
#   4
#  / \
# 1   2
print(isSubtree(root, subRoot))  # False
