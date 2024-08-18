from typing import Optional, List
from binarytree import build
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def largestValues(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        levelMax = float("-inf")
        for _ in range(len(queue)):
            node = queue.popleft()

            levelMax = max(levelMax, node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(levelMax)

    return result


root = [1, 2, 2, 3, 4, None, None, None, None, 5]
root = build(root)
print(root)
#     ____1
#    /     \
#   2__     2
#  /   \
# 3     4
#      /
#     5
print(largestValues(root))  # [1, 2, 4, 5]
