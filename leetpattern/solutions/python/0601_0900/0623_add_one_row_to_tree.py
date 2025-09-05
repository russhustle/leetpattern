from typing import Optional
from binarytree import build, Node as TreeNode
from collections import deque
from copy import deepcopy


# BFS
def addOneRow_bfs(root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
    if not root:
        return None

    if depth == 1:
        new = TreeNode(val)
        new.left = root
        return new

    q = deque([root])
    cur = 1

    while q:
        size = len(q)
        for _ in range(size):
            node = q.popleft()

            if cur == depth - 1:
                old_left, old_right = node.left, node.right
                node.left, node.right = TreeNode(val), TreeNode(val)
                node.left.left = old_left
                node.right.right = old_right
            else:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        cur += 1

    return root


# DFS
def addOneRow_dfs(root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
    if depth == 1:
        new = TreeNode(val)
        new.left = root
        return new

    def dfs(node, cur):
        if not node:
            return
        if cur == depth - 1:
            old_left, old_right = node.left, node.right
            node.left = TreeNode(val, old_left, None)
            node.right = TreeNode(val, None, old_right)
        else:
            dfs(node.left, cur + 1)
            dfs(node.right, cur + 1)

    dfs(root, 1)

    return root


if __name__ == "__main__":
    root = build([4, 2, 6, 3, 1, 5])
    print(root)
    #     __4__
    #    /     \
    #   2       6
    #  / \     /
    # 3   1   5
    print(addOneRow_bfs(deepcopy(root), 1, 2))
    #         4
    #        / \
    #     __1   1__
    #    /         \
    #   2           6
    #  / \         /
    # 3   1       5
    print(addOneRow_dfs(deepcopy(root), 1, 2))
    #         4
    #        / \
    #     __1   1__
    #    /         \
    #   2           6
    #  / \         /
    # 3   1       5
