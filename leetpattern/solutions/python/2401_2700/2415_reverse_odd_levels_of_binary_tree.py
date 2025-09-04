from collections import deque
from typing import Optional
from binarytree import build, Node as TreeNode


def reverseOddLevels(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    q = deque([root])
    level = -1

    while q:
        size = len(q)
        nodes = []
        level += 1

        for _ in range(size):
            node = q.popleft()
            nodes.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        if level % 2 == 1:
            i, j = 0, len(nodes) - 1
            while i < j:
                nodes[i].val, nodes[j].val = nodes[j].val, nodes[i].val
                i += 1
                j -= 1

    return root


if __name__ == "__main__":
    root = build([2, 3, 5, 8, 13, 21, 34])
    print(root)
    #     ___2___
    #    /       \
    #   3        _5
    #  / \      /  \
    # 8   13   21   34
    print(reverseOddLevels(root))
    #     ___2___
    #    /       \
    #   5        _3
    #  / \      /  \
    # 8   13   21   34
