from typing import List, Optional

from binarytree import Node as TreeNode
from binarytree import build


# Binary Tree Traversal
def getLonelyNodes(root: Optional[TreeNode]) -> List[int]:
    res = []

    def dfs(node):
        if not node:
            return False

        left = dfs(node.left)
        right = dfs(node.right)
        if left and not right:
            res.append(node.left.val)
        if not left and right:
            res.append(node.right.val)

        return True

    dfs(root)

    return res


if __name__ == "__main__":
    root = build([1, 2, 3, None, 4])
    print(root)
    #    __1
    #  /   \
    # 2     3
    #  \
    #   4
    assert getLonelyNodes(root) == [4]

    root = build([7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2])
    print(root)
    #     7____
    #    /     \
    #   1     __4
    #  /     /   \
    # 6     5     3
    #        \
    #         2
    assert getLonelyNodes(root) == [6, 2]
