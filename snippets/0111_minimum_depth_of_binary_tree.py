from collections import deque
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# Iterative
def minDepthIterative(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    q = deque([root])
    res = 0

    while q:
        res += 1

        for _ in range(len(q)):
            node = q.popleft()

            if not node.left and not node.right:
                return res

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


# Recursive
def minDepthRecursive(root: Optional[TreeNode]) -> int:
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
