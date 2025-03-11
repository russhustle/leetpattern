from collections import deque
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# BFS
class BFS:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        res = []
        q = deque([root])

        while q:
            node = q.popleft()

            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")

        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        index = 1

        while q:
            node = q.popleft()

            if nodes[index] != "null":
                node.left = TreeNode(int(nodes[index]))
                q.append(node.left)
            index += 1

            if nodes[index] != "null":
                node.right = TreeNode(int(nodes[index]))
                q.append(node.right)
            index += 1

        return root


# DFS
class DFS:
    def serialize(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if not node:
                return ["null"]
            return [str(node.val)] + dfs(node.left) + dfs(node.right)

        return ",".join(dfs(root))

    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        self.index = 0

        def dfs():
            if nodes[self.index] == "null":
                self.index += 1
                return None

            node = TreeNode(int(nodes[self.index]))
            self.index += 1

            node.left = dfs()
            node.right = dfs()

            return node

        root = dfs()
        return root


root = build([1, 2, 3, None, None, 4, 5])
print(root)
#   1__
#  /   \
# 2     3
#      / \
#     4   5

bfs = BFS()
data1 = bfs.serialize(root)
print(data1)  # "1,2,3,null,null,4,5,null,null,null,null"
root1 = bfs.deserialize(data1)
print(root1)
#   1__
#  /   \
# 2     3
#      / \
#     4   5

dfs = DFS()
data2 = dfs.serialize(root)
print(data2)  # "1,2,null,null,3,4,null,null,5,null,null"
root2 = dfs.deserialize(data2)
print(root2)
#   1__
#  /   \
# 2     3
#      / \
#     4   5
