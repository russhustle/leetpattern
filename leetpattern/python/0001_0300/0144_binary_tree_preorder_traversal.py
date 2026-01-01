from typing import List, Optional

from binarytree import Node as TreeNode
from binarytree import build


class PreorderTraversal:
    def recursive(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return None

            res.append(node.val)  # <--
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return res

    def iterative(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res


if __name__ == "__main__":
    tree = build([0, 1, 2, 3, 4, 5, 6])
    print(tree)
    #     __0__
    #    /     \
    #   1       2
    #  / \     / \
    # 3   4   5   6
    sol = PreorderTraversal()
    assert sol.recursive(tree) == [0, 1, 3, 4, 2, 5, 6]
    assert sol.iterative(tree) == [0, 1, 3, 4, 2, 5, 6]
