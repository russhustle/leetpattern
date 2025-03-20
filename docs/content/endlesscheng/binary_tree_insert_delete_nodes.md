---
comments: True
---

# Binary Tree Insert Delete Nodes

## Table of Contents

- [x] [701. Insert into a Binary Search Tree](https://leetcode.cn/problems/insert-into-a-binary-search-tree/) (Medium)
- [x] [450. Delete Node in a BST](https://leetcode.cn/problems/delete-node-in-a-bst/) (Medium)
- [x] [669. Trim a Binary Search Tree](https://leetcode.cn/problems/trim-a-binary-search-tree/) (Medium)
- [ ] [776. Split BST](https://leetcode.cn/problems/split-bst/) (Medium) 👑
- [ ] [1666. Change the Root of a Binary Tree](https://leetcode.cn/problems/change-the-root-of-a-binary-tree/) (Medium) 👑

## 701. Insert into a Binary Search Tree

-   [LeetCode](https://leetcode.com/problems/insert-into-a-binary-search-tree/) | [LeetCode CH](https://leetcode.cn/problems/insert-into-a-binary-search-tree/) (Medium)

-   Tags: tree, binary search tree, binary tree

```python title="701. Insert into a Binary Search Tree - Python Solution"
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertIntoBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root is None:
        return TreeNode(val)

    if root.val > val:
        root.left = insertIntoBST(root.left, val)
    if root.val < val:
        root.right = insertIntoBST(root.right, val)

    return root


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
#     __4
#    /   \
#   2     6
#  / \
# 1   3

insertIntoBST(root, 5)
#     __4
#    /   \
#   2     6
#  / \   /
# 1   3 5

```

## 450. Delete Node in a BST

-   [LeetCode](https://leetcode.com/problems/delete-node-in-a-bst/) | [LeetCode CH](https://leetcode.cn/problems/delete-node-in-a-bst/) (Medium)

-   Tags: tree, binary search tree, binary tree

```python title="450. Delete Node in a BST - Python Solution"
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deleteNode(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if root is None:
        return root

    if root.val == key:
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            cur = root.right
            while cur.left is not None:
                cur = cur.left
            cur.left = root.left
            return root.right

    if root.val > key:
        root.left = deleteNode(root.left, key)
    if root.val < key:
        root.right = deleteNode(root.right, key)

    return root


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)
#     __5
#    /   \
#   3     6
#  / \     \
# 2   4     7

deleteNode(root, 3)
#     __5
#    /   \
#   4     6
#  /       \
# 2         7

```

## 669. Trim a Binary Search Tree

-   [LeetCode](https://leetcode.com/problems/trim-a-binary-search-tree/) | [LeetCode CH](https://leetcode.cn/problems/trim-a-binary-search-tree/) (Medium)

-   Tags: tree, depth first search, binary search tree, binary tree

```python title="669. Trim a Binary Search Tree - Python Solution"
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def trimBST(
    root: Optional[TreeNode], low: int, high: int
) -> Optional[TreeNode]:
    if root is None:
        return None

    if root.val < low:
        return trimBST(root.right, low, high)
    if root.val > high:
        return trimBST(root.left, low, high)

    root.left = trimBST(root.left, low, high)
    root.right = trimBST(root.right, low, high)

    return root


root = TreeNode(3)
root.left = TreeNode(0)
root.right = TreeNode(4)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(1)
#     __3
#    /   \
#   0     4
#    \
#     2
#    /
#   1

trimBST(root, 1, 3)
#     __3
#    /
#   2
#  /
# 1

```

## 776. Split BST

-   [LeetCode](https://leetcode.com/problems/split-bst/) | [LeetCode CH](https://leetcode.cn/problems/split-bst/) (Medium)

-   Tags: tree, binary search tree, recursion, binary tree

## 1666. Change the Root of a Binary Tree

-   [LeetCode](https://leetcode.com/problems/change-the-root-of-a-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/change-the-root-of-a-binary-tree/) (Medium)

-   Tags: tree, depth first search, binary tree
