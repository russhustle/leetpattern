from typing import Optional

from binarytree import build

from helper import TreeNode


# BST
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.nodes = self._inorder(root)
        self.index = -1
        self.size = len(self.nodes)

    def _inorder(self, node):
        if not node:
            return []
        return (
            self._inorder(node.left) + [node.val] + self._inorder(node.right)
        )

    def hasNext(self) -> bool:
        return self.index < self.size - 1

    def next(self) -> int:
        self.index += 1
        return self.nodes[min(self.index, self.size - 1)]

    def hasPrev(self) -> bool:
        return self.index > 0

    def prev(self) -> int:
        self.index -= 1
        return self.nodes[max(self.index, 0)]


root = build([7, 3, 15, None, None, 9, 20])
print(root)
#   7__
#  /   \
# 3     15
#      /  \
#     9    20
obj = BSTIterator(root)
print(obj.next())  # 3
print(obj.next())  # 7
print(obj.hasNext())  # True
print(obj.prev())  # 3
print(obj.prev())  # None
