from collections import deque
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# BFS
def deepestLeavesSum(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    q = deque([root])

    while q:
        n = len(q)
        res = 0
        for _ in range(n):
            node = q.popleft()
            res += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return res


root = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, None, 8]
root = build(root)
print(root)
#       __1
#      /   \
#     2     3__
#    / \       \
#   4   5       6
#  /           /
# 7           8
print(deepestLeavesSum(root))  # 15
