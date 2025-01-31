from collections import deque
from typing import List

from binarytree import build

from helper import TreeNode


# BFS
def distanceK(root: TreeNode, target: TreeNode, k: int) -> List[int]:
    parent = dict()

    def dfs(node, par=None):
        if node:
            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)

    dfs(root)

    q = deque([(target, 0)])
    seen = set([target])

    while q:
        node, dist = q.popleft()

        if dist == k:
            return [node.val] + [node.val for node, _ in q]

        for nei in (node.left, node.right, parent[node]):
            if nei and nei not in seen:
                seen.add(nei)
                q.append((nei, dist + 1))

    return []


root = build([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
print(root)
#     ______3__
#    /         \
#   5__         1
#  /   \       / \
# 6     2     0   8
#      / \
#     7   4
target = root.left
k = 2
print(distanceK(root, target, k))  # [7, 4, 1]
