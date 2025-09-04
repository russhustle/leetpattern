from collections import deque
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# Recursive
def is_symmetric_recursive(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    def check(left, right):
        if left is right:
            return True
        if not left or not right or left.val != right.val:
            return False
        outside = check(left.left, right.right)
        inside = check(left.right, right.left)
        return outside and inside

    return check(root.left, root.right)


# Iterative
def is_symmetric_iterative(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    q = deque()
    q.append(root.left)
    q.append(root.right)

    while q:
        left = q.popleft()
        right = q.popleft()

        if not left and not right:
            continue

        if not left or not right or left.val != right.val:
            return False

        q.append(left.left)
        q.append(right.right)
        q.append(left.right)
        q.append(right.left)

    return True


if __name__ == "__main__":
    root = [1, 2, 2, 3, 4, 4, 3]
    root = build(root)
    print(root)
    #     __1__
    #    /     \
    #   2       2
    #  / \     / \
    # 3   4   4   3
    assert is_symmetric_recursive(root) is True
    assert is_symmetric_iterative(root) is True
