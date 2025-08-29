---
comments: True
---

# Tree Modification

## Table of Contents

- [x] [226. Invert Binary Tree](https://leetcode.cn/problems/invert-binary-tree/) (Easy)
- [x] [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) (Medium)
- [x] [106. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) (Medium)
- [x] [654. Maximum Binary Tree](https://leetcode.cn/problems/maximum-binary-tree/) (Medium)
- [x] [617. Merge Two Binary Trees](https://leetcode.cn/problems/merge-two-binary-trees/) (Easy)

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

