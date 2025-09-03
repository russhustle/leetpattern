---
comments: True
---

# Binary Search Tree

## Table of Contents

- [x] [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/) (Medium)
- [x] [98. Validate Binary Search Tree](https://leetcode.cn/problems/validate-binary-search-tree/) (Medium)
- [x] [230. Kth Smallest Element in a BST](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/) (Medium)

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

## 98. Validate Binary Search Tree

-   [LeetCode](https://leetcode.com/problems/validate-binary-search-tree/) | [LeetCode CH](https://leetcode.cn/problems/validate-binary-search-tree/) (Medium)

-   Tags: tree, depth first search, binary search tree, binary tree
```python title="98. Validate Binary Search Tree - Python Solution"
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


def isValidBST(root: Optional[TreeNode]) -> bool:
    inorder = []  # inorder traversal of BST

    def dfs(node):
        if not node:
            return None
        dfs(node.left)
        inorder.append(node.val)
        dfs(node.right)

    dfs(root)

    for i in range(1, len(inorder)):
        if inorder[i] <= inorder[i - 1]:
            return False

    return True


root = [5, 1, 4, None, None, 3, 6]
root = build(root)
print(root)
#   5__
#  /   \
# 1     4
#      / \
#     3   6
print(isValidBST(root))  # False
# [1, 5, 3, 4, 6]

```

```cpp title="98. Validate Binary Search Tree - C++ Solution"
#include <cassert>
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right)
        : val(x), left(left), right(right) {}
};

class Solution {
   private:
    vector<int> inorder;
    bool check(vector<int> inorder) {
        int n = inorder.size();
        if (n <= 1) return true;
        for (int i = 1; i < n; i++) {
            if (inorder[i] <= inorder[i - 1]) return false;
        }
        return true;
    }

   public:
    bool isValidBST(TreeNode *root) {
        auto dfs = [&](auto &&self, TreeNode *node) -> void {
            if (!node) return;

            self(self, node->left);
            inorder.push_back(node->val);
            self(self, node->right);
        };

        dfs(dfs, root);

        return check(inorder);
    }
};

int main() {
    Solution s;
    TreeNode *root = new TreeNode(2);
    root->left = new TreeNode(1);
    root->right = new TreeNode(3);
    assert(s.isValidBST(root) == true);

    root = new TreeNode(5);
    root->left = new TreeNode(1);
    root->right = new TreeNode(4);
    root->right->left = new TreeNode(3);
    root->right->right = new TreeNode(6);
    assert(s.isValidBST(root) == false);

    root = new TreeNode(5);
    root->left = new TreeNode(4);
    root->right = new TreeNode(6);
    root->right->left = new TreeNode(3);
    root->right->right = new TreeNode(7);
    assert(s.isValidBST(root) == false);

    return 0;
}
```

## 230. Kth Smallest Element in a BST

-   [LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | [LeetCode CH](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/) (Medium)

-   Tags: tree, depth first search, binary search tree, binary tree
```python title="230. Kth Smallest Element in a BST - Python Solution"
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# Recursive
def kthSmallestRecursive(root: Optional[TreeNode], k: int) -> int:
    inorder = []

    def dfs(node):
        if not node:
            return None
        dfs(node.left)
        inorder.append(node.val)
        dfs(node.right)

    dfs(root)
    return inorder[k - 1]


# Iteratve
def kthSmallestIteratve(root: Optional[TreeNode], k: int) -> int:
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if not k:
            return root.val
        root = root.right


if __name__ == "__main__":
    root = build([3, 1, 4, None, 2])
    k = 1
    assert kthSmallestRecursive(root, k) == 1
    assert kthSmallestIteratve(root, k) == 1

```
