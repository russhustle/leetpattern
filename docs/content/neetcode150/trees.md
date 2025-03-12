---
comments: True
---

# Trees

- [x] [226. Invert Binary Tree](https://leetcode.cn/problems/invert-binary-tree/) (Easy)
- [x] [104. Maximum Depth of Binary Tree](https://leetcode.cn/problems/maximum-depth-of-binary-tree/) (Easy)
- [x] [543. Diameter of Binary Tree](https://leetcode.cn/problems/diameter-of-binary-tree/) (Easy)
- [x] [110. Balanced Binary Tree](https://leetcode.cn/problems/balanced-binary-tree/) (Easy)
- [x] [100. Same Tree](https://leetcode.cn/problems/same-tree/) (Easy)
- [x] [572. Subtree of Another Tree](https://leetcode.cn/problems/subtree-of-another-tree/) (Easy)
- [x] [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/) (Medium)
- [x] [102. Binary Tree Level Order Traversal](https://leetcode.cn/problems/binary-tree-level-order-traversal/) (Medium)
- [x] [199. Binary Tree Right Side View](https://leetcode.cn/problems/binary-tree-right-side-view/) (Medium)
- [x] [1448. Count Good Nodes in Binary Tree](https://leetcode.cn/problems/count-good-nodes-in-binary-tree/) (Medium)
- [x] [98. Validate Binary Search Tree](https://leetcode.cn/problems/validate-binary-search-tree/) (Medium)
- [x] [230. Kth Smallest Element in a BST](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/) (Medium)
- [x] [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) (Medium)
- [x] [124. Binary Tree Maximum Path Sum](https://leetcode.cn/problems/binary-tree-maximum-path-sum/) (Hard)
- [x] [297. Serialize and Deserialize Binary Tree](https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/) (Hard)

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

## 102. Binary Tree Level Order Traversal

-   [LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [LeetCode CH](https://leetcode.cn/problems/binary-tree-level-order-traversal/) (Medium)

-   Tags: tree, breadth first search, binary tree

```python title="102. Binary Tree Level Order Traversal - Python Solution"
from collections import deque
from typing import List, Optional

from binarytree import Node as TreeNode
from binarytree import build


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    q = deque([root])
    res = []

    while q:
        level = []
        size = len(q)

        for _ in range(size):
            cur = q.popleft()
            level.append(cur.val)

            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        res.append(level)

    return res


tree = build([3, 9, 20, None, None, 15, 7])
print(tree)
#   3___
#  /    \
# 9     _20
#      /   \
#     15    7
print(levelOrder(tree))  # [[3], [9, 20], [15, 7]]

```

## 199. Binary Tree Right Side View

-   [LeetCode](https://leetcode.com/problems/binary-tree-right-side-view/) | [LeetCode CH](https://leetcode.cn/problems/binary-tree-right-side-view/) (Medium)

-   Tags: tree, depth first search, breadth first search, binary tree
```plaintext
    ____1       <---
   /     \
  2__     2     <--- Look at the rightmost node at each level
 /   \     \
3     4     3   <---
     /
    5           <---
```

```python title="199. Binary Tree Right Side View - Python Solution"
from collections import deque
from typing import List, Optional

from binarytree import Node as TreeNode
from binarytree import build


# Binary Tree
def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    q = deque([root])
    res = []

    while q:
        n = len(q)
        for i in range(n):
            node = q.popleft()
            if i == n - 1:
                res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return res


root = [1, 2, 2, 3, 4, None, 3, None, None, 5]
root = build(root)
print(root)
#     ____1
#    /     \
#   2__     2
#  /   \     \
# 3     4     3
#      /
#     5
print(rightSideView(root))  # [1, 2, 3, 5]

```

## 1448. Count Good Nodes in Binary Tree

-   [LeetCode](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/count-good-nodes-in-binary-tree/) (Medium)

-   Tags: tree, depth first search, breadth first search, binary tree

```python title="1448. Count Good Nodes in Binary Tree - Python Solution"
from typing import List

from binarytree import Node as TreeNode
from binarytree import build


# Tree
def goodNodes(root: TreeNode) -> int:
    def dfs(node, max_val):
        if not node:
            return 0

        good = 1 if node.val >= max_val else 0

        max_val = max(max_val, node.val)

        good += dfs(node.left, max_val)
        good += dfs(node.right, max_val)

        return good

    return dfs(root, root.val)


root = build([3, 1, 4, 3, None, 1, 5])
print(root)
#     3__
#    /   \
#   1     4
#  /     / \
# 3     1   5
print(goodNodes(root))  # 4

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


root = build([3, 1, 4, None, 2])
k = 1
print(root)
#   __3
#  /   \
# 1     4
#  \
#   2
print(kthSmallestRecursive(root, k))  # 1
print(kthSmallestIteratve(root, k))  # 1

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

## 297. Serialize and Deserialize Binary Tree

-   [LeetCode](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/) (Hard)

-   Tags: string, tree, depth first search, breadth first search, design, binary tree

```python title="297. Serialize and Deserialize Binary Tree - Python Solution"
from collections import deque
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# BFS
class BFS:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        res = []
        q = deque([root])

        while q:
            node = q.popleft()

            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")

        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        index = 1

        while q:
            node = q.popleft()

            if nodes[index] != "null":
                node.left = TreeNode(int(nodes[index]))
                q.append(node.left)
            index += 1

            if nodes[index] != "null":
                node.right = TreeNode(int(nodes[index]))
                q.append(node.right)
            index += 1

        return root


# DFS
class DFS:
    def serialize(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if not node:
                return ["null"]
            return [str(node.val)] + dfs(node.left) + dfs(node.right)

        return ",".join(dfs(root))

    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        self.index = 0

        def dfs():
            if nodes[self.index] == "null":
                self.index += 1
                return None

            node = TreeNode(int(nodes[self.index]))
            self.index += 1

            node.left = dfs()
            node.right = dfs()

            return node

        root = dfs()
        return root


root = build([1, 2, 3, None, None, 4, 5])
print(root)
#   1__
#  /   \
# 2     3
#      / \
#     4   5

bfs = BFS()
data1 = bfs.serialize(root)
print(data1)  # "1,2,3,null,null,4,5,null,null,null,null"
root1 = bfs.deserialize(data1)
print(root1)
#   1__
#  /   \
# 2     3
#      / \
#     4   5

dfs = DFS()
data2 = dfs.serialize(root)
print(data2)  # "1,2,null,null,3,4,null,null,5,null,null"
root2 = dfs.deserialize(data2)
print(root2)
#   1__
#  /   \
# 2     3
#      / \
#     4   5

```
