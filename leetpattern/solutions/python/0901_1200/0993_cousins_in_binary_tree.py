from collections import deque
from math import inf
from typing import Optional

from binarytree import build, Node as TreeNode


def is_cousins_bfs(root: Optional[TreeNode], x: int, y: int) -> bool:
    if not root:
        return False

    q = deque([(root, inf)])

    while q:
        size = len(q)
        p1, p2 = None, None

        for _ in range(size):
            cur, par = q.popleft()
            val = cur.val
            if x == val:
                p1 = par
            if y == val:
                p2 = par

            if cur.left:
                q.append((cur.left, val))
            if cur.right:
                q.append((cur.right, val))

        # Check if both found at same level
        if p1 and p2:
            return p1 != p2  # Same level, different parents
        elif p1 or p2:
            return False  # Only one found at this level

    return False


if __name__ == "__main__":
    root = build([1, 2, 3, None, 4, None, 5])
    assert is_cousins_bfs(root, 5, 4)
    root = build([1, 2, 3, None, 4])
    assert not is_cousins_bfs(root, 2, 3)
    root = build([1, 2, 3, 4])
    assert not is_cousins_bfs(root, 4, 3)
