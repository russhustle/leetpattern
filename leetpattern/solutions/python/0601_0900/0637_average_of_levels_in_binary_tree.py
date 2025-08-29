from collections import deque
from typing import List, Optional

from binarytree import Node as TreeNode
from binarytree import build


# Binary Tree BFS
def averageOfLevels(root: Optional[TreeNode]) -> List[float]:
    if not root:
        return []

    q = deque([root])
    res = []

    while q:
        n = len(q)
        level = 0
        for _ in range(n):
            cur = q.popleft()
            level += cur.val

            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        res.append(float(level / n))

    return res


if __name__ == "__main__":
    root = [3, 9, 20, None, None, 15, 7]
    root = build(root)
    print(root)
    #   3___
    #  /    \
    # 9     _20
    #      /   \
    #     15    7
    assert averageOfLevels(root) == [3.00000, 14.50000, 11.00000]
