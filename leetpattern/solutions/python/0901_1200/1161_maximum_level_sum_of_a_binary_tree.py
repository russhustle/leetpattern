from collections import deque
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# BFS
def maxLevelSum(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    q = deque([root])
    res = 0
    maxSum = float("-inf")
    level = 1

    while q:
        n = len(q)
        curSum = 0

        for _ in range(n):
            node = q.popleft()
            curSum += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        if curSum > maxSum:
            maxSum = curSum
            res = level
        level += 1

    return res


root = [1, 7, 0, 7, -8, None, None]
root = build(root)
print(root)
#     ___1
#    /    \
#   7      0
#  / \
# 7   -8
print(maxLevelSum(root))  # 2
