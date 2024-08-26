from typing import List, Optional

from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive
def binaryTreePaths(root: Optional[TreeNode]) -> List[str]:
    if not root:
        return []

    path = []
    paths = []

    def dfs(node, path):
        if not node:
            return None

        path.append(str(node.val))

        if not node.left and not node.right:
            paths.append("->".join(path))

        dfs(node.left, path[:])
        dfs(node.right, path[:])

    dfs(root, path)

    return paths


root = build([1, 2, 3, None, 5])
print(root)
#   __1
#  /   \
# 2     3
#  \
#   5
print(binaryTreePaths(root))  # ['1->2->5', '1->3']
