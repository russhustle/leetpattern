from collections import defaultdict
from typing import List, Optional

from binarytree import Node as TreeNode
from binarytree import build


def findLeaves(root: Optional[TreeNode]) -> List[List[int]]:
    depths = defaultdict(list)

    def dfs(node):
        if not node:
            return 0
        l, r = dfs(node.left), dfs(node.right)
        depth = 1 + max(l, r)
        depths[depth].append(node.val)
        return depth

    dfs(root)
    return [i for i in depths.values()]


if __name__ == "__main__":
    root = build([1, 2, 3, 4, 5])
    print(root)
    #     __1
    #    /   \
    #   2     3
    #  / \
    # 4   5
    print(findLeaves(root))  # [[4, 5, 3], [2], [1]]
