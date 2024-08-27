from collections import deque

from binarytree import TreeNode


def treeBFS(root: TreeNode):
    if not root:
        return

    q = deque([root])

    while q:

        n = len(q)

        for i in range(n):
            node = q.popleft()

            # Do something here

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
