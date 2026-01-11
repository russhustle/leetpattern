from typing import Optional

from binarytree import Node as TreeNode


class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        LCA = self.find_LCA(root, p, q)  # Least Common Ancestor

        p_dep = self.dfs(LCA, p)
        q_dep = self.dfs(LCA, q)
        return p_dep + q_dep

    def dfs(self, root: TreeNode, target: int) -> int:
        """Depth of target node from node"""
        if not root:
            return -1
        if root.val == target:
            return 0
        L = self.dfs(root.left, target)
        R = self.dfs(root.right, target)

        if L == -1 and R == -1:
            return -1
        return max(L, R) + 1

    def find_LCA(self, root: TreeNode, p: int, q: int) -> TreeNode:
        if not root or root.val == p or root.val == q:
            return root
        L = self.find_LCA(root.left, p, q)
        R = self.find_LCA(root.right, p, q)
        if L and R:
            return root
        elif L and not R:
            return L
        elif not L and R:
            return R
        else:
            return None
