from collections import deque
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class CloneGraph:
    def dfs(self, node: Optional["Node"]) -> Optional["Node"]:
        hashmap = {}

        def dfs(node):
            if node in hashmap:
                return hashmap[node]

            res = Node(node.val)
            hashmap[node] = res

            for nei in node.neighbors:
                res.neighbors.append(dfs(nei))

            return res

        return dfs(node) if node else None

    def bfs(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        hashmap = {node: Node(node.val)}
        q = deque([node])

        while q:
            cur = q.popleft()

            for nei in cur.neighbors:
                if nei not in hashmap:
                    hashmap[nei] = Node(nei.val)
                    q.append(nei)

                hashmap[cur].neighbors.append(hashmap[nei])

        return hashmap[node]
