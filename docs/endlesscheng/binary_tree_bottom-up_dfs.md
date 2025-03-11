---
comments: True
---

# Binary Tree Bottom-Up DFS

- [x] [104. Maximum Depth of Binary Tree](https://leetcode.cn/problems/maximum-depth-of-binary-tree/) (Easy)
- [x] [111. Minimum Depth of Binary Tree](https://leetcode.cn/problems/minimum-depth-of-binary-tree/) (Easy)
- [ ] [965. Univalued Binary Tree](https://leetcode.cn/problems/univalued-binary-tree/) (Easy)
- [x] [100. Same Tree](https://leetcode.cn/problems/same-tree/) (Easy)
- [x] [101. Symmetric Tree](https://leetcode.cn/problems/symmetric-tree/) (Easy)
- [ ] [951. Flip Equivalent Binary Trees](https://leetcode.cn/problems/flip-equivalent-binary-trees/) (Medium)
- [ ] [1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree](https://leetcode.cn/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/) (Easy)
- [x] [110. Balanced Binary Tree](https://leetcode.cn/problems/balanced-binary-tree/) (Easy)
- [x] [226. Invert Binary Tree](https://leetcode.cn/problems/invert-binary-tree/) (Easy)
- [x] [617. Merge Two Binary Trees](https://leetcode.cn/problems/merge-two-binary-trees/) (Easy)
- [x] [2331. Evaluate Boolean Binary Tree](https://leetcode.cn/problems/evaluate-boolean-binary-tree/) (Easy)
- [ ] [508. Most Frequent Subtree Sum](https://leetcode.cn/problems/most-frequent-subtree-sum/) (Medium)
- [ ] [563. Binary Tree Tilt](https://leetcode.cn/problems/binary-tree-tilt/) (Easy)
- [ ] [606. Construct String from Binary Tree](https://leetcode.cn/problems/construct-string-from-binary-tree/) (Medium)
- [ ] [2265. Count Nodes Equal to Average of Subtree](https://leetcode.cn/problems/count-nodes-equal-to-average-of-subtree/) (Medium)
- [ ] [1026. Maximum Difference Between Node and Ancestor](https://leetcode.cn/problems/maximum-difference-between-node-and-ancestor/) (Medium)
- [ ] [3319. K-th Largest Perfect Subtree Size in Binary Tree](https://leetcode.cn/problems/k-th-largest-perfect-subtree-size-in-binary-tree/) (Medium)
- [ ] [1339. Maximum Product of Splitted Binary Tree](https://leetcode.cn/problems/maximum-product-of-splitted-binary-tree/) (Medium)
- [ ] [1372. Longest ZigZag Path in a Binary Tree](https://leetcode.cn/problems/longest-zigzag-path-in-a-binary-tree/) (Medium)
- [ ] [1145. Binary Tree Coloring Game](https://leetcode.cn/problems/binary-tree-coloring-game/) (Medium)
- [x] [572. Subtree of Another Tree](https://leetcode.cn/problems/subtree-of-another-tree/) (Easy)
- [ ] [1530. Number of Good Leaf Nodes Pairs](https://leetcode.cn/problems/number-of-good-leaf-nodes-pairs/) (Medium)
- [ ] [298. Binary Tree Longest Consecutive Sequence](https://leetcode.cn/problems/binary-tree-longest-consecutive-sequence/) (Medium) 👑
- [ ] [250. Count Univalue Subtrees](https://leetcode.cn/problems/count-univalue-subtrees/) (Medium) 👑
- [ ] [1973. Count Nodes Equal to Sum of Descendants](https://leetcode.cn/problems/count-nodes-equal-to-sum-of-descendants/) (Medium) 👑
- [ ] [663. Equal Tree Partition](https://leetcode.cn/problems/equal-tree-partition/) (Medium) 👑
- [ ] [1120. Maximum Average Subtree](https://leetcode.cn/problems/maximum-average-subtree/) (Medium) 👑
- [ ] [2792. Count Nodes That Are Great Enough](https://leetcode.cn/problems/count-nodes-that-are-great-enough/) (Hard) 👑
- [ ] [333. Largest BST Subtree](https://leetcode.cn/problems/largest-bst-subtree/) (Medium) 👑
- [ ] [366. Find Leaves of Binary Tree](https://leetcode.cn/problems/find-leaves-of-binary-tree/) (Medium) 👑
- [ ] [156. Binary Tree Upside Down](https://leetcode.cn/problems/binary-tree-upside-down/) (Medium) 👑
- [ ] [1612. Check If Two Expression Trees are Equivalent](https://leetcode.cn/problems/check-if-two-expression-trees-are-equivalent/) (Medium) 👑

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

## 965. Univalued Binary Tree

-   [LeetCode](https://leetcode.com/problems/univalued-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/univalued-binary-tree/) (Easy)

-   Tags: tree, depth first search, breadth first search, binary tree

## 100. Same Tree

-   [LeetCode](https://leetcode.com/problems/same-tree/) | [LeetCode CH](https://leetcode.cn/problems/same-tree/) (Easy)

-   Tags: tree, depth first search, breadth first search, binary tree

```python title="100. Same Tree - Python Solution"
from collections import deque
from typing import Optional

from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. Recursive
def isSameTreeRecursive(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False

    return isSameTreeRecursive(p.left, q.left) and isSameTreeRecursive(
        p.right, q.right
    )


# 2. Iterative with queue
def isSameTreeIterativeQueue(
    p: Optional[TreeNode], q: Optional[TreeNode]
) -> bool:
    queue = deque([(p, q)])

    while queue:
        p, q = queue.popleft()

        if not p and not q:
            continue
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        queue.append((p.left, q.left))
        queue.append((p.right, q.right))

    return True


# 3. Iterative with stack
def isSameTreeIterativeStack(
    p: Optional[TreeNode], q: Optional[TreeNode]
) -> bool:
    stack = [(p, q)]

    while stack:
        n1, n2 = stack.pop()

        if not n1 and not n2:
            continue
        if not n1 or not n2:
            return False
        if n1.val != n2.val:
            return False

        stack.append((n1.left, n2.left))
        stack.append((n1.right, n2.right))

    return True


p1 = build([1, 2, 3])
q1 = build([1, 2, 3])
p2 = build([1, 2])
q2 = build([1, None, 2])

print(isSameTreeRecursive(p1, q1))  # True
print(isSameTreeRecursive(p2, q2))  # False
print(isSameTreeIterativeQueue(p1, q1))  # True
print(isSameTreeIterativeQueue(p2, q2))  # False
print(isSameTreeIterativeStack(p1, q1))  # True
print(isSameTreeIterativeStack(p2, q2))  # False

```

## 101. Symmetric Tree

-   [LeetCode](https://leetcode.com/problems/symmetric-tree/) | [LeetCode CH](https://leetcode.cn/problems/symmetric-tree/) (Easy)

-   Tags: tree, depth first search, breadth first search, binary tree

```python title="101. Symmetric Tree - Python Solution"
from collections import deque
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# Recursive
def isSymmetricRecursive(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    def check(left, right):
        if left is right:
            return True
        if not left or not right or left.val != right.val:
            return False
        outside = check(left.left, right.right)
        inside = check(left.right, right.left)
        return outside and inside

    return check(root.left, root.right)


# Iterative
def isSymmetricIterative(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    q = deque()
    q.append(root.left)
    q.append(root.right)

    while q:
        left = q.popleft()
        right = q.popleft()

        if not left and not right:
            continue

        if not left or not right or left.val != right.val:
            return False

        q.append(left.left)
        q.append(right.right)
        q.append(left.right)
        q.append(right.left)

    return True


root = [1, 2, 2, 3, 4, 4, 3]
root = build(root)
print(root)
#     __1__
#    /     \
#   2       2
#  / \     / \
# 3   4   4   3
print(isSymmetricRecursive(root))  # True
print(isSymmetricIterative(root))  # True

```

## 951. Flip Equivalent Binary Trees

-   [LeetCode](https://leetcode.com/problems/flip-equivalent-binary-trees/) | [LeetCode CH](https://leetcode.cn/problems/flip-equivalent-binary-trees/) (Medium)

-   Tags: tree, depth first search, binary tree

## 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree

-   [LeetCode](https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/) | [LeetCode CH](https://leetcode.cn/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/) (Easy)

-   Tags: tree, depth first search, breadth first search, binary tree

## 110. Balanced Binary Tree

-   [LeetCode](https://leetcode.com/problems/balanced-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/balanced-binary-tree/) (Easy)

-   Tags: tree, depth first search, binary tree

```python title="110. Balanced Binary Tree - Python Solution"
from typing import Optional

from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive
def isBalanced(root: Optional[TreeNode]) -> bool:
    def getHeight(node):
        if not node:
            return 0

        # post order
        leftHeight = getHeight(node.left)
        rightHeight = getHeight(node.right)

        if leftHeight == -1 or rightHeight == -1:
            return -1

        if abs(leftHeight - rightHeight) > 1:
            return -1
        else:
            return 1 + max(leftHeight, rightHeight)

    if getHeight(root) != -1:
        return True
    else:
        return False


root = [3, 9, 20, None, None, 15, 7]
root = build(root)
print(root)
#   3___
#  /    \
# 9     _20
#      /   \
#     15    7
print(isBalanced(root))  # True

```

## 226. Invert Binary Tree

-   [LeetCode](https://leetcode.com/problems/invert-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/invert-binary-tree/) (Easy)

-   Tags: tree, depth first search, breadth first search, binary tree

```python title="226. Invert Binary Tree - Python Solution"
from typing import Optional

from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive
def invertTreeRecursive(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return root

    root.left, root.right = root.right, root.left

    invertTreeRecursive(root.left)
    invertTreeRecursive(root.right)

    return root


# Iterative
def invertTreeIterative(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return root

    stack = [root]

    while stack:
        node = stack.pop()

        node.left, node.right = node.right, node.left
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return root


root = build([4, 2, 7, 1, 3, 6, 9])
print(root)
#     __4__
#    /     \
#   2       7
#  / \     / \
# 1   3   6   9
invertedRecursive = invertTreeRecursive(root)
print(invertedRecursive)
#     __4__
#    /     \
#   7       2
#  / \     / \
# 9   6   3   1
root = build([4, 2, 7, 1, 3, 6, 9])
invertedIterative = invertTreeIterative(root)
print(invertedIterative)
#     __4__
#    /     \
#   7       2
#  / \     / \
# 9   6   3   1

```

## 617. Merge Two Binary Trees

-   [LeetCode](https://leetcode.com/problems/merge-two-binary-trees/) | [LeetCode CH](https://leetcode.cn/problems/merge-two-binary-trees/) (Easy)

-   Tags: tree, depth first search, breadth first search, binary tree

```python title="617. Merge Two Binary Trees - Python Solution"
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mergeTrees(
    root1: Optional[TreeNode], root2: Optional[TreeNode]
) -> Optional[TreeNode]:

    if not root1:
        return root2
    if not root2:
        return root1

    root = TreeNode()

    root.val += root1.val + root2.val
    root.left = mergeTrees(root1.left, root2.left)
    root.right = mergeTrees(root1.right, root2.right)

    return root


root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)
#     1
#    / \
#   3   2
#  /
# 5

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)
#     2
#    / \
#   1   3
#    \   \
#     4   7

root = mergeTrees(root1, root2)
#     3
#    / \
#   4   5
#  / \   \
# 5   4   7

```

## 2331. Evaluate Boolean Binary Tree

-   [LeetCode](https://leetcode.com/problems/evaluate-boolean-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/evaluate-boolean-binary-tree/) (Easy)

-   Tags: tree, depth first search, binary tree

```python title="2331. Evaluate Boolean Binary Tree - Python Solution"
from typing import Optional

from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive
def evaluateTree(root: Optional[TreeNode]) -> bool:
    if not root.left and not root.right:
        return root.val

    left = evaluateTree(root.left)
    right = evaluateTree(root.right)

    if root.val == 2:
        return left or right
    elif root.val == 3:
        return left and right


root = build([2, 1, 3, None, None, 0, 1])
print(root)
#   2__
#  /   \
# 1     3
#      / \
#     0   1
boolTree = build(["OR", "True", "AND", None, None, "False", "True"])
print(boolTree)
#    __OR_______
#   /           \
# True        __AND_
#            /      \
#         False     True
print(evaluateTree(root))  # 1

```

## 508. Most Frequent Subtree Sum

-   [LeetCode](https://leetcode.com/problems/most-frequent-subtree-sum/) | [LeetCode CH](https://leetcode.cn/problems/most-frequent-subtree-sum/) (Medium)

-   Tags: hash table, tree, depth first search, binary tree

## 563. Binary Tree Tilt

-   [LeetCode](https://leetcode.com/problems/binary-tree-tilt/) | [LeetCode CH](https://leetcode.cn/problems/binary-tree-tilt/) (Easy)

-   Tags: tree, depth first search, binary tree

## 606. Construct String from Binary Tree

-   [LeetCode](https://leetcode.com/problems/construct-string-from-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/construct-string-from-binary-tree/) (Medium)

-   Tags: string, tree, depth first search, binary tree

## 2265. Count Nodes Equal to Average of Subtree

-   [LeetCode](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/) | [LeetCode CH](https://leetcode.cn/problems/count-nodes-equal-to-average-of-subtree/) (Medium)

-   Tags: tree, depth first search, binary tree

## 1026. Maximum Difference Between Node and Ancestor

-   [LeetCode](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/) | [LeetCode CH](https://leetcode.cn/problems/maximum-difference-between-node-and-ancestor/) (Medium)

-   Tags: tree, depth first search, binary tree

## 3319. K-th Largest Perfect Subtree Size in Binary Tree

-   [LeetCode](https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/k-th-largest-perfect-subtree-size-in-binary-tree/) (Medium)

-   Tags: tree, depth first search, sorting, binary tree

## 1339. Maximum Product of Splitted Binary Tree

-   [LeetCode](https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/maximum-product-of-splitted-binary-tree/) (Medium)

-   Tags: tree, depth first search, binary tree

## 1372. Longest ZigZag Path in a Binary Tree

-   [LeetCode](https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/longest-zigzag-path-in-a-binary-tree/) (Medium)

-   Tags: dynamic programming, tree, depth first search, binary tree

## 1145. Binary Tree Coloring Game

-   [LeetCode](https://leetcode.com/problems/binary-tree-coloring-game/) | [LeetCode CH](https://leetcode.cn/problems/binary-tree-coloring-game/) (Medium)

-   Tags: tree, depth first search, binary tree

## 572. Subtree of Another Tree

-   [LeetCode](https://leetcode.com/problems/subtree-of-another-tree/) | [LeetCode CH](https://leetcode.cn/problems/subtree-of-another-tree/) (Easy)

-   Tags: tree, depth first search, string matching, binary tree, hash function

```python title="572. Subtree of Another Tree - Python Solution"
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# DFS - Tree
def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def isSameTree(p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

    if not root:
        return False

    return (
        isSameTree(root, subRoot)
        or isSubtree(root.left, subRoot)
        or isSubtree(root.right, subRoot)
    )


# |------------|---------|----------|
# | Approach   | Time    | Space    |
# |------------|---------|----------|
# | DFS        | O(n * m)| O(n)     |
# |------------|---------|----------|


root = build([3, 4, 5, 1, 2, None, None, None, None, 0])
subRoot = build([4, 1, 2])
print(root)
#     ____3
#    /     \
#   4__     5
#  /   \
# 1     2
#      /
#     0
print(subRoot)
#   4
#  / \
# 1   2
print(isSubtree(root, subRoot))  # False

```

## 1530. Number of Good Leaf Nodes Pairs

-   [LeetCode](https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/) | [LeetCode CH](https://leetcode.cn/problems/number-of-good-leaf-nodes-pairs/) (Medium)

-   Tags: tree, depth first search, binary tree

## 298. Binary Tree Longest Consecutive Sequence

-   [LeetCode](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/) | [LeetCode CH](https://leetcode.cn/problems/binary-tree-longest-consecutive-sequence/) (Medium)

-   Tags: tree, depth first search, binary tree

## 250. Count Univalue Subtrees

-   [LeetCode](https://leetcode.com/problems/count-univalue-subtrees/) | [LeetCode CH](https://leetcode.cn/problems/count-univalue-subtrees/) (Medium)

-   Tags: tree, depth first search, binary tree

## 1973. Count Nodes Equal to Sum of Descendants

-   [LeetCode](https://leetcode.com/problems/count-nodes-equal-to-sum-of-descendants/) | [LeetCode CH](https://leetcode.cn/problems/count-nodes-equal-to-sum-of-descendants/) (Medium)

-   Tags: tree, depth first search, binary tree

## 663. Equal Tree Partition

-   [LeetCode](https://leetcode.com/problems/equal-tree-partition/) | [LeetCode CH](https://leetcode.cn/problems/equal-tree-partition/) (Medium)

-   Tags: tree, depth first search, binary tree

## 1120. Maximum Average Subtree

-   [LeetCode](https://leetcode.com/problems/maximum-average-subtree/) | [LeetCode CH](https://leetcode.cn/problems/maximum-average-subtree/) (Medium)

-   Tags: tree, depth first search, binary tree

## 2792. Count Nodes That Are Great Enough

-   [LeetCode](https://leetcode.com/problems/count-nodes-that-are-great-enough/) | [LeetCode CH](https://leetcode.cn/problems/count-nodes-that-are-great-enough/) (Hard)

-   Tags: divide and conquer, tree, depth first search, binary tree

## 333. Largest BST Subtree

-   [LeetCode](https://leetcode.com/problems/largest-bst-subtree/) | [LeetCode CH](https://leetcode.cn/problems/largest-bst-subtree/) (Medium)

-   Tags: dynamic programming, tree, depth first search, binary search tree, binary tree

## 366. Find Leaves of Binary Tree

-   [LeetCode](https://leetcode.com/problems/find-leaves-of-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/find-leaves-of-binary-tree/) (Medium)

-   Tags: tree, depth first search, binary tree

## 156. Binary Tree Upside Down

-   [LeetCode](https://leetcode.com/problems/binary-tree-upside-down/) | [LeetCode CH](https://leetcode.cn/problems/binary-tree-upside-down/) (Medium)

-   Tags: tree, depth first search, binary tree

## 1612. Check If Two Expression Trees are Equivalent

-   [LeetCode](https://leetcode.com/problems/check-if-two-expression-trees-are-equivalent/) | [LeetCode CH](https://leetcode.cn/problems/check-if-two-expression-trees-are-equivalent/) (Medium)

-   Tags: hash table, tree, depth first search, binary tree, counting
