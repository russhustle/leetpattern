---
comments: True
---

# Binary Tree Diameter

- [x] [543. Diameter of Binary Tree](https://leetcode.cn/problems/diameter-of-binary-tree/) (Easy)
- [ ] [687. Longest Univalue Path](https://leetcode.cn/problems/longest-univalue-path/) (Medium)
- [x] [124. Binary Tree Maximum Path Sum](https://leetcode.cn/problems/binary-tree-maximum-path-sum/) (Hard)
- [ ] [2385. Amount of Time for Binary Tree to Be Infected](https://leetcode.cn/problems/amount-of-time-for-binary-tree-to-be-infected/) (Medium)
- [ ] [549. Binary Tree Longest Consecutive Sequence II](https://leetcode.cn/problems/binary-tree-longest-consecutive-sequence-ii/) (Medium) 👑

## 543. Diameter of Binary Tree

-   [LeetCode](https://leetcode.com/problems/diameter-of-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/diameter-of-binary-tree/) (Easy)

-   Tags: tree, depth first search, binary tree

```python title="543. Diameter of Binary Tree - Python Solution"
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# Tree DFS
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)

        dfs(root)

        return self.diameter


root = build([1, 2, 3, 4, 5])
print(root)
#     __1
#    /   \
#   2     3
#  / \
# 4   5
obj = Solution()
print(obj.diameterOfBinaryTree(root))  # 3

```

```cpp title="543. Diameter of Binary Tree - C++ Solution"
#include <algorithm>
#include <iostream>
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

int diameterOfBinaryTree(TreeNode* root) {
    int diameter = 0;

    auto dfs = [&](auto&& self, TreeNode* node) -> int {
        if (!node) return 0;
        int left = self(self, node->left);
        int right = self(self, node->right);

        diameter = max(diameter, left + right);

        return 1 + max(left, right);
    };

    dfs(dfs, root);
    return diameter;
}

int main() {
    // [1, 2, 3, 4, 5]
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    cout << diameterOfBinaryTree(root) << endl;  // 3

    return 0;
}

```

## 687. Longest Univalue Path

-   [LeetCode](https://leetcode.com/problems/longest-univalue-path/) | [LeetCode CH](https://leetcode.cn/problems/longest-univalue-path/) (Medium)

-   Tags: tree, depth first search, binary tree

## 124. Binary Tree Maximum Path Sum

-   [LeetCode](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | [LeetCode CH](https://leetcode.cn/problems/binary-tree-maximum-path-sum/) (Hard)

-   Tags: dynamic programming, tree, depth first search, binary tree

```python title="124. Binary Tree Maximum Path Sum - Python Solution"
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


def maxPathSum(root: Optional[TreeNode]) -> int:
    res = float("-inf")

    def dfs(node):
        if not node:
            return 0

        leftMax = max(dfs(node.left), 0)
        rightMax = max(dfs(node.right), 0)

        cur = node.val + leftMax + rightMax
        nonlocal res
        res = max(res, cur)

        return node.val + max(leftMax, rightMax)

    dfs(root)

    return res


root = build([-10, 9, 20, None, None, 15, 7])
print(root)
#   -10___
#  /      \
# 9       _20
#        /   \
#       15    7
print(maxPathSum(root))  # 42

```

## 2385. Amount of Time for Binary Tree to Be Infected

-   [LeetCode](https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/) | [LeetCode CH](https://leetcode.cn/problems/amount-of-time-for-binary-tree-to-be-infected/) (Medium)

-   Tags: hash table, tree, depth first search, breadth first search, binary tree

## 549. Binary Tree Longest Consecutive Sequence II

-   [LeetCode](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/) | [LeetCode CH](https://leetcode.cn/problems/binary-tree-longest-consecutive-sequence-ii/) (Medium)

-   Tags: tree, depth first search, binary tree
