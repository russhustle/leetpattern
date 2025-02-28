from typing import Optional

from binarytree import build, Node as TreeNode


# BST
def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    inorder = []

    def dfs(node):
        if not node:
            return None

        dfs(node.left)
        nonlocal inorder
        inorder.append(node.val)
        dfs(node.right)

    dfs(root)

    return inorder[k - 1]


# |----------|------|-------|
# | Approach | Time | Space |
# |----------|------|-------|
# | DFS      | O(n) | O(n)  |
# |----------|------|-------|


root = build([3, 1, 4, None, 2])
k = 1
print(root)
#   __3
#  /   \
# 1     4
#  \
#   2
print(kthSmallest(root, k))  # 1
