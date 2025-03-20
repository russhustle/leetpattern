---
comments: True
---

# Binary Tree Backtracking

## Table of Contents

- [x] [257. Binary Tree Paths](https://leetcode.cn/problems/binary-tree-paths/) (Easy)
- [ ] [113. Path Sum II](https://leetcode.cn/problems/path-sum-ii/) (Medium)
- [x] [437. Path Sum III](https://leetcode.cn/problems/path-sum-iii/) (Medium)

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

## 113. Path Sum II

-   [LeetCode](https://leetcode.com/problems/path-sum-ii/) | [LeetCode CH](https://leetcode.cn/problems/path-sum-ii/) (Medium)

-   Tags: backtracking, tree, depth first search, binary tree

## 437. Path Sum III

-   [LeetCode](https://leetcode.com/problems/path-sum-iii/) | [LeetCode CH](https://leetcode.cn/problems/path-sum-iii/) (Medium)

-   Tags: tree, depth first search, binary tree

```cpp title="437. Path Sum III - C++ Solution"
#include <iostream>
#include <unordered_map>
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
   public:
    int pathSum(TreeNode *root, int targetSum) {
        int res = 0;
        unordered_map<long long, int> cnt{{0, 1}};

        auto dfs = [&](auto &&self, TreeNode *node, long long cur) {
            if (!node) return;
            cur += node->val;

            if (cnt.find(cur - targetSum) != cnt.end())
                res += cnt[cur - targetSum];

            cnt[cur]++;
            self(self, node->left, cur);
            self(self, node->right, cur);
            cnt[cur]--;
        };

        dfs(dfs, root, 0);
        return res;
    }
};

int main() {
    Solution s;
    {
        TreeNode *root = new TreeNode(10);
        root->left = new TreeNode(5);
        root->right = new TreeNode(-3);
        root->left->left = new TreeNode(3);
        root->left->right = new TreeNode(2);
        root->right->right = new TreeNode(11);
        root->left->left->left = new TreeNode(3);
        root->left->left->right = new TreeNode(-2);
        root->left->right->right = new TreeNode(1);
        cout << s.pathSum(root, 8) << endl;  // 3
    }
    {
        TreeNode *root = new TreeNode(5);
        root->left = new TreeNode(4);
        root->right = new TreeNode(8);
        root->left->left = new TreeNode(11);
        root->right->left = new TreeNode(13);
        root->right->right = new TreeNode(4);
        root->left->left->left = new TreeNode(7);
        root->left->left->right = new TreeNode(2);
        root->right->right->left = new TreeNode(5);
        root->right->right->right = new TreeNode(1);
        cout << s.pathSum(root, 22) << endl;  // 3
    }
    return 0;
}

```
