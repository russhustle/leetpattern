from typing import Optional
from binarytree import Node as TreeNode


class GetDirections:
    def lca(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        path_s, path_t = [], []

        def dfs(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True

            path.append("L")
            if dfs(node.left, target, path):
                return True
            path.pop()

            path.append("R")
            if dfs(node.right, target, path):
                return True
            path.pop()

            return False

        dfs(root, startValue, path_s)
        dfs(root, destValue, path_t)

        i = 0
        while i < len(path_s) and i < len(path_t) and path_s[i] == path_t[i]:
            i += 1

        UP = "U" * (len(path_s) - i)
        DOWN = "".join(path_t[i:])
        return UP + DOWN
