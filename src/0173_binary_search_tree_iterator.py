from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# BST
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        topmost_node = self.stack.pop()

        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)

        return topmost_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


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
