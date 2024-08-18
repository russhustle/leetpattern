from typing import List, Optional
from binarytree import build
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        size = len(queue)

        for i in range(size):
            current = queue.popleft()

            # rightmost element
            if i == size - 1:
                result.append(current.val)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    return result


root = [1, 2, 2, 3, 4, None, 3, None, None, 5]
root = build(root)
print(root)
"""
    ____1
   /     \
  2__     2
 /   \     \
3     4     3
     /
    5
"""
print(rightSideView(root))  # [1, 2, 3, 5]
