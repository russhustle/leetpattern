---
comments: True
---

# Tree DP Tree Diameter

- [x] [543. Diameter of Binary Tree](https://leetcode.cn/problems/diameter-of-binary-tree/) (Easy)
- [ ] [687. Longest Univalue Path](https://leetcode.cn/problems/longest-univalue-path/) (Medium)
- [x] [124. Binary Tree Maximum Path Sum](https://leetcode.cn/problems/binary-tree-maximum-path-sum/) (Hard)
- [ ] [2385. Amount of Time for Binary Tree to Be Infected](https://leetcode.cn/problems/amount-of-time-for-binary-tree-to-be-infected/) (Medium)
- [ ] [2246. Longest Path With Different Adjacent Characters](https://leetcode.cn/problems/longest-path-with-different-adjacent-characters/) (Hard)
- [ ] [3203. Find Minimum Diameter After Merging Two Trees](https://leetcode.cn/problems/find-minimum-diameter-after-merging-two-trees/) (Hard)
- [ ] [1617. Count Subtrees With Max Distance Between Cities](https://leetcode.cn/problems/count-subtrees-with-max-distance-between-cities/) (Hard)
- [ ] [2538. Difference Between Maximum and Minimum Price Sum](https://leetcode.cn/problems/difference-between-maximum-and-minimum-price-sum/) (Hard)
- [x] [1522. Diameter of N-Ary Tree](https://leetcode.cn/problems/diameter-of-n-ary-tree/) (Medium) 👑
- [x] [1245. Tree Diameter](https://leetcode.cn/problems/tree-diameter/) (Medium) 👑
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

## 2246. Longest Path With Different Adjacent Characters

-   [LeetCode](https://leetcode.com/problems/longest-path-with-different-adjacent-characters/) | [LeetCode CH](https://leetcode.cn/problems/longest-path-with-different-adjacent-characters/) (Hard)

-   Tags: array, string, tree, depth first search, graph, topological sort

## 3203. Find Minimum Diameter After Merging Two Trees

-   [LeetCode](https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/) | [LeetCode CH](https://leetcode.cn/problems/find-minimum-diameter-after-merging-two-trees/) (Hard)

-   Tags: tree, depth first search, breadth first search, graph

## 1617. Count Subtrees With Max Distance Between Cities

-   [LeetCode](https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/) | [LeetCode CH](https://leetcode.cn/problems/count-subtrees-with-max-distance-between-cities/) (Hard)

-   Tags: dynamic programming, bit manipulation, tree, enumeration, bitmask

## 2538. Difference Between Maximum and Minimum Price Sum

-   [LeetCode](https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/) | [LeetCode CH](https://leetcode.cn/problems/difference-between-maximum-and-minimum-price-sum/) (Hard)

-   Tags: array, dynamic programming, tree, depth first search

## 1522. Diameter of N-Ary Tree

-   [LeetCode](https://leetcode.com/problems/diameter-of-n-ary-tree/) | [LeetCode CH](https://leetcode.cn/problems/diameter-of-n-ary-tree/) (Medium)

-   Tags: tree, depth first search

```python title="1522. Diameter of N-Ary Tree - Python Solution"
from typing import List, Optional


class Node:
    def __init__(
        self,
        val: Optional[int] = None,
        children: Optional[List["Node"]] = None,
    ):
        self.val = val
        self.children = children if children is not None else []


def diameter(root: "Node") -> int:

    def dfs(node):
        if not node.children:
            return 1, 1
        mx0, mx1 = 0, 0
        mxf = 0
        for child in node.children:
            hl, fl = dfs(child)
            mxf = max(mxf, fl)
            if hl > mx1:
                if hl < mx0:
                    mx1 = hl
                else:
                    mx0, mx1 = hl, mx0
        return mx0 + 1, max(mxf, mx0 + mx1 + 1)

    return dfs(root)[1] - 1


root = [1, None, 2, None, 3, 4, None, 5, None, 6]
root = Node(1)
root.children = [Node(2)]
root.children[0].children = [Node(3), Node(4)]
root.children[0].children[0].children = [Node(5)]
root.children[0].children[1].children = [Node(6)]
print(diameter(root))  # 4

```

## 1245. Tree Diameter

-   [LeetCode](https://leetcode.com/problems/tree-diameter/) | [LeetCode CH](https://leetcode.cn/problems/tree-diameter/) (Medium)

-   Tags: tree, depth first search, breadth first search, graph, topological sort

```python title="1245. Tree Diameter - Python Solution"
from collections import defaultdict, deque
from typing import List


# Tree Diameter
def treeDiameter(edges: List[List[int]]) -> int:
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = {0}
    q = deque([0])
    cur = 0

    while q:
        size = len(q)
        for _ in range(size):
            cur = q.popleft()
            for nxt in graph[cur]:
                if nxt not in visited:
                    q.append(nxt)
                    visited.add(nxt)

    visited = {cur}
    q = deque([cur])
    res = -1

    while q:
        size = len(q)
        for _ in range(size):
            cur = q.popleft()
            for nxt in graph[cur]:
                if nxt not in visited:
                    q.append(nxt)
                    visited.add(nxt)
        res += 1

    return res


edges = [[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]
assert treeDiameter(edges) == 4

```

## 549. Binary Tree Longest Consecutive Sequence II

-   [LeetCode](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/) | [LeetCode CH](https://leetcode.cn/problems/binary-tree-longest-consecutive-sequence-ii/) (Medium)

-   Tags: tree, depth first search, binary tree
