---
comments: True
---

# Binary Tree

## Table of Contents

- [x] [104. Maximum Depth of Binary Tree](https://leetcode.cn/problems/maximum-depth-of-binary-tree/) (Easy)
- [x] [100. Same Tree](https://leetcode.cn/problems/same-tree/) (Easy)
- [x] [226. Invert Binary Tree](https://leetcode.cn/problems/invert-binary-tree/) (Easy)
- [x] [101. Symmetric Tree](https://leetcode.cn/problems/symmetric-tree/) (Easy)
- [x] [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) (Medium)
- [x] [106. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) (Medium)
- [x] [117. Populating Next Right Pointers in Each Node II](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/) (Medium)
- [x] [114. Flatten Binary Tree to Linked List](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/) (Medium)
- [x] [112. Path Sum](https://leetcode.cn/problems/path-sum/) (Easy)
- [x] [129. Sum Root to Leaf Numbers](https://leetcode.cn/problems/sum-root-to-leaf-numbers/) (Medium)
- [x] [124. Binary Tree Maximum Path Sum](https://leetcode.cn/problems/binary-tree-maximum-path-sum/) (Hard)
- [x] [173. Binary Search Tree Iterator](https://leetcode.cn/problems/binary-search-tree-iterator/) (Medium)
- [x] [222. Count Complete Tree Nodes](https://leetcode.cn/problems/count-complete-tree-nodes/) (Easy)
- [x] [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/) (Medium)

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


if __name__ == "__main__":
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
    assert maxDepthRecursive(root) == 4
    assert maxDepthDFS(root) == 4
    assert maxDepthIterative(root) == 4

```

## 100. Same Tree

-   [LeetCode](https://leetcode.com/problems/same-tree/) | [LeetCode CH](https://leetcode.cn/problems/same-tree/) (Easy)

-   Tags: tree, depth first search, breadth first search, binary tree
```python title="100. Same Tree - Python Solution"
from collections import deque
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# 1. Recursive
def isSameTreeRecursive(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    elif not p or not q:
        return False
    elif p.val != q.val:
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


if __name__ == "__main__":
    p1 = build([1, 2, 3])
    q1 = build([1, 2, 3])
    p2 = build([1, 2])
    q2 = build([1, None, 2])

    assert isSameTreeRecursive(p1, q1) is True
    assert isSameTreeRecursive(p2, q2) is False
    assert isSameTreeIterativeQueue(p1, q1) is True
    assert isSameTreeIterativeQueue(p2, q2) is False
    assert isSameTreeIterativeStack(p1, q1) is True
    assert isSameTreeIterativeStack(p2, q2) is False

```

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

## 101. Symmetric Tree

-   [LeetCode](https://leetcode.com/problems/symmetric-tree/) | [LeetCode CH](https://leetcode.cn/problems/symmetric-tree/) (Easy)

-   Tags: tree, depth first search, breadth first search, binary tree
```python title="101. Symmetric Tree - Python Solution"
from collections import deque
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# Recursive
def is_symmetric_recursive(root: Optional[TreeNode]) -> bool:
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
def is_symmetric_iterative(root: Optional[TreeNode]) -> bool:
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


if __name__ == "__main__":
    root = [1, 2, 2, 3, 4, 4, 3]
    root = build(root)
    print(root)
    #     __1__
    #    /     \
    #   2       2
    #  / \     / \
    # 3   4   4   3
    assert is_symmetric_recursive(root) is True
    assert is_symmetric_iterative(root) is True

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

## 117. Populating Next Right Pointers in Each Node II

-   [LeetCode](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/) | [LeetCode CH](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/) (Medium)

-   Tags: linked list, tree, depth first search, breadth first search, binary tree
```python title="117. Populating Next Right Pointers in Each Node II - Python Solution"
from collections import deque


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: "Node") -> "Node":
    if not root:
        return root

    queue = deque([root])

    while queue:
        size = len(queue)
        prev = None

        for _ in range(size):
            node = queue.popleft()

            if prev:
                prev.next = node

            prev = node

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return root


# Binary tree creation
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(7)
#       1
#      / \
#     2   3
#    / \   \
#   4   5   7

# Connect the nodes
connect(root)
#       1 -> None
#      / \
#     2 -> 3 -> None
#    / \    \
#   4 -> 5 -> 7 -> None

assert root.next is None
assert root.left.next == root.right
assert root.right.next is None
assert root.left.left.next == root.left.right
assert root.left.right.next == root.right.right
assert root.right.right.next is None

print("All tests passed.")

```

## 114. Flatten Binary Tree to Linked List

-   [LeetCode](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) | [LeetCode CH](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/) (Medium)

-   Tags: linked list, stack, tree, depth first search, binary tree
```cpp title="114. Flatten Binary Tree to Linked List - C++ Solution"
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
    TreeNode* head;

   public:
    void flatten(TreeNode* root) {
        if (!root) return;

        flatten(root->right);
        flatten(root->left);
        root->left = nullptr;
        root->right = head;
        head = root;
    }
};
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

## 129. Sum Root to Leaf Numbers

-   [LeetCode](https://leetcode.com/problems/sum-root-to-leaf-numbers/) | [LeetCode CH](https://leetcode.cn/problems/sum-root-to-leaf-numbers/) (Medium)

-   Tags: tree, depth first search, binary tree
```python title="129. Sum Root to Leaf Numbers - Python Solution"
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node, cur):
            if not node:
                return
            cur = cur * 10 + node.val
            if not node.left and not node.right:
                self.res += cur
                return
            dfs(node.left, cur)
            dfs(node.right, cur)

        dfs(root, 0)

        return self.res


root = [1, 2, 3]
root = build(root)
print(root)
#   1
#  / \
# 2   3
print(Solution().sumNumbers(root))  # 25

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

## 173. Binary Search Tree Iterator

-   [LeetCode](https://leetcode.com/problems/binary-search-tree-iterator/) | [LeetCode CH](https://leetcode.cn/problems/binary-search-tree-iterator/) (Medium)

-   Tags: stack, tree, design, binary search tree, binary tree, iterator
```python title="173. Binary Search Tree Iterator - Python Solution"
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# BST
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        topmost_node = self.stack.pop()

        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)

        return topmost_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


root = build([7, 3, 15, None, None, 9, 20])
print(root)
#   7__
#  /   \
# 3     15
#      /  \
#     9    20
obj = BSTIterator(root)
print(obj.next())  # 3
print(obj.next())  # 7
print(obj.hasNext())  # True

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
