from typing import List, Optional

from binarytree import Node as TreeNode
from binarytree import build


# Recursive
def binaryTreePaths(root: Optional[TreeNode]) -> List[str]:
    res = []

    def dfs(node, path):
        if not node:
            return
        path += str(node.val)

        if not node.left and not node.right:
            res.append(path)
            return

        path += "->"

        dfs(node.left, path)
        dfs(node.right, path)

    dfs(root, "")

    return res


root = build([1, 2, 3, None, 5])
print(root)
#   __1
#  /   \
# 2     3
#  \
#   5
print(binaryTreePaths(root))  # ['1->2->5', '1->3']
