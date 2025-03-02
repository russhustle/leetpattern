from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# Tree DFS
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)

        dfs(root)

        return self.diameter


root = build([1, 2, 3, 4, 5])
print(root)
#     __1
#    /   \
#   2     3
#  / \
# 4   5
obj = Solution()
print(obj.diameterOfBinaryTree(root))  # 3
