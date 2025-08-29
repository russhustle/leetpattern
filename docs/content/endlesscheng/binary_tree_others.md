---
comments: True
---

# Binary Tree Others

## Table of Contents

- [x] [297. Serialize and Deserialize Binary Tree](https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/) (Hard)
- [ ] [449. Serialize and Deserialize BST](https://leetcode.cn/problems/serialize-and-deserialize-bst/) (Medium)
- [ ] [652. Find Duplicate Subtrees](https://leetcode.cn/problems/find-duplicate-subtrees/) (Medium)
- [x] [173. Binary Search Tree Iterator](https://leetcode.cn/problems/binary-search-tree-iterator/) (Medium)
- [ ] [1261. Find Elements in a Contaminated Binary Tree](https://leetcode.cn/problems/find-elements-in-a-contaminated-binary-tree/) (Medium)
- [ ] [1104. Path In Zigzag Labelled Binary Tree](https://leetcode.cn/problems/path-in-zigzag-labelled-binary-tree/) (Medium)
- [ ] [987. Vertical Order Traversal of a Binary Tree](https://leetcode.cn/problems/vertical-order-traversal-of-a-binary-tree/) (Hard)
- [ ] [655. Print Binary Tree](https://leetcode.cn/problems/print-binary-tree/) (Medium)
- [ ] [979. Distribute Coins in Binary Tree](https://leetcode.cn/problems/distribute-coins-in-binary-tree/) (Medium)
- [x] [222. Count Complete Tree Nodes](https://leetcode.cn/problems/count-complete-tree-nodes/) (Easy)
- [ ] [2049. Count Nodes With the Highest Score](https://leetcode.cn/problems/count-nodes-with-the-highest-score/) (Medium)
- [ ] [2673. Make Costs of Paths Equal in a Binary Tree](https://leetcode.cn/problems/make-costs-of-paths-equal-in-a-binary-tree/) (Medium)
- [ ] [2509. Cycle Length Queries in a Tree](https://leetcode.cn/problems/cycle-length-queries-in-a-tree/) (Hard)
- [ ] [2458. Height of Binary Tree After Subtree Removal Queries](https://leetcode.cn/problems/height-of-binary-tree-after-subtree-removal-queries/) (Hard)
- [ ] [314. Binary Tree Vertical Order Traversal](https://leetcode.cn/problems/binary-tree-vertical-order-traversal/) (Medium) 👑
- [ ] [666. Path Sum IV](https://leetcode.cn/problems/path-sum-iv/) (Medium) 👑
- [x] [1586. Binary Search Tree Iterator II](https://leetcode.cn/problems/binary-search-tree-iterator-ii/) (Medium) 👑
- [ ] [2773. Height of Special Binary Tree](https://leetcode.cn/problems/height-of-special-binary-tree/) (Medium) 👑
- [ ] [1485. Clone Binary Tree With Random Pointer](https://leetcode.cn/problems/clone-binary-tree-with-random-pointer/) (Medium) 👑
- [ ] [2445. Number of Nodes With Value One](https://leetcode.cn/problems/number-of-nodes-with-value-one/) (Medium) 👑
- [ ] [431. Encode N-ary Tree to Binary Tree](https://leetcode.cn/problems/encode-n-ary-tree-to-binary-tree/) (Hard) 👑
- [ ] [2005. Subtree Removal Game with Fibonacci Tree](https://leetcode.cn/problems/subtree-removal-game-with-fibonacci-tree/) (Hard) 👑

## 297. Serialize and Deserialize Binary Tree

-   [LeetCode](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/) (Hard)

-   Tags: string, tree, depth first search, breadth first search, design, binary tree
```python title="297. Serialize and Deserialize Binary Tree - Python Solution"
from collections import deque
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# BFS
class BFS:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        res = []
        q = deque([root])

        while q:
            node = q.popleft()

            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")

        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        index = 1

        while q:
            node = q.popleft()

            if nodes[index] != "null":
                node.left = TreeNode(int(nodes[index]))
                q.append(node.left)
            index += 1

            if nodes[index] != "null":
                node.right = TreeNode(int(nodes[index]))
                q.append(node.right)
            index += 1

        return root


# DFS
class DFS:
    def serialize(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if not node:
                return ["null"]
            return [str(node.val)] + dfs(node.left) + dfs(node.right)

        return ",".join(dfs(root))

    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        self.index = 0

        def dfs():
            if nodes[self.index] == "null":
                self.index += 1
                return None

            node = TreeNode(int(nodes[self.index]))
            self.index += 1

            node.left = dfs()
            node.right = dfs()

            return node

        root = dfs()
        return root


root = build([1, 2, 3, None, None, 4, 5])
print(root)
#   1__
#  /   \
# 2     3
#      / \
#     4   5

bfs = BFS()
data1 = bfs.serialize(root)
print(data1)  # "1,2,3,null,null,4,5,null,null,null,null"
root1 = bfs.deserialize(data1)
print(root1)
#   1__
#  /   \
# 2     3
#      / \
#     4   5

dfs = DFS()
data2 = dfs.serialize(root)
print(data2)  # "1,2,null,null,3,4,null,null,5,null,null"
root2 = dfs.deserialize(data2)
print(root2)
#   1__
#  /   \
# 2     3
#      / \
#     4   5

```

## 449. Serialize and Deserialize BST

-   [LeetCode](https://leetcode.com/problems/serialize-and-deserialize-bst/) | [LeetCode CH](https://leetcode.cn/problems/serialize-and-deserialize-bst/) (Medium)

-   Tags: string, tree, depth first search, breadth first search, design, binary search tree, binary tree
## 652. Find Duplicate Subtrees

-   [LeetCode](https://leetcode.com/problems/find-duplicate-subtrees/) | [LeetCode CH](https://leetcode.cn/problems/find-duplicate-subtrees/) (Medium)

-   Tags: hash table, tree, depth first search, binary tree
## 173. Binary Search Tree Iterator

-   [LeetCode](https://leetcode.com/problems/binary-search-tree-iterator/) | [LeetCode CH](https://leetcode.cn/problems/binary-search-tree-iterator/) (Medium)

-   Tags: stack, tree, design, binary search tree, binary tree, iterator
```python title="173. Binary Search Tree Iterator - Python Solution"
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

```

## 1261. Find Elements in a Contaminated Binary Tree

-   [LeetCode](https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/find-elements-in-a-contaminated-binary-tree/) (Medium)

-   Tags: hash table, tree, depth first search, breadth first search, design, binary tree
## 1104. Path In Zigzag Labelled Binary Tree

-   [LeetCode](https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/path-in-zigzag-labelled-binary-tree/) (Medium)

-   Tags: math, tree, binary tree
## 987. Vertical Order Traversal of a Binary Tree

-   [LeetCode](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/vertical-order-traversal-of-a-binary-tree/) (Hard)

-   Tags: hash table, tree, depth first search, breadth first search, sorting, binary tree
## 655. Print Binary Tree

-   [LeetCode](https://leetcode.com/problems/print-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/print-binary-tree/) (Medium)

-   Tags: tree, depth first search, breadth first search, binary tree
## 979. Distribute Coins in Binary Tree

-   [LeetCode](https://leetcode.com/problems/distribute-coins-in-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/distribute-coins-in-binary-tree/) (Medium)

-   Tags: tree, depth first search, binary tree
## 222. Count Complete Tree Nodes

-   [LeetCode](https://leetcode.com/problems/count-complete-tree-nodes/) | [LeetCode CH](https://leetcode.cn/problems/count-complete-tree-nodes/) (Easy)

-   Tags: binary search, bit manipulation, tree, binary tree
```python title="222. Count Complete Tree Nodes - Python Solution"
from collections import deque
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# Recursive
def countNodesRecursive(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    num = 1 + countNodesRecursive(root.left) + countNodesRecursive(root.right)

    return num


# Iterative
def countNodesIterative(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    q = deque([root])
    count = 0

    while q:
        n = len(q)

        for _ in range(n):
            node = q.popleft()
            count += 1

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return count


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# | Recursive  |  O(n)  |  O(n)   |
# | Iterative  |  O(n)  |  O(n)   |
# |------------|--------|---------|

root = [1, 2, 3, 4, 5, 6]
root = build(root)
print(root)
#     __1__
#    /     \
#   2       3
#  / \     /
# 4   5   6
print(countNodesRecursive(root))  # 6
print(countNodesIterative(root))  # 6

```

## 2049. Count Nodes With the Highest Score

-   [LeetCode](https://leetcode.com/problems/count-nodes-with-the-highest-score/) | [LeetCode CH](https://leetcode.cn/problems/count-nodes-with-the-highest-score/) (Medium)

-   Tags: array, tree, depth first search, binary tree
## 2673. Make Costs of Paths Equal in a Binary Tree

-   [LeetCode](https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/make-costs-of-paths-equal-in-a-binary-tree/) (Medium)

-   Tags: array, dynamic programming, greedy, tree, binary tree
## 2509. Cycle Length Queries in a Tree

-   [LeetCode](https://leetcode.com/problems/cycle-length-queries-in-a-tree/) | [LeetCode CH](https://leetcode.cn/problems/cycle-length-queries-in-a-tree/) (Hard)

-   Tags: array, tree, binary tree
## 2458. Height of Binary Tree After Subtree Removal Queries

-   [LeetCode](https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/) | [LeetCode CH](https://leetcode.cn/problems/height-of-binary-tree-after-subtree-removal-queries/) (Hard)

-   Tags: array, tree, depth first search, breadth first search, binary tree
## 314. Binary Tree Vertical Order Traversal

-   [LeetCode](https://leetcode.com/problems/binary-tree-vertical-order-traversal/) | [LeetCode CH](https://leetcode.cn/problems/binary-tree-vertical-order-traversal/) (Medium)

-   Tags: hash table, tree, depth first search, breadth first search, sorting, binary tree
## 666. Path Sum IV

-   [LeetCode](https://leetcode.com/problems/path-sum-iv/) | [LeetCode CH](https://leetcode.cn/problems/path-sum-iv/) (Medium)

-   Tags: array, hash table, tree, depth first search, binary tree
## 1586. Binary Search Tree Iterator II

-   [LeetCode](https://leetcode.com/problems/binary-search-tree-iterator-ii/) | [LeetCode CH](https://leetcode.cn/problems/binary-search-tree-iterator-ii/) (Medium)

-   Tags: stack, tree, design, binary search tree, binary tree, iterator
```python title="1586. Binary Search Tree Iterator II - Python Solution"
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


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

```

## 2773. Height of Special Binary Tree

-   [LeetCode](https://leetcode.com/problems/height-of-special-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/height-of-special-binary-tree/) (Medium)

-   Tags: tree, depth first search, breadth first search, binary tree
## 1485. Clone Binary Tree With Random Pointer

-   [LeetCode](https://leetcode.com/problems/clone-binary-tree-with-random-pointer/) | [LeetCode CH](https://leetcode.cn/problems/clone-binary-tree-with-random-pointer/) (Medium)

-   Tags: hash table, tree, depth first search, breadth first search, binary tree
## 2445. Number of Nodes With Value One

-   [LeetCode](https://leetcode.com/problems/number-of-nodes-with-value-one/) | [LeetCode CH](https://leetcode.cn/problems/number-of-nodes-with-value-one/) (Medium)

-   Tags: tree, depth first search, breadth first search, binary tree
## 431. Encode N-ary Tree to Binary Tree

-   [LeetCode](https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/encode-n-ary-tree-to-binary-tree/) (Hard)

-   Tags: tree, depth first search, breadth first search, design, binary tree
## 2005. Subtree Removal Game with Fibonacci Tree

-   [LeetCode](https://leetcode.com/problems/subtree-removal-game-with-fibonacci-tree/) | [LeetCode CH](https://leetcode.cn/problems/subtree-removal-game-with-fibonacci-tree/) (Hard)

-   Tags: math, dynamic programming, tree, binary tree, game theory
