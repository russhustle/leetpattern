from typing import List, Optional
from binarytree import build
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative
def minDepthIterative(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    queue = deque([root])
    depth = 0

    while queue:
        depth += 1

        for _ in range(len(queue)):
            node = queue.popleft()

            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


# Recursive
def minDepthRecursive(root):
    if root is None:
        return 0

    if root.left is None and root.right is not None:
        return 1 + minDepthRecursive(root.right)
    if root.left is not None and root.right is None:
        return 1 + minDepthRecursive(root.left)

    return 1 + min(minDepthRecursive(root.left), minDepthRecursive(root.right))


root = [1, 2, 2, 3, 4, None, None, None, None, 5]
root = build(root)
print(root)
"""
    ____1
   /     \
  2__     2
 /   \
3     4
     /
    5

"""
print(minDepthIterative(root))  # 2
print(minDepthRecursive(root))  # 2
