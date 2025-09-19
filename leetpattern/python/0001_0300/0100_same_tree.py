from collections import deque
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# 1. Recursive
def isSameTreeRecursive(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    elif not p or not q:
        return False
    elif p.val != q.val:
        return False

    return isSameTreeRecursive(p.left, q.left) and isSameTreeRecursive(p.right, q.right)


# 2. Iterative with queue
def isSameTreeIterativeQueue(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    queue = deque([(p, q)])

    while queue:
        p, q = queue.popleft()

        if not p and not q:
            continue
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        queue.append((p.left, q.left))
        queue.append((p.right, q.right))

    return True


# 3. Iterative with stack
def isSameTreeIterativeStack(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    stack = [(p, q)]

    while stack:
        n1, n2 = stack.pop()

        if not n1 and not n2:
            continue
        if not n1 or not n2:
            return False
        if n1.val != n2.val:
            return False

        stack.append((n1.left, n2.left))
        stack.append((n1.right, n2.right))

    return True


if __name__ == "__main__":
    p1 = build([1, 2, 3])
    q1 = build([1, 2, 3])
    p2 = build([1, 2])
    q2 = build([1, None, 2])

    assert isSameTreeRecursive(p1, q1) is True
    assert isSameTreeRecursive(p2, q2) is False
    assert isSameTreeIterativeQueue(p1, q1) is True
    assert isSameTreeIterativeQueue(p2, q2) is False
    assert isSameTreeIterativeStack(p1, q1) is True
    assert isSameTreeIterativeStack(p2, q2) is False
