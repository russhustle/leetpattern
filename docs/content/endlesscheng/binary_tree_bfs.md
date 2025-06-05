---
comments: True
---

# Binary Tree BFS

## Table of Contents

- [x] [102. Binary Tree Level Order Traversal](https://leetcode.cn/problems/binary-tree-level-order-traversal/) (Medium)
- [x] [103. Binary Tree Zigzag Level Order Traversal](https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/) (Medium)
- [x] [107. Binary Tree Level Order Traversal II](https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/) (Medium)
- [x] [199. Binary Tree Right Side View](https://leetcode.cn/problems/binary-tree-right-side-view/) (Medium)
- [x] [513. Find Bottom Left Tree Value](https://leetcode.cn/problems/find-bottom-left-tree-value/) (Medium)
- [x] [515. Find Largest Value in Each Tree Row](https://leetcode.cn/problems/find-largest-value-in-each-tree-row/) (Medium)
- [x] [637. Average of Levels in Binary Tree](https://leetcode.cn/problems/average-of-levels-in-binary-tree/) (Easy)
- [x] [1161. Maximum Level Sum of a Binary Tree](https://leetcode.cn/problems/maximum-level-sum-of-a-binary-tree/) (Medium)
- [ ] [993. Cousins in Binary Tree](https://leetcode.cn/problems/cousins-in-binary-tree/) (Easy)
- [x] [2583. Kth Largest Sum in a Binary Tree](https://leetcode.cn/problems/kth-largest-sum-in-a-binary-tree/) (Medium)
- [x] [1302. Deepest Leaves Sum](https://leetcode.cn/problems/deepest-leaves-sum/) (Medium)
- [ ] [2415. Reverse Odd Levels of Binary Tree](https://leetcode.cn/problems/reverse-odd-levels-of-binary-tree/) (Medium)
- [ ] [1609. Even Odd Tree](https://leetcode.cn/problems/even-odd-tree/) (Medium)
- [ ] [623. Add One Row to Tree](https://leetcode.cn/problems/add-one-row-to-tree/) (Medium)
- [ ] [2471. Minimum Number of Operations to Sort a Binary Tree by Level](https://leetcode.cn/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/) (Medium)
- [x] [863. All Nodes Distance K in Binary Tree](https://leetcode.cn/problems/all-nodes-distance-k-in-binary-tree/) (Medium)
- [ ] [2641. Cousins in Binary Tree II](https://leetcode.cn/problems/cousins-in-binary-tree-ii/) (Medium)
- [ ] [919. Complete Binary Tree Inserter](https://leetcode.cn/problems/complete-binary-tree-inserter/) (Medium)
- [ ] [331. Verify Preorder Serialization of a Binary Tree](https://leetcode.cn/problems/verify-preorder-serialization-of-a-binary-tree/) (Medium)
- [ ] [958. Check Completeness of a Binary Tree](https://leetcode.cn/problems/check-completeness-of-a-binary-tree/) (Medium)
- [ ] [662. Maximum Width of Binary Tree](https://leetcode.cn/problems/maximum-width-of-binary-tree/) (Medium)
- [ ] [3157. Find the Level of Tree with Minimum Sum](https://leetcode.cn/problems/find-the-level-of-tree-with-minimum-sum/) (Medium) 👑
- [ ] [1602. Find Nearest Right Node in Binary Tree](https://leetcode.cn/problems/find-nearest-right-node-in-binary-tree/) (Medium) 👑
- [ ] [742. Closest Leaf in a Binary Tree](https://leetcode.cn/problems/closest-leaf-in-a-binary-tree/) (Medium) 👑
- [ ] [1660. Correct a Binary Tree](https://leetcode.cn/problems/correct-a-binary-tree/) (Medium) 👑

## 102. Binary Tree Level Order Traversal

-   [LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [LeetCode CH](https://leetcode.cn/problems/binary-tree-level-order-traversal/) (Medium)

-   Tags: tree, breadth first search, binary tree

```python title="102. Binary Tree Level Order Traversal - Python Solution"
from collections import deque
from typing import List, Optional

from binarytree import Node as TreeNode
from binarytree import build


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    q = deque([root])
    res = []

    while q:
        level = []
        size = len(q)

        for _ in range(size):
            cur = q.popleft()
            level.append(cur.val)

            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        res.append(level)

    return res


tree = build([3, 9, 20, None, None, 15, 7])
print(tree)
#   3___
#  /    \
# 9     _20
#      /   \
#     15    7
print(levelOrder(tree))  # [[3], [9, 20], [15, 7]]

```

## 103. Binary Tree Zigzag Level Order Traversal

-   [LeetCode](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) | [LeetCode CH](https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/) (Medium)

-   Tags: tree, breadth first search, binary tree

```python title="103. Binary Tree Zigzag Level Order Traversal - Python Solution"
from collections import deque
from typing import List, Optional

from binarytree import Node as TreeNode
from binarytree import build


def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    q = deque([root])
    res = []

    while q:
        level = []
        n = len(q)

        for _ in range(n):
            cur = q.popleft()
            level.append(cur.val)

            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        res.append(level if len(res) % 2 == 0 else level[::-1])

    return res


tree = build([3, 9, 20, None, None, 15, 7])
print(tree)
#   3___
#  /    \
# 9     _20
#      /   \
#     15    7
print(zigzagLevelOrder(tree))  # [[3], [20, 9], [15, 7]]

```

## 107. Binary Tree Level Order Traversal II

-   [LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/) | [LeetCode CH](https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/) (Medium)

-   Tags: tree, breadth first search, binary tree

```python title="107. Binary Tree Level Order Traversal II - Python Solution"
from collections import deque
from typing import List, Optional

from binarytree import Node as TreeNode
from binarytree import build


def levelOrderBottom(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    res = []
    q = deque([root])

    while q:
        level = []
        n = len(q)

        for _ in range(n):
            cur = q.popleft()
            level.append(cur.val)

            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        res.append(level)

    return res[::-1]


tree = build([3, 9, 20, None, None, 15, 7])
print(tree)
#   3___
#  /    \
# 9     _20
#      /   \
#     15    7
print(levelOrderBottom(tree))  # [[15, 7], [9, 20], [3]]

```

## 199. Binary Tree Right Side View

-   [LeetCode](https://leetcode.com/problems/binary-tree-right-side-view/) | [LeetCode CH](https://leetcode.cn/problems/binary-tree-right-side-view/) (Medium)

-   Tags: tree, depth first search, breadth first search, binary tree

```python title="199. Binary Tree Right Side View - Python Solution"
from collections import deque
from typing import List, Optional

from binarytree import Node as TreeNode
from binarytree import build


# Binary Tree BFS
def rightSideViewBFS(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    q = deque([root])
    res = []

    while q:
        n = len(q)
        for i in range(n):
            node = q.popleft()
            if i == n - 1:
                res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return res


# Binary Tree DFS
def rightSideViewDFS(root: Optional[TreeNode]) -> List[int]:
    """后序遍历，先右后左，遇到的第一个节点就是该深度的最右侧节点"""
    ans = []

    def dfs(node, depth):
        if node is None:
            return
        if depth == len(ans):  # 这个深度首次遇到
            ans.append(node.val)

        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)

    dfs(root, 0)

    return ans


if __name__ == "__main__":
    root = [1, 2, 2, 3, 4, None, 3, None, None, 5]
    root = build(root)
    print(root)
    #     ____1
    #    /     \
    #   2__     2
    #  /   \     \
    # 3     4     3
    #      /
    #     5
    assert rightSideViewBFS(root) == [1, 2, 3, 5]
    assert rightSideViewDFS(root) == [1, 2, 3, 5]

```

## 513. Find Bottom Left Tree Value

-   [LeetCode](https://leetcode.com/problems/find-bottom-left-tree-value/) | [LeetCode CH](https://leetcode.cn/problems/find-bottom-left-tree-value/) (Medium)

-   Tags: tree, depth first search, breadth first search, binary tree

```python title="513. Find Bottom Left Tree Value - Python Solution"
from collections import deque
from typing import Optional

from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findBottomLeftValue(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    queue = deque([root])
    result = 0

    while queue:
        size = len(queue)

        for i in range(size):
            node = queue.popleft()
            if i == 0:
                result = node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


root = [1, 2, 2, 3, 4, None, None, None, None, 5]
root = build(root)
print(root)
#     ____1
#    /     \
#   2__     2
#  /   \
# 3     4
#      /
#     5

print(findBottomLeftValue(root))  # 5

```

## 515. Find Largest Value in Each Tree Row

-   [LeetCode](https://leetcode.com/problems/find-largest-value-in-each-tree-row/) | [LeetCode CH](https://leetcode.cn/problems/find-largest-value-in-each-tree-row/) (Medium)

-   Tags: tree, depth first search, breadth first search, binary tree

```python title="515. Find Largest Value in Each Tree Row - Python Solution"
from collections import deque
from typing import List, Optional

from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def largestValues(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        levelMax = float("-inf")
        for _ in range(len(queue)):
            node = queue.popleft()

            levelMax = max(levelMax, node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(levelMax)

    return result


root = [1, 2, 2, 3, 4, None, None, None, None, 5]
root = build(root)
print(root)
#     ____1
#    /     \
#   2__     2
#  /   \
# 3     4
#      /
#     5
print(largestValues(root))  # [1, 2, 4, 5]

```

## 637. Average of Levels in Binary Tree

-   [LeetCode](https://leetcode.com/problems/average-of-levels-in-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/average-of-levels-in-binary-tree/) (Easy)

-   Tags: tree, depth first search, breadth first search, binary tree

```python title="637. Average of Levels in Binary Tree - Python Solution"
from collections import deque
from typing import List, Optional

from binarytree import Node as TreeNode
from binarytree import build


# Binary Tree BFS
def averageOfLevels(root: Optional[TreeNode]) -> List[float]:
    if not root:
        return []

    q = deque([root])
    res = []

    while q:
        n = len(q)
        level = 0
        for _ in range(n):
            cur = q.popleft()
            level += cur.val

            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        res.append(float(level / n))

    return res


if __name__ == "__main__":
    root = [3, 9, 20, None, None, 15, 7]
    root = build(root)
    print(root)
    #   3___
    #  /    \
    # 9     _20
    #      /   \
    #     15    7
    assert averageOfLevels(root) == [3.00000, 14.50000, 11.00000]

```

## 1161. Maximum Level Sum of a Binary Tree

-   [LeetCode](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/maximum-level-sum-of-a-binary-tree/) (Medium)

-   Tags: tree, depth first search, breadth first search, binary tree

```python title="1161. Maximum Level Sum of a Binary Tree - Python Solution"
from collections import deque
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# BFS
def maxLevelSum(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    q = deque([root])
    res = 0
    maxSum = float("-inf")
    level = 1

    while q:
        n = len(q)
        curSum = 0

        for _ in range(n):
            node = q.popleft()
            curSum += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        if curSum > maxSum:
            maxSum = curSum
            res = level
        level += 1

    return res


root = [1, 7, 0, 7, -8, None, None]
root = build(root)
print(root)
#     ___1
#    /    \
#   7      0
#  / \
# 7   -8
print(maxLevelSum(root))  # 2

```

## 993. Cousins in Binary Tree

-   [LeetCode](https://leetcode.com/problems/cousins-in-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/cousins-in-binary-tree/) (Easy)

-   Tags: tree, depth first search, breadth first search, binary tree
## 2583. Kth Largest Sum in a Binary Tree

-   [LeetCode](https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/kth-largest-sum-in-a-binary-tree/) (Medium)

-   Tags: tree, breadth first search, sorting, binary tree

```python title="2583. Kth Largest Sum in a Binary Tree - Python Solution"
from collections import deque
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# BFS
def kthLargestLevelSum(root: Optional[TreeNode], k: int) -> int:
    if not root:
        return 0
    sums = []
    q = deque([root])

    while q:
        size = len(q)
        level = 0
        for _ in range(size):
            node = q.popleft()
            level += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        sums.append(level)

    if len(sums) < k:
        return -1

    sums.sort()
    return sums[-k]


root = [5, 8, 9, 2, 1, 3, 7, 4, 6]
root = build(root)
k = 2
print(kthLargestLevelSum(root, k))  # 13

```

## 1302. Deepest Leaves Sum

-   [LeetCode](https://leetcode.com/problems/deepest-leaves-sum/) | [LeetCode CH](https://leetcode.cn/problems/deepest-leaves-sum/) (Medium)

-   Tags: tree, depth first search, breadth first search, binary tree

```python title="1302. Deepest Leaves Sum - Python Solution"
from collections import deque
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# BFS
def deepestLeavesSum(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    q = deque([root])

    while q:
        n = len(q)
        res = 0
        for _ in range(n):
            node = q.popleft()
            res += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return res


root = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, None, 8]
root = build(root)
print(root)
#       __1
#      /   \
#     2     3__
#    / \       \
#   4   5       6
#  /           /
# 7           8
print(deepestLeavesSum(root))  # 15

```

## 2415. Reverse Odd Levels of Binary Tree

-   [LeetCode](https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/reverse-odd-levels-of-binary-tree/) (Medium)

-   Tags: tree, depth first search, breadth first search, binary tree
## 1609. Even Odd Tree

-   [LeetCode](https://leetcode.com/problems/even-odd-tree/) | [LeetCode CH](https://leetcode.cn/problems/even-odd-tree/) (Medium)

-   Tags: tree, breadth first search, binary tree
## 623. Add One Row to Tree

-   [LeetCode](https://leetcode.com/problems/add-one-row-to-tree/) | [LeetCode CH](https://leetcode.cn/problems/add-one-row-to-tree/) (Medium)

-   Tags: tree, depth first search, breadth first search, binary tree
## 2471. Minimum Number of Operations to Sort a Binary Tree by Level

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/) (Medium)

-   Tags: tree, breadth first search, binary tree
## 863. All Nodes Distance K in Binary Tree

-   [LeetCode](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/all-nodes-distance-k-in-binary-tree/) (Medium)

-   Tags: hash table, tree, depth first search, breadth first search, binary tree

```python title="863. All Nodes Distance K in Binary Tree - Python Solution"
from collections import deque
from typing import List

from binarytree import Node as TreeNode
from binarytree import build


# BFS
def distanceK(root: TreeNode, target: TreeNode, k: int) -> List[int]:
    parent = dict()

    def dfs(node, par=None):
        if node:
            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)

    dfs(root)

    q = deque([(target, 0)])
    seen = set([target])

    while q:
        node, dist = q.popleft()

        if dist == k:
            return [node.val] + [node.val for node, _ in q]

        for nei in (node.left, node.right, parent[node]):
            if nei and nei not in seen:
                seen.add(nei)
                q.append((nei, dist + 1))

    return []


root = build([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
print(root)
#     ______3__
#    /         \
#   5__         1
#  /   \       / \
# 6     2     0   8
#      / \
#     7   4
target = root.left
k = 2
print(distanceK(root, target, k))  # [7, 4, 1]

```

## 2641. Cousins in Binary Tree II

-   [LeetCode](https://leetcode.com/problems/cousins-in-binary-tree-ii/) | [LeetCode CH](https://leetcode.cn/problems/cousins-in-binary-tree-ii/) (Medium)

-   Tags: hash table, tree, depth first search, breadth first search, binary tree
## 919. Complete Binary Tree Inserter

-   [LeetCode](https://leetcode.com/problems/complete-binary-tree-inserter/) | [LeetCode CH](https://leetcode.cn/problems/complete-binary-tree-inserter/) (Medium)

-   Tags: tree, breadth first search, design, binary tree
## 331. Verify Preorder Serialization of a Binary Tree

-   [LeetCode](https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/verify-preorder-serialization-of-a-binary-tree/) (Medium)

-   Tags: string, stack, tree, binary tree
## 958. Check Completeness of a Binary Tree

-   [LeetCode](https://leetcode.com/problems/check-completeness-of-a-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/check-completeness-of-a-binary-tree/) (Medium)

-   Tags: tree, breadth first search, binary tree
## 662. Maximum Width of Binary Tree

-   [LeetCode](https://leetcode.com/problems/maximum-width-of-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/maximum-width-of-binary-tree/) (Medium)

-   Tags: tree, depth first search, breadth first search, binary tree
## 3157. Find the Level of Tree with Minimum Sum

-   [LeetCode](https://leetcode.com/problems/find-the-level-of-tree-with-minimum-sum/) | [LeetCode CH](https://leetcode.cn/problems/find-the-level-of-tree-with-minimum-sum/) (Medium)

-   Tags: tree, depth first search, breadth first search, binary tree
## 1602. Find Nearest Right Node in Binary Tree

-   [LeetCode](https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/find-nearest-right-node-in-binary-tree/) (Medium)

-   Tags: tree, breadth first search, binary tree
## 742. Closest Leaf in a Binary Tree

-   [LeetCode](https://leetcode.com/problems/closest-leaf-in-a-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/closest-leaf-in-a-binary-tree/) (Medium)

-   Tags: tree, depth first search, breadth first search, binary tree
## 1660. Correct a Binary Tree

-   [LeetCode](https://leetcode.com/problems/correct-a-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/correct-a-binary-tree/) (Medium)

-   Tags: hash table, tree, depth first search, breadth first search, binary tree
