from collections import deque
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# Recursive
def countNodesRecursive(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    num = 1 + countNodesRecursive(root.left) + countNodesRecursive(root.right)

    return num


# Iterative
def countNodesIterative(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    q = deque([root])
    count = 0

    while q:
        n = len(q)

        for _ in range(n):
            node = q.popleft()
            count += 1

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return count


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# | Recursive  |  O(n)  |  O(n)   |
# | Iterative  |  O(n)  |  O(n)   |
# |------------|--------|---------|

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
