---
comments: True
---

# Binary Tree Lowest Common Ancestor

- [x] [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/) (Medium)
- [x] [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/) (Medium)
- [ ] [1123. Lowest Common Ancestor of Deepest Leaves](https://leetcode.cn/problems/lowest-common-ancestor-of-deepest-leaves/) (Medium)
- [ ] [2096. Step-By-Step Directions From a Binary Tree Node to Another](https://leetcode.cn/problems/step-by-step-directions-from-a-binary-tree-node-to-another/) (Medium)
- [ ] [1740. Find Distance in a Binary Tree](https://leetcode.cn/problems/find-distance-in-a-binary-tree/) (Medium) 👑
- [ ] [1644. Lowest Common Ancestor of a Binary Tree II](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree-ii/) (Medium) 👑
- [ ] [1650. Lowest Common Ancestor of a Binary Tree III](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree-iii/) (Medium) 👑
- [ ] [1676. Lowest Common Ancestor of a Binary Tree IV](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree-iv/) (Medium) 👑

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

## 1123. Lowest Common Ancestor of Deepest Leaves

-   [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/) | [LeetCode CH](https://leetcode.cn/problems/lowest-common-ancestor-of-deepest-leaves/) (Medium)

-   Tags: hash table, tree, depth first search, breadth first search, binary tree

## 2096. Step-By-Step Directions From a Binary Tree Node to Another

-   [LeetCode](https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/) | [LeetCode CH](https://leetcode.cn/problems/step-by-step-directions-from-a-binary-tree-node-to-another/) (Medium)

-   Tags: string, tree, depth first search, binary tree

## 1740. Find Distance in a Binary Tree

-   [LeetCode](https://leetcode.com/problems/find-distance-in-a-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/find-distance-in-a-binary-tree/) (Medium)

-   Tags: hash table, tree, depth first search, breadth first search, binary tree

## 1644. Lowest Common Ancestor of a Binary Tree II

-   [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/) | [LeetCode CH](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree-ii/) (Medium)

-   Tags: tree, depth first search, binary tree

## 1650. Lowest Common Ancestor of a Binary Tree III

-   [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/) | [LeetCode CH](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree-iii/) (Medium)

-   Tags: hash table, two pointers, tree, binary tree

## 1676. Lowest Common Ancestor of a Binary Tree IV

-   [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/) | [LeetCode CH](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree-iv/) (Medium)

-   Tags: hash table, tree, depth first search, binary tree
