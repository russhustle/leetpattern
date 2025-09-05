from collections import deque
from typing import Optional
from binarytree import Node as TreeNode
from binarytree import build


def _min_swaps_to_sort(nums):
    """
    Calculate the minimum number of swaps to sort the array.
    Method: Permutation Cycle
    """
    n = len(nums)
    arr = [(num, i) for i, num in enumerate(nums)]
    arr.sort(key=lambda x: x[0])

    visited = [False] * n
    res = 0

    for i in range(n):
        if visited[i] or arr[i][1] == i:
            continue

        cycle_len = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = arr[j][1]
            cycle_len += 1

        if cycle_len > 1:
            res += cycle_len - 1

    return res


def minimumOperations_bfs(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    res = 0
    q = deque([root])

    while q:
        size = len(q)
        level = []
        for _ in range(size):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        res += _min_swaps_to_sort(level)

    return res


if __name__ == "__main__":
    root = build([1, 4, 3, 7, 6, 8, 5, None, None, None, None, 9, None, 10])
    print(root)
    #     __1____
    #    /       \
    #   4         3___
    #  / \       /    \
    # 7   6     8     _5
    #          /     /
    #         9     10
    assert minimumOperations_bfs(root) == 3
