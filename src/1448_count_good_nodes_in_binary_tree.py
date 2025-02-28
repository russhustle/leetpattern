from typing import List

from binarytree import build, Node as TreeNode



# Tree
def goodNodes(root: TreeNode) -> int:
    def dfs(node, max_val):
        if not node:
            return 0

        good = 1 if node.val >= max_val else 0

        max_val = max(max_val, node.val)

        good += dfs(node.left, max_val)
        good += dfs(node.right, max_val)

        return good

    return dfs(root, root.val)


root = build([3, 1, 4, 3, None, 1, 5])
print(root)
#     3__
#    /   \
#   1     4
#  /     / \
# 3     1   5
print(goodNodes(root))  # 4
