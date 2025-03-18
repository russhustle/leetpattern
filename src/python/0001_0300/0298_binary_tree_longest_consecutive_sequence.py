from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# Binary Tree
def longestConsecutive(root: Optional[TreeNode]) -> int:
    res = 0

    def dfs(node):
        if not node:
            return 0

        left, right = dfs(node.left), dfs(node.right)
        cur = 1
        if node.left and node.left.val == (node.val + 1):
            cur = max(cur, left + 1)
        if node.right and node.right.val == (node.val + 1):
            cur = max(cur, right + 1)

        nonlocal res
        res = max(res, cur)
        return cur

    dfs(root)

    return res


if __name__ == "__main__":
    root = build([1, 3, 2, 4, None, None, None, 5])
    print(root)
    #       1
    #      / \
    #     3   2
    #    /
    #   4
    #  /
    # 5
    print(longestConsecutive(root))  # 3
