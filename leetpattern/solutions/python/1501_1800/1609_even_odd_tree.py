from collections import deque
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


def isEvenOddTree(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    q = deque([root])
    level = 0

    while q:
        size = len(q)
        prev = None

        for _ in range(size):
            node = q.popleft()

            if level % 2 == 0:
                if node.val % 2 == 0:
                    return False
                if prev and node.val <= prev:
                    return False
            else:
                if node.val % 2 == 1:
                    return False
                if prev and node.val >= prev:
                    return False

            prev = node.val

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        level += 1

    return True


if __name__ == "__main__":
    root = build([5, 4, 2, 3, 3, 7])
    print(root)
    #     __5__
    #    /     \
    #   4       2
    #  / \     /
    # 3   3   7
    assert isEvenOddTree(root) is False
