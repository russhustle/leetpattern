---
comments: True
---

# Binary Tree

## Table of Contents

- [x] [298. Binary Tree Longest Consecutive Sequence](https://leetcode.cn/problems/binary-tree-longest-consecutive-sequence/) (Medium) 👑
- [ ] [549. Binary Tree Longest Consecutive Sequence II](https://leetcode.cn/problems/binary-tree-longest-consecutive-sequence-ii/) (Medium) 👑
- [ ] [250. Count Univalue Subtrees](https://leetcode.cn/problems/count-univalue-subtrees/) (Medium) 👑
- [ ] [1120. Maximum Average Subtree](https://leetcode.cn/problems/maximum-average-subtree/) (Medium) 👑
- [ ] [545. Boundary of Binary Tree](https://leetcode.cn/problems/boundary-of-binary-tree/) (Medium) 👑
- [x] [366. Find Leaves of Binary Tree](https://leetcode.cn/problems/find-leaves-of-binary-tree/) (Medium) 👑
- [ ] [314. Binary Tree Vertical Order Traversal](https://leetcode.cn/problems/binary-tree-vertical-order-traversal/) (Medium) 👑

## 298. Binary Tree Longest Consecutive Sequence

-   [LeetCode](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/) | [LeetCode CH](https://leetcode.cn/problems/binary-tree-longest-consecutive-sequence/) (Medium)

-   Tags: tree, depth first search, binary tree

```python title="298. Binary Tree Longest Consecutive Sequence - Python Solution"
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# Binary Tree
def longestConsecutive(root: Optional[TreeNode]) -> int:
    res = 0

    def dfs(node):
        if not node:
            return 0

        left, right = dfs(node.left), dfs(node.right)
        cur = 1
        if node.left and node.left.val == (node.val + 1):
            cur = max(cur, left + 1)
        if node.right and node.right.val == (node.val + 1):
            cur = max(cur, right + 1)

        nonlocal res
        res = max(res, cur)
        return cur

    dfs(root)

    return res


if __name__ == "__main__":
    root = build([1, 3, 2, 4, None, None, None, 5])
    print(root)
    #       1
    #      / \
    #     3   2
    #    /
    #   4
    #  /
    # 5
    print(longestConsecutive(root))  # 3

```

## 549. Binary Tree Longest Consecutive Sequence II

-   [LeetCode](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/) | [LeetCode CH](https://leetcode.cn/problems/binary-tree-longest-consecutive-sequence-ii/) (Medium)

-   Tags: tree, depth first search, binary tree

## 250. Count Univalue Subtrees

-   [LeetCode](https://leetcode.com/problems/count-univalue-subtrees/) | [LeetCode CH](https://leetcode.cn/problems/count-univalue-subtrees/) (Medium)

-   Tags: tree, depth first search, binary tree

## 1120. Maximum Average Subtree

-   [LeetCode](https://leetcode.com/problems/maximum-average-subtree/) | [LeetCode CH](https://leetcode.cn/problems/maximum-average-subtree/) (Medium)

-   Tags: tree, depth first search, binary tree

## 545. Boundary of Binary Tree

-   [LeetCode](https://leetcode.com/problems/boundary-of-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/boundary-of-binary-tree/) (Medium)

-   Tags: tree, depth first search, binary tree

## 366. Find Leaves of Binary Tree

-   [LeetCode](https://leetcode.com/problems/find-leaves-of-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/find-leaves-of-binary-tree/) (Medium)

-   Tags: tree, depth first search, binary tree

```python title="366. Find Leaves of Binary Tree - Python Solution"
from collections import defaultdict
from typing import List, Optional

from binarytree import Node as TreeNode
from binarytree import build


def findLeaves(root: Optional[TreeNode]) -> List[List[int]]:
    depths = defaultdict(list)

    def dfs(node):
        if not node:
            return 0
        l, r = dfs(node.left), dfs(node.right)
        depth = 1 + max(l, r)
        depths[depth].append(node.val)
        return depth

    dfs(root)
    return [i for i in depths.values()]


if __name__ == "__main__":
    root = build([1, 2, 3, 4, 5])
    print(root)
    #     __1
    #    /   \
    #   2     3
    #  / \
    # 4   5
    print(findLeaves(root))  # [[4, 5, 3], [2], [1]]

```

## 314. Binary Tree Vertical Order Traversal

-   [LeetCode](https://leetcode.com/problems/binary-tree-vertical-order-traversal/) | [LeetCode CH](https://leetcode.cn/problems/binary-tree-vertical-order-traversal/) (Medium)

-   Tags: hash table, tree, depth first search, breadth first search, sorting, binary tree
