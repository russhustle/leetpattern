from collections import deque
from typing import Optional

from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. Recursive
def countNodesRecursive(root: Optional[TreeNode]) -> int:
    # TC: O(n)
    # SC: O(n)
    if not root:
        return 0

    nodeNum = (
        countNodesRecursive(root.left) + countNodesRecursive(root.right) + 1
    )

    return nodeNum


# 2. Iterative
def countNodesIterative(root: Optional[TreeNode]) -> int:
    # TC: O(n)
    # SC: O(n)

    if not root:
        return 0

    q = deque([root])
    nodeNum = 0

    while q:
        n = len(q)

        for _ in range(n):
            node = q.popleft()
            nodeNum += 1

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return nodeNum


root = [1, 2, 3, 4, 5, 6]
root = build(root)
print(root)
#     __1__
#    /     \
#   2       3
#  / \     /
# 4   5   6
print(countNodesRecursive(root))  # 6
print(countNodesIterative(root))  # 6
