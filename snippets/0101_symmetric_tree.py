from collections import deque
from typing import Optional

from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. Recursive
def isSymmetricRecursive(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    def compare(left, right):
        if left is None and right is not None:
            return False
        elif left is not None and right is None:
            return False
        elif left is None and right is None:
            return True
        elif left.val != right.val:
            return False

        outside = compare(left.left, right.right)
        inside = compare(left.right, right.left)

        return outside and inside

    return compare(root.left, root.right)


# 2. Iterative
def isSymmetricIterative(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    q = deque()
    q.append(root.left)
    q.append(root.right)

    while q:
        leftNode = q.popleft()
        rightNode = q.popleft()

        if not leftNode and not rightNode:
            continue

        if not leftNode or not rightNode or leftNode.val != rightNode.val:
            return False

        q.append(leftNode.left)
        q.append(rightNode.right)
        q.append(leftNode.right)
        q.append(rightNode.left)

    return True


root = [1, 2, 2, 3, 4, 4, 3]
root = build(root)
print(root)
#     __1__
#    /     \
#   2       2
#  / \     / \
# 3   4   4   3
print(isSymmetricRecursive(root))  # True
print(isSymmetricIterative(root))  # True
