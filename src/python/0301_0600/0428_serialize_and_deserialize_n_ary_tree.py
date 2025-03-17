from typing import List, Optional


class Node(object):
    def __init__(
        self,
        val: Optional[int] = None,
        children: Optional[List["Node"]] = None,
    ):
        if children is None:
            children = []
        self.val = val
        self.children = children


# DFS
class CodecDFS:
    def serialize(self, root: "Node") -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if not root:
            return "*"

        data = ""
        data += str(root.val) + "|" + str(len(root.children))
        for child in root.children:
            data += "|" + self.serialize(child)
        return data

    def deserialize(self, data: str) -> "Node":
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if data == "*":
            return None

        data = data.split("|")[::-1]

        def dfs(data):
            root = Node(int(data.pop()))
            size = int(data.pop())
            for i in range(size):
                root.children.append(dfs(data))
            return root

        return dfs(data)


if __name__ == "__main__":
    obj = CodecDFS()
    root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
    data = obj.serialize(root)
    print(data)  # 1|3|3|2|5|0|6|0|2|0|4|0
    root = obj.deserialize(data)
    print(root.val)  # 1
    print(root.children[0].val)  # 3
    print(root.children[1].val)  # 2
    print(root.children[2].val)  # 4
    print(root.children[0].children[0].val)  # 5
