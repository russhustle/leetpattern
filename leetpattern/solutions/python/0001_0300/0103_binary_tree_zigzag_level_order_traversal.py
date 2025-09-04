from collections import deque
from typing import List, Optional

from binarytree import Node as TreeNode
from binarytree import build


def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    q = deque([root])
    res = []

    while q:
        level = []
        size = len(q)

        for _ in range(size):
            cur = q.popleft()
            level.append(cur.val)

            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        res.append(level if not len(res) % 2 else level[::-1])

    return res


if __name__ == "__main__":
    tree = build([3, 9, 20, None, None, 15, 7])
    print(tree)
    #   3___
    #  /    \
    # 9     _20
    #      /   \
    #     15    7
    assert zigzagLevelOrder(tree) == [[3], [20, 9], [15, 7]]
