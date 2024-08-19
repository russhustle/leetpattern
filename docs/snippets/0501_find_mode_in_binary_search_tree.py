from typing import List, Optional

from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findMode(root: Optional[TreeNode]) -> List[int]:
    hashmap = dict()

    def dfs(node):
        if not node:
            return None
        dfs(node.left)
        if node.val not in hashmap:
            hashmap[node.val] = 1
        else:
            hashmap[node.val] += 1
        dfs(node.right)

    dfs(root)
    max_counts = max(hashmap.values())
    result = []

    for key, value in hashmap.items():
        if value == max_counts:
            result.append(key)

    return result


root = [1, None, 2, None, None, 2]
root = build(root)
print(root)
# 1__
#    \
#     2
#    /
#   2
print(findMode(root))  # [2]
