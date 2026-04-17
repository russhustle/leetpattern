from collections import deque
from typing import Optional

from binarytree import Node as TreeNode


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])
        res, level = 1, 1
        max_sum = root.val

        while q:
            level_sum = 0
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                level_sum += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            if level_sum > max_sum:
                max_sum = level_sum
                res = level

            level += 1

        return res
