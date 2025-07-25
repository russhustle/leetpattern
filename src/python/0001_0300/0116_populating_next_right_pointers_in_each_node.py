"""
-   Perfect Binary Tree
"""

from collections import deque
from typing import Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: "Optional[Node]") -> "Optional[Node]":
    if not root:
        return root

    queue = deque([root])

    while queue:
        size = len(queue)
        prev = None

        for _ in range(size):
            node = queue.popleft()

            if prev:
                prev.next = node
            prev = node

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return root


# Perfect binary tree creation
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
#     __1__
#    /     \
#   2__     3
#  /   \   / \
# 4     5 6   7


# Connect the nodes
connect(root)
#      __1__ -> None
#     /     \
#   _2_ ->  3 -> None
#  /   \   / \
# 4 -> 5->6-> 7 -> None


assert root.next is None
assert root.left.next == root.right
assert root.left.left.next == root.left.right
assert root.left.right.next == root.right.left
assert root.right.left.next == root.right.right
assert root.right.right.next is None
print("All tests passed.")
