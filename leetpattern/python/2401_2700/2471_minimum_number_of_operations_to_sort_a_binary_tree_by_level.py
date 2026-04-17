from collections import deque
from typing import List, Optional

from binarytree import Node as TreeNode


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        """
        层序遍历+置换环
        """
        if not root:
            0

        q = deque([root])
        res = 0
        while q:
            n = len(q)
            level = []
            for _ in range(n):
                cur = q.popleft()
                level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res += self._min_swaps(level)
        return res

    def _min_swaps(self, nums: List) -> int:
        n = len(nums)
        nums = sorted((v, i) for i, v in enumerate(nums))
        vis = [False] * n
        pos = [0] * n
        for new, (_, old) in enumerate(nums):
            pos[old] = new

        swaps = 0
        for i in range(n):
            if vis[i] or nums[i][1] == i:
                continue
            cycle_len = 0
            j = i
            while not vis[j]:
                vis[j] = True
                j = pos[j]
                cycle_len += 1
            swaps += cycle_len - 1

        return swaps
