---
comments: True
---

# Tree BFS

## Table of Contents

- [x] [199. Binary Tree Right Side View](https://leetcode.cn/problems/binary-tree-right-side-view/) (Medium)
- [x] [111. Minimum Depth of Binary Tree](https://leetcode.cn/problems/minimum-depth-of-binary-tree/) (Easy)
- [x] [104. Maximum Depth of Binary Tree](https://leetcode.cn/problems/maximum-depth-of-binary-tree/) (Easy)
- [x] [637. Average of Levels in Binary Tree](https://leetcode.cn/problems/average-of-levels-in-binary-tree/) (Easy)
- [x] [429. N-ary Tree Level Order Traversal](https://leetcode.cn/problems/n-ary-tree-level-order-traversal/) (Medium)
- [x] [515. Find Largest Value in Each Tree Row](https://leetcode.cn/problems/find-largest-value-in-each-tree-row/) (Medium)
- [x] [116. Populating Next Right Pointers in Each Node](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/) (Medium)
- [x] [117. Populating Next Right Pointers in Each Node II](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/) (Medium)
- [x] [513. Find Bottom Left Tree Value](https://leetcode.cn/problems/find-bottom-left-tree-value/) (Medium)
- [x] [863. All Nodes Distance K in Binary Tree](https://leetcode.cn/problems/all-nodes-distance-k-in-binary-tree/) (Medium)

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

## 111. Minimum Depth of Binary Tree

-   [LeetCode](https://leetcode.com/problems/minimum-depth-of-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/minimum-depth-of-binary-tree/) (Easy)

-   Tags: tree, depth first search, breadth first search, binary tree

```python title="111. Minimum Depth of Binary Tree - Python Solution"
from collections import deque
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# Iterative
def minDepthIterative(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    q = deque([root])
    res = 0

    while q:
        res += 1

        for _ in range(len(q)):
            node = q.popleft()

            if not node.left and not node.right:
                return res

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


# Recursive
def minDepthRecursive(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    if root.left is None and root.right is not None:
        return 1 + minDepthRecursive(root.right)
    if root.left is not None and root.right is None:
        return 1 + minDepthRecursive(root.left)

    return 1 + min(minDepthRecursive(root.left), minDepthRecursive(root.right))


root = [1, 2, 2, 3, 4, None, None, None, None, 5]
root = build(root)
print(root)
"""
    ____1
   /     \
  2__     2
 /   \
3     4
     /
    5

"""
print(minDepthIterative(root))  # 2
print(minDepthRecursive(root))  # 2

```

## 104. Maximum Depth of Binary Tree

-   [LeetCode](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/maximum-depth-of-binary-tree/) (Easy)

-   Tags: tree, depth first search, breadth first search, binary tree

```python title="104. Maximum Depth of Binary Tree - Python Solution"
from collections import deque
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# Recursive
def maxDepthRecursive(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    left = maxDepthRecursive(root.left)
    right = maxDepthRecursive(root.right)

    return 1 + max(left, right)


# DFS
def maxDepthDFS(root: Optional[TreeNode]) -> int:
    res = 0

    def dfs(node, cnt):
        if node is None:
            return
        cnt += 1
        nonlocal res
        res = max(res, cnt)

        dfs(node.left, cnt)
        dfs(node.right, cnt)

    dfs(root, 0)

    return res


# Iterative
def maxDepthIterative(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    q = deque([root])
    res = 0

    while q:
        res += 1
        n = len(q)

        for _ in range(n):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return res


if __name__ == "__main__":
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
    assert maxDepthRecursive(root) == 4
    assert maxDepthDFS(root) == 4
    assert maxDepthIterative(root) == 4

```

## 637. Average of Levels in Binary Tree

-   [LeetCode](https://leetcode.com/problems/average-of-levels-in-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/average-of-levels-in-binary-tree/) (Easy)

-   Tags: tree, depth first search, breadth first search, binary tree

```python title="637. Average of Levels in Binary Tree - Python Solution"
from collections import deque
from typing import List, Optional

from binarytree import build, Node as TreeNode


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

## 429. N-ary Tree Level Order Traversal

-   [LeetCode](https://leetcode.com/problems/n-ary-tree-level-order-traversal/) | [LeetCode CH](https://leetcode.cn/problems/n-ary-tree-level-order-traversal/) (Medium)

-   Tags: tree, breadth first search

```python title="429. N-ary Tree Level Order Traversal - Python Solution"
from collections import deque
from typing import List, Optional


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def levelOrder(root: Optional[Node]) -> List[List[int]]:
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        level = []
        size = len(queue)

        for _ in range(size):
            node = queue.popleft()
            level.append(node.val)

            for child in node.children:
                queue.append(child)

        result.append(level)

    return result


root = Node(
    1,
    [
        Node(
            3,
            [
                Node(5, []),
                Node(6, []),
            ],
        ),
        Node(2, []),
        Node(4, []),
    ],
)
print(levelOrder(root))  # [[1], [3, 2, 4], [5, 6]]

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

## 116. Populating Next Right Pointers in Each Node

-   [LeetCode](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/) | [LeetCode CH](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/) (Medium)

-   Tags: linked list, tree, depth first search, breadth first search, binary tree
-   Perfect Binary Tree


```python title="116. Populating Next Right Pointers in Each Node - Python Solution"
from collections import deque
from typing import Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: "Optional[Node]") -> "Optional[Node]":
    if not root:
        return root

    queue = deque([root])

    while queue:
        size = len(queue)
        prev = None

        for _ in range(size):
            node = queue.popleft()

            if prev:
                prev.next = node
            prev = node

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return root


# Perfect binary tree creation
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
#     __1__
#    /     \
#   2__     3
#  /   \   / \
# 4     5 6   7


# Connect the nodes
connect(root)
#      __1__ -> None
#     /     \
#   _2_ ->  3 -> None
#  /   \   / \
# 4 -> 5->6-> 7 -> None


assert root.next is None
assert root.left.next == root.right
assert root.left.left.next == root.left.right
assert root.left.right.next == root.right.left
assert root.right.left.next == root.right.right
assert root.right.right.next is None
print("All tests passed.")

```

## 117. Populating Next Right Pointers in Each Node II

-   [LeetCode](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/) | [LeetCode CH](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/) (Medium)

-   Tags: linked list, tree, depth first search, breadth first search, binary tree

```python title="117. Populating Next Right Pointers in Each Node II - Python Solution"
from collections import deque


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: "Node") -> "Node":
    if not root:
        return root

    queue = deque([root])

    while queue:
        size = len(queue)
        prev = None

        for _ in range(size):
            node = queue.popleft()

            if prev:
                prev.next = node

            prev = node

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return root


# Binary tree creation
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(7)
#       1
#      / \
#     2   3
#    / \   \
#   4   5   7

# Connect the nodes
connect(root)
#       1 -> None
#      / \
#     2 -> 3 -> None
#    / \    \
#   4 -> 5 -> 7 -> None

assert root.next is None
assert root.left.next == root.right
assert root.right.next is None
assert root.left.left.next == root.left.right
assert root.left.right.next == root.right.right
assert root.right.right.next is None

print("All tests passed.")

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
