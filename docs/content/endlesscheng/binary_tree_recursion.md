---
comments: True
---

# Binary Tree Recursion

## Table of Contents

- [x] [538. Convert BST to Greater Tree](https://leetcode.cn/problems/convert-bst-to-greater-tree/) (Medium)
- [ ] [1038. Binary Search Tree to Greater Sum Tree](https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree/) (Medium)
- [ ] [865. Smallest Subtree with all the Deepest Nodes](https://leetcode.cn/problems/smallest-subtree-with-all-the-deepest-nodes/) (Medium)
- [ ] [1080. Insufficient Nodes in Root to Leaf Paths](https://leetcode.cn/problems/insufficient-nodes-in-root-to-leaf-paths/) (Medium)

## 538. Convert BST to Greater Tree

-   [LeetCode](https://leetcode.com/problems/convert-bst-to-greater-tree/) | [LeetCode CH](https://leetcode.cn/problems/convert-bst-to-greater-tree/) (Medium)

-   Tags: tree, depth first search, binary search tree, binary tree
![538](https://assets.leetcode.com/uploads/2019/05/02/tree.png)

```python title="538. Convert BST to Greater Tree - Python Solution"
from typing import Optional

from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def convertBST(root: Optional[TreeNode]) -> Optional[TreeNode]:
    prev = 0

    def dfs(node):
        if not node:
            return None
        nonlocal prev

        dfs(node.right)

        node.val += prev
        prev = node.val

        dfs(node.left)

    dfs(root)

    return root


root = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
root = build(root)
print(root)
#     ____4__
#    /       \
#   1         6
#  / \       / \
# 0   2     5   7
#      \         \
#       3         8
greater_tree = convertBST(root)
print(greater_tree)
#      _______30___
#     /            \
#   _36            _21
#  /   \          /   \
# 36    35       26    15
#         \              \
#          33             8

```

## 1038. Binary Search Tree to Greater Sum Tree

-   [LeetCode](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/) | [LeetCode CH](https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree/) (Medium)

-   Tags: tree, depth first search, binary search tree, binary tree

## 865. Smallest Subtree with all the Deepest Nodes

-   [LeetCode](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/) | [LeetCode CH](https://leetcode.cn/problems/smallest-subtree-with-all-the-deepest-nodes/) (Medium)

-   Tags: hash table, tree, depth first search, breadth first search, binary tree

## 1080. Insufficient Nodes in Root to Leaf Paths

-   [LeetCode](https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/) | [LeetCode CH](https://leetcode.cn/problems/insufficient-nodes-in-root-to-leaf-paths/) (Medium)

-   Tags: tree, depth first search, binary tree
