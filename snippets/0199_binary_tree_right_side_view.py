from collections import deque
from typing import List, Optional

from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    q = deque([root])
    right = []

    while q:
        n = len(q)

        for i in range(n):
            cur = q.popleft()

            # rightmost element
            if i == n - 1:
                right.append(cur.val)

            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

    return right


root = [1, 2, 2, 3, 4, None, 3, None, None, 5]
root = build(root)
print(root)
#     ____1
#    /     \
#   2__     2
#  /   \     \
# 3     4     3
#      /
#     5
print(rightSideView(root))  # [1, 2, 3, 5]
