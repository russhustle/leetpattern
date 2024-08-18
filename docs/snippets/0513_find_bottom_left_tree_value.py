from typing import Optional
from binarytree import build
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findBottomLeftValue(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    queue = deque([root])
    result = 0

    while queue:
        size = len(queue)

        for i in range(size):
            node = queue.popleft()
            if i == 0:
                result = node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

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

print(findBottomLeftValue(root))  # 5
