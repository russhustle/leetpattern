from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


class sumNumbers:
    def dfs(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node, cur):
            if not node:
                return

            cur = cur * 10 + node.val

            if not node.left and not node.right:
                self.res += cur
                return

            dfs(node.left, cur)
            dfs(node.right, cur)

        dfs(root, 0)

        return self.res


if __name__ == "__main__":
    root = [1, 2, 3]
    root = build(root)
    print(root)
    #   1
    #  / \
    # 2   3
    assert sumNumbers().dfs(root) == 25
