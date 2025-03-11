from collections import deque
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# BFS
def kthLargestLevelSum(root: Optional[TreeNode], k: int) -> int:
    if not root:
        return 0
    sums = []
    q = deque([root])

    while q:
        size = len(q)
        level = 0
        for _ in range(size):
            node = q.popleft()
            level += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        sums.append(level)

    if len(sums) < k:
        return -1

    sums.sort()
    return sums[-k]


root = [5, 8, 9, 2, 1, 3, 7, 4, 6]
root = build(root)
k = 2
print(kthLargestLevelSum(root, k))  # 13
