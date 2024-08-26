from collections import deque


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


def connect(root: "Node") -> "Node":
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


# Binary tree creation
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

# Connect the nodes
connect(root)
#       1 -> None
#      / \
#     2 -> 3 -> None
#    / \    \
#   4 -> 5 -> 7 -> None

assert root.next is None
assert root.left.next == root.right
assert root.right.next is None
assert root.left.left.next == root.left.right
assert root.left.right.next == root.right.right
assert root.right.right.next is None

print("All tests passed.")
