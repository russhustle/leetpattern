from typing import List, Optional
from binarytree import build
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrderBottom(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    levels = []
    queue = deque([root])

    while queue:
        level = []
        n = len(queue)

        for _ in range(n):
            current = queue.popleft()
            level.append(current.val)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        levels.append(level)

    return levels[::-1]


tree = build([3, 9, 20, None, None, 15, 7])
print(tree)
#   3___
#  /    \
# 9     _20
#      /   \
#     15    7
print(levelOrderBottom(tree))  # [[15, 7], [9, 20], [3]]
