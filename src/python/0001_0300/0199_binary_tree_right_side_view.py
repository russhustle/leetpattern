from collections import deque
from typing import List, Optional

from binarytree import Node as TreeNode
from binarytree import build


# Binary Tree BFS
def rightSideViewBFS(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    q = deque([root])
    res = []

    while q:
        n = len(q)
        for i in range(n):
            node = q.popleft()
            if i == n - 1:
                res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return res


# Binary Tree DFS
def rightSideViewDFS(root: Optional[TreeNode]) -> List[int]:
    """后序遍历，先右后左，遇到的第一个节点就是该深度的最右侧节点"""
    ans = []

    def dfs(node, depth):
        if node is None:
            return
        if depth == len(ans):  # 这个深度首次遇到
            ans.append(node.val)

        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)

    dfs(root, 0)

    return ans


if __name__ == "__main__":
    root = [1, 2, 2, 3, 4, None, 3, None, None, 5]
    root = build(root)
    print(root)
    #     ____1
    #    /     \
    #   2__     2
    #  /   \     \
    # 3     4     3
    #      /
    #     5
    assert rightSideViewBFS(root) == [1, 2, 3, 5]
    assert rightSideViewDFS(root) == [1, 2, 3, 5]
