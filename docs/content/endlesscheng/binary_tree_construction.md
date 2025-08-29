---
comments: True
---

# Binary Tree Construction

## Table of Contents

- [x] [108. Convert Sorted Array to Binary Search Tree](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/) (Easy)
- [x] [654. Maximum Binary Tree](https://leetcode.cn/problems/maximum-binary-tree/) (Medium)
- [ ] [998. Maximum Binary Tree II](https://leetcode.cn/problems/maximum-binary-tree-ii/) (Medium)
- [ ] [1008. Construct Binary Search Tree from Preorder Traversal](https://leetcode.cn/problems/construct-binary-search-tree-from-preorder-traversal/) (Medium)
- [ ] [1382. Balance a Binary Search Tree](https://leetcode.cn/problems/balance-a-binary-search-tree/) (Medium)
- [ ] [2196. Create Binary Tree From Descriptions](https://leetcode.cn/problems/create-binary-tree-from-descriptions/) (Medium)
- [x] [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) (Medium)
- [x] [106. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) (Medium)
- [ ] [889. Construct Binary Tree from Preorder and Postorder Traversal](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal/) (Medium)
- [ ] [1028. Recover a Tree From Preorder Traversal](https://leetcode.cn/problems/recover-a-tree-from-preorder-traversal/) (Hard)
- [ ] [536. Construct Binary Tree from String](https://leetcode.cn/problems/construct-binary-tree-from-string/) (Medium) 👑
- [ ] [1628. Design an Expression Tree With Evaluate Function](https://leetcode.cn/problems/design-an-expression-tree-with-evaluate-function/) (Medium) 👑
- [ ] [1597. Build Binary Expression Tree From Infix Expression](https://leetcode.cn/problems/build-binary-expression-tree-from-infix-expression/) (Hard) 👑

## 108. Convert Sorted Array to Binary Search Tree

-   [LeetCode](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) | [LeetCode CH](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/) (Easy)

-   Tags: array, divide and conquer, tree, binary search tree, binary tree
```python title="108. Convert Sorted Array to Binary Search Tree - Python Solution"
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    if len(nums) == 0:
        return None

    mid = len(nums) // 2
    root = TreeNode(nums[mid])

    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1 :])

    return root


nums = [-10, -3, 0, 5, 9]
root = sortedArrayToBST(nums)
#      0
#     / \
#   -3   9
#   /   /
# -10  5

```

```cpp title="108. Convert Sorted Array to Binary Search Tree - C++ Solution"
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
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        if (nums.size() == 0) return nullptr;

        int mid = nums.size() / 2;
        TreeNode* root = new TreeNode(nums[mid]);

        vector<int> left(nums.begin(), nums.begin() + mid);
        vector<int> right(nums.begin() + mid + 1, nums.end());

        root->left = sortedArrayToBST(left);
        root->right = sortedArrayToBST(right);

        return root;
    }
};

int main() { return 0; }
```

## 654. Maximum Binary Tree

-   [LeetCode](https://leetcode.com/problems/maximum-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/maximum-binary-tree/) (Medium)

-   Tags: array, divide and conquer, stack, tree, monotonic stack, binary tree
```python title="654. Maximum Binary Tree - Python Solution"
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def constructMaximumBinaryTree(nums: List[int]) -> Optional[TreeNode]:
    if len(nums) == 0:
        return None

    maximum = max(nums)
    rootIndex = nums.index(maximum)

    root = TreeNode(maximum)

    left_nums = nums[:rootIndex]
    right_nums = nums[rootIndex + 1 :]

    root.left = constructMaximumBinaryTree(left_nums)
    root.right = constructMaximumBinaryTree(right_nums)

    return root


nums = [3, 2, 1, 6, 0, 5]
root = constructMaximumBinaryTree(nums)
#     __6__
#    /     \
#   3       5
#    \     /
#     2   0
#      \
#       1

```

## 998. Maximum Binary Tree II

-   [LeetCode](https://leetcode.com/problems/maximum-binary-tree-ii/) | [LeetCode CH](https://leetcode.cn/problems/maximum-binary-tree-ii/) (Medium)

-   Tags: tree, binary tree
## 1008. Construct Binary Search Tree from Preorder Traversal

-   [LeetCode](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/) | [LeetCode CH](https://leetcode.cn/problems/construct-binary-search-tree-from-preorder-traversal/) (Medium)

-   Tags: array, stack, tree, binary search tree, monotonic stack, binary tree
## 1382. Balance a Binary Search Tree

-   [LeetCode](https://leetcode.com/problems/balance-a-binary-search-tree/) | [LeetCode CH](https://leetcode.cn/problems/balance-a-binary-search-tree/) (Medium)

-   Tags: divide and conquer, greedy, tree, depth first search, binary search tree, binary tree
## 2196. Create Binary Tree From Descriptions

-   [LeetCode](https://leetcode.com/problems/create-binary-tree-from-descriptions/) | [LeetCode CH](https://leetcode.cn/problems/create-binary-tree-from-descriptions/) (Medium)

-   Tags: array, hash table, tree, binary tree
## 105. Construct Binary Tree from Preorder and Inorder Traversal

-   [LeetCode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | [LeetCode CH](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) (Medium)

-   Tags: array, hash table, divide and conquer, tree, binary tree
```python title="105. Construct Binary Tree from Preorder and Inorder Traversal - Python Solution"
from typing import List, Optional

from helper import TreeNode


def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    """
    preorder  root left right  1  2  3
    inorder   left root right  4  5  6
    """
    if len(preorder) == 0:
        return None

    root_val = preorder[0]  # 1
    root = TreeNode(root_val)

    separator_idx = inorder.index(root_val)  # 5

    left_inorder = inorder[:separator_idx]  # 4
    right_inorder = inorder[separator_idx + 1 :]  # 6

    left_preorder = preorder[1 : 1 + len(left_inorder)]  # 2
    right_preorder = preorder[1 + len(left_inorder) :]  # 3

    root.left = buildTree(left_preorder, left_inorder)
    root.right = buildTree(right_preorder, right_inorder)

    return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
root = buildTree(preorder, inorder)
print(root)
#     3
#    / \
#   9  20
#     /  \
#    15   7

```

```cpp title="105. Construct Binary Tree from Preorder and Inorder Traversal - C++ Solution"
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
    vector<int> preorder;
    unordered_map<int, int> inorderMap;

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        this->preorder = preorder;
        for (size_t i = 0; i < inorder.size(); i++) {
            inorderMap[inorder[i]] = i;
        }
        return buildSubtree(0, 0, inorder.size() - 1);
    }

   private:
    TreeNode* buildSubtree(int rootIndex, int left, int right) {
        if (left > right) return nullptr;

        TreeNode* root = new TreeNode(preorder[rootIndex]);
        int inorderIndex = inorderMap[preorder[rootIndex]];

        root->left = buildSubtree(rootIndex + 1, left, inorderIndex - 1);
        root->right = buildSubtree(rootIndex + (inorderIndex - left + 1),
                                   inorderIndex + 1, right);

        return root;
    }
};

int main() {
    vector<int> preorder = {3, 9, 20, 15, 7};
    vector<int> inorder = {9, 3, 15, 20, 7};
    Solution solution;
    TreeNode* root = solution.buildTree(preorder, inorder);
    cout << root->val << endl;                // 3
    cout << root->left->val << endl;          // 9
    cout << root->right->val << endl;         // 20
    cout << root->right->left->val << endl;   // 15
    cout << root->right->right->val << endl;  // 7
    return 0;
}
```

## 106. Construct Binary Tree from Inorder and Postorder Traversal

-   [LeetCode](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) | [LeetCode CH](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) (Medium)

-   Tags: array, hash table, divide and conquer, tree, binary tree
```python title="106. Construct Binary Tree from Inorder and Postorder Traversal - Python Solution"
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    """
    inorder:    left root  right   1  2  3
    postorder:  left right root    4  5  6
    """

    if not postorder:
        return None

    root_val = postorder[-1]  # 6
    root = TreeNode(root_val)

    separator_idx = inorder.index(root_val)  # 2

    left_inorder = inorder[:separator_idx]  # 1
    right_inorder = inorder[separator_idx + 1 :]  # 3

    left_postorder = postorder[: len(left_inorder)]  # 4
    right_postorder = postorder[len(left_inorder) : -1]  # 5

    root.left = buildTree(left_inorder, left_postorder)
    root.right = buildTree(right_inorder, right_postorder)

    return root


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
root = buildTree(inorder, postorder)
print(root)
#     3
#    / \
#   9  20
#     /  \
#    15   7

```

## 889. Construct Binary Tree from Preorder and Postorder Traversal

-   [LeetCode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/) | [LeetCode CH](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal/) (Medium)

-   Tags: array, hash table, divide and conquer, tree, binary tree
## 1028. Recover a Tree From Preorder Traversal

-   [LeetCode](https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/) | [LeetCode CH](https://leetcode.cn/problems/recover-a-tree-from-preorder-traversal/) (Hard)

-   Tags: string, tree, depth first search, binary tree
## 536. Construct Binary Tree from String

-   [LeetCode](https://leetcode.com/problems/construct-binary-tree-from-string/) | [LeetCode CH](https://leetcode.cn/problems/construct-binary-tree-from-string/) (Medium)

-   Tags: string, stack, tree, depth first search, binary tree
## 1628. Design an Expression Tree With Evaluate Function

-   [LeetCode](https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/) | [LeetCode CH](https://leetcode.cn/problems/design-an-expression-tree-with-evaluate-function/) (Medium)

-   Tags: array, math, stack, tree, design, binary tree
## 1597. Build Binary Expression Tree From Infix Expression

-   [LeetCode](https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/) | [LeetCode CH](https://leetcode.cn/problems/build-binary-expression-tree-from-infix-expression/) (Hard)

-   Tags: string, stack, tree, binary tree
