---
comments: True
---

# Binary Tree Top-Down DFS

## Table of Contents

- [x] [104. Maximum Depth of Binary Tree](https://leetcode.cn/problems/maximum-depth-of-binary-tree/) (Easy)
- [x] [111. Minimum Depth of Binary Tree](https://leetcode.cn/problems/minimum-depth-of-binary-tree/) (Easy)
- [x] [112. Path Sum](https://leetcode.cn/problems/path-sum/) (Easy)
- [x] [129. Sum Root to Leaf Numbers](https://leetcode.cn/problems/sum-root-to-leaf-numbers/) (Medium)
- [x] [199. Binary Tree Right Side View](https://leetcode.cn/problems/binary-tree-right-side-view/) (Medium)
- [x] [1448. Count Good Nodes in Binary Tree](https://leetcode.cn/problems/count-good-nodes-in-binary-tree/) (Medium)
- [ ] [1457. Pseudo-Palindromic Paths in a Binary Tree](https://leetcode.cn/problems/pseudo-palindromic-paths-in-a-binary-tree/) (Medium)
- [ ] [1315. Sum of Nodes with Even-Valued Grandparent](https://leetcode.cn/problems/sum-of-nodes-with-even-valued-grandparent/) (Medium)
- [ ] [988. Smallest String Starting From Leaf](https://leetcode.cn/problems/smallest-string-starting-from-leaf/) (Medium)
- [ ] [1026. Maximum Difference Between Node and Ancestor](https://leetcode.cn/problems/maximum-difference-between-node-and-ancestor/) (Medium)
- [ ] [1022. Sum of Root To Leaf Binary Numbers](https://leetcode.cn/problems/sum-of-root-to-leaf-binary-numbers/) (Easy)
- [ ] [623. Add One Row to Tree](https://leetcode.cn/problems/add-one-row-to-tree/) (Medium)
- [ ] [1372. Longest ZigZag Path in a Binary Tree](https://leetcode.cn/problems/longest-zigzag-path-in-a-binary-tree/) (Medium)
- [ ] [971. Flip Binary Tree To Match Preorder Traversal](https://leetcode.cn/problems/flip-binary-tree-to-match-preorder-traversal/) (Medium)
- [ ] [2689. Extract Kth Character From The Rope Tree](https://leetcode.cn/problems/extract-kth-character-from-the-rope-tree/) (Easy) 👑
- [x] [298. Binary Tree Longest Consecutive Sequence](https://leetcode.cn/problems/binary-tree-longest-consecutive-sequence/) (Medium) 👑
- [ ] [1430. Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree](https://leetcode.cn/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/) (Medium) 👑
- [ ] [545. Boundary of Binary Tree](https://leetcode.cn/problems/boundary-of-binary-tree/) (Medium) 👑

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
print(maxDepthRecursive(root))  # 4
print(maxDepthIterative(root))  # 4
print(maxDepthDFS(root))  # 4

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

## 112. Path Sum

-   [LeetCode](https://leetcode.com/problems/path-sum/) | [LeetCode CH](https://leetcode.cn/problems/path-sum/) (Easy)

-   Tags: tree, depth first search, breadth first search, binary tree

```python title="112. Path Sum - Python Solution"
from typing import Optional

from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive
def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False

    if not root.left and not root.right:
        return root.val == targetSum

    targetSum -= root.val

    return hasPathSum(root.left, targetSum) or hasPathSum(
        root.right, targetSum
    )


root = build([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1])
print(root)
#          5___
#         /    \
#     ___4     _8
#    /        /  \
#   11       13   4
#  /  \            \
# 7    2            1
print(hasPathSum(root, 22))  # True

```

## 129. Sum Root to Leaf Numbers

-   [LeetCode](https://leetcode.com/problems/sum-root-to-leaf-numbers/) | [LeetCode CH](https://leetcode.cn/problems/sum-root-to-leaf-numbers/) (Medium)

-   Tags: tree, depth first search, binary tree

```python title="129. Sum Root to Leaf Numbers - Python Solution"
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
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


root = [1, 2, 3]
root = build(root)
print(root)
#   1
#  / \
# 2   3
print(Solution().sumNumbers(root))  # 25

```

## 199. Binary Tree Right Side View

-   [LeetCode](https://leetcode.com/problems/binary-tree-right-side-view/) | [LeetCode CH](https://leetcode.cn/problems/binary-tree-right-side-view/) (Medium)

-   Tags: tree, depth first search, breadth first search, binary tree
```plaintext
    ____1       <---
   /     \
  2__     2     <--- Look at the rightmost node at each level
 /   \     \
3     4     3   <---
     /
    5           <---
```

```python title="199. Binary Tree Right Side View - Python Solution"
from collections import deque
from typing import List, Optional

from binarytree import Node as TreeNode
from binarytree import build


# Binary Tree
def rightSideView(root: Optional[TreeNode]) -> List[int]:
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
print(rightSideView(root))  # [1, 2, 3, 5]

```

## 1448. Count Good Nodes in Binary Tree

-   [LeetCode](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/count-good-nodes-in-binary-tree/) (Medium)

-   Tags: tree, depth first search, breadth first search, binary tree

```python title="1448. Count Good Nodes in Binary Tree - Python Solution"
from typing import List

from binarytree import Node as TreeNode
from binarytree import build


# Tree
def goodNodes(root: TreeNode) -> int:
    def dfs(node, max_val):
        if not node:
            return 0

        good = 1 if node.val >= max_val else 0

        max_val = max(max_val, node.val)

        good += dfs(node.left, max_val)
        good += dfs(node.right, max_val)

        return good

    return dfs(root, root.val)


root = build([3, 1, 4, 3, None, 1, 5])
print(root)
#     3__
#    /   \
#   1     4
#  /     / \
# 3     1   5
print(goodNodes(root))  # 4

```

## 1457. Pseudo-Palindromic Paths in a Binary Tree

-   [LeetCode](https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/pseudo-palindromic-paths-in-a-binary-tree/) (Medium)

-   Tags: bit manipulation, tree, depth first search, breadth first search, binary tree

## 1315. Sum of Nodes with Even-Valued Grandparent

-   [LeetCode](https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-nodes-with-even-valued-grandparent/) (Medium)

-   Tags: tree, depth first search, breadth first search, binary tree

## 988. Smallest String Starting From Leaf

-   [LeetCode](https://leetcode.com/problems/smallest-string-starting-from-leaf/) | [LeetCode CH](https://leetcode.cn/problems/smallest-string-starting-from-leaf/) (Medium)

-   Tags: string, backtracking, tree, depth first search, binary tree

## 1026. Maximum Difference Between Node and Ancestor

-   [LeetCode](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/) | [LeetCode CH](https://leetcode.cn/problems/maximum-difference-between-node-and-ancestor/) (Medium)

-   Tags: tree, depth first search, binary tree

## 1022. Sum of Root To Leaf Binary Numbers

-   [LeetCode](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-root-to-leaf-binary-numbers/) (Easy)

-   Tags: tree, depth first search, binary tree

## 623. Add One Row to Tree

-   [LeetCode](https://leetcode.com/problems/add-one-row-to-tree/) | [LeetCode CH](https://leetcode.cn/problems/add-one-row-to-tree/) (Medium)

-   Tags: tree, depth first search, breadth first search, binary tree

## 1372. Longest ZigZag Path in a Binary Tree

-   [LeetCode](https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/longest-zigzag-path-in-a-binary-tree/) (Medium)

-   Tags: dynamic programming, tree, depth first search, binary tree

## 971. Flip Binary Tree To Match Preorder Traversal

-   [LeetCode](https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/) | [LeetCode CH](https://leetcode.cn/problems/flip-binary-tree-to-match-preorder-traversal/) (Medium)

-   Tags: tree, depth first search, binary tree

## 2689. Extract Kth Character From The Rope Tree

-   [LeetCode](https://leetcode.com/problems/extract-kth-character-from-the-rope-tree/) | [LeetCode CH](https://leetcode.cn/problems/extract-kth-character-from-the-rope-tree/) (Easy)

-   Tags: tree, depth first search, binary tree

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

## 1430. Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree

-   [LeetCode](https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/) (Medium)

-   Tags: tree, depth first search, breadth first search, binary tree

## 545. Boundary of Binary Tree

-   [LeetCode](https://leetcode.com/problems/boundary-of-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/boundary-of-binary-tree/) (Medium)

-   Tags: tree, depth first search, binary tree
