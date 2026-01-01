from collections import deque
from typing import Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        left: Optional["Node"] = None,
        right: Optional["Node"] = None,
        next: Optional["Node"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class connect:
    def level_order(self, root: "Node") -> "Node":
        if not root:
            return None

        q = deque([root])

        while q:
            size = len(q)
            prev = None

            for _ in range(size):
                node = q.popleft()

                if prev:
                    prev.next = node
                prev = node

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root


if __name__ == "__main__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(7)
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   7

    solution = connect()
    root = solution.level_order(root)
    assert root.next is None
    assert root.left.next == root.right
    assert root.right.next is None
    assert root.left.left.next == root.left.right
    assert root.left.right.next == root.right.right
    assert root.right.right.next is None
    #       1 -> None
    #      / \
    #     2 -> 3 -> None
    #    / \    \
    #   4 -> 5 -> 7 -> None
