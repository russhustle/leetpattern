from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# Lowest Common Ancestor
def lcaDeepestLeaves(root: Optional[TreeNode]) -> Optional[TreeNode]:
    res = None
    max_depth = -1

    def dfs(node, depth) -> int:
        nonlocal res, max_depth
        if not node:
            max_depth = max(max_depth, depth)
            return depth
        left_max_depth = dfs(node.left, depth + 1)
        right_max_depth = dfs(node.right, depth + 1)
        if left_max_depth == right_max_depth == max_depth:
            res = node
        return max(left_max_depth, right_max_depth)

    dfs(root, 0)
    return res


if __name__ == "__main__":
    root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root = build(root)
    print(root)
    #     ______3__
    #    /         \
    #   5__         1
    #  /   \       / \
    # 6     2     0   8
    #      / \
    #     7   4
    print(lcaDeepestLeaves(root))  # 2
    #   2
    #  / \
    # 7   4
