---
comments: True
---

# Tree Feature

## Table of Contents

- [x] [101. Symmetric Tree](https://leetcode.cn/problems/symmetric-tree/) (Easy)
- [x] [222. Count Complete Tree Nodes](https://leetcode.cn/problems/count-complete-tree-nodes/) (Easy)
- [x] [110. Balanced Binary Tree](https://leetcode.cn/problems/balanced-binary-tree/) (Easy)
- [x] [257. Binary Tree Paths](https://leetcode.cn/problems/binary-tree-paths/) (Easy)
- [x] [404. Sum of Left Leaves](https://leetcode.cn/problems/sum-of-left-leaves/) (Easy)
- [x] [112. Path Sum](https://leetcode.cn/problems/path-sum/) (Easy)
- [x] [2331. Evaluate Boolean Binary Tree](https://leetcode.cn/problems/evaluate-boolean-binary-tree/) (Easy)
- [x] [100. Same Tree](https://leetcode.cn/problems/same-tree/) (Easy)
- [x] [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/) (Medium)
- [x] [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/) (Medium)

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

## 257. Binary Tree Paths

-   [LeetCode](https://leetcode.com/problems/binary-tree-paths/) | [LeetCode CH](https://leetcode.cn/problems/binary-tree-paths/) (Easy)

-   Tags: string, backtracking, tree, depth first search, binary tree

```python title="257. Binary Tree Paths - Python Solution"
from typing import List, Optional

from binarytree import Node as TreeNode
from binarytree import build


# Recursive
def binaryTreePaths(root: Optional[TreeNode]) -> List[str]:
    res = []

    def dfs(node, path):
        if not node:
            return
        path += str(node.val)

        if not node.left and not node.right:
            res.append(path)
            return

        path += "->"

        dfs(node.left, path)
        dfs(node.right, path)

    dfs(root, "")

    return res


root = build([1, 2, 3, None, 5])
print(root)
#   __1
#  /   \
# 2     3
#  \
#   5
print(binaryTreePaths(root))  # ['1->2->5', '1->3']

```

## 404. Sum of Left Leaves

-   [LeetCode](https://leetcode.com/problems/sum-of-left-leaves/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-left-leaves/) (Easy)

-   Tags: tree, depth first search, breadth first search, binary tree

```python title="404. Sum of Left Leaves - Python Solution"
from typing import Optional

from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative
def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    stack = [root]
    sumLL = 0

    while stack:
        node = stack.pop()

        if node.left and not node.left.left and not node.left.right:
            sumLL += node.left.val

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return sumLL


# Left Leave None:
#   - node.left is not None
#   - node.left.left is None
#   - node.left.right is None

root = build([3, 9, 20, None, None, 15, 7])
print(root)
#   3___
#  /    \
# 9     _20
#      /   \
#     15    7
print(sumOfLeftLeaves(root))  # 24

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

## 235. Lowest Common Ancestor of a Binary Search Tree

-   [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | [LeetCode CH](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/) (Medium)

-   Tags: tree, depth first search, binary search tree, binary tree

```python title="235. Lowest Common Ancestor of a Binary Search Tree - Python Solution"
from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(
    root: "TreeNode", p: "TreeNode", q: "TreeNode"
) -> "TreeNode":
    while root:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root


root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
root = build(root)
p = root.left
q = root.right
print(root)
#     ______6__
#    /         \
#   2__         8
#  /   \       / \
# 0     4     7   9
#      / \
#     3   5
print(lowestCommonAncestor(root, p, q))
#     ______6__
#    /         \
#   2__         8
#  /   \       / \
# 0     4     7   9
#      / \
#     3   5

```

## 236. Lowest Common Ancestor of a Binary Tree

-   [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/) (Medium)

-   Tags: tree, depth first search, binary tree

```python title="236. Lowest Common Ancestor of a Binary Tree - Python Solution"
from typing import List, Optional

from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(
    root: "TreeNode", p: "TreeNode", q: "TreeNode"
) -> "TreeNode":
    if not root or q == root or p == root:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root

    return left or right


root = build([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
print(root)
#     ______3__
#    /         \
#   5__         1
#  /   \       / \
# 6     2     0   8
#      / \
#     7   4
p = root.left  # 5
q = root.right  # 1
print(lowestCommonAncestor(root, p, q))  # 3
#     ______3__
#    /         \
#   5__         1
#  /   \       / \
# 6     2     0   8
#      / \
#     7   4
r = root.left.right.right  # 4
print(lowestCommonAncestor(root, p, r))  # 5
#   5__
#  /   \
# 6     2
#      / \
#     7   4

```

```cpp title="236. Lowest Common Ancestor of a Binary Tree - C++ Solution"
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right)
        : val(x), left(left), right(right) {}
};

class Solution {
   public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == nullptr || root == p || root == q) {
            return root;
        }

        TreeNode* left = lowestCommonAncestor(root->left, p, q);
        TreeNode* right = lowestCommonAncestor(root->right, p, q);

        if (left && right) {
            return root;
        }

        return left ? left : right;
    }
};

int main() { return 0; }

```
