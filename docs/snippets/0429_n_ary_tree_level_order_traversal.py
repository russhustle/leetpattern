from collections import deque
from typing import List, Optional


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def levelOrder(root: Optional[Node]) -> List[List[int]]:
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        level = []
        size = len(queue)

        for _ in range(size):
            node = queue.popleft()
            level.append(node.val)

            for child in node.children:
                queue.append(child)

        result.append(level)

    return result


root = Node(
    1,
    [
        Node(
            3,
            [
                Node(5, []),
                Node(6, []),
            ],
        ),
        Node(2, []),
        Node(4, []),
    ],
)
print(levelOrder(root))  # [[1], [3, 2, 4], [5, 6]]
