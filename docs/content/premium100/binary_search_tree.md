---
comments: True
---

# Binary Search Tree

## Table of Contents

- [ ] [270. Closest Binary Search Tree Value](https://leetcode.cn/problems/closest-binary-search-tree-value/) (Easy) 👑
- [ ] [272. Closest Binary Search Tree Value II](https://leetcode.cn/problems/closest-binary-search-tree-value-ii/) (Hard) 👑
- [x] [255. Verify Preorder Sequence in Binary Search Tree](https://leetcode.cn/problems/verify-preorder-sequence-in-binary-search-tree/) (Medium) 👑
- [ ] [1214. Two Sum BSTs](https://leetcode.cn/problems/two-sum-bsts/) (Medium) 👑
- [ ] [333. Largest BST Subtree](https://leetcode.cn/problems/largest-bst-subtree/) (Medium) 👑

## 270. Closest Binary Search Tree Value

-   [LeetCode](https://leetcode.com/problems/closest-binary-search-tree-value/) | [LeetCode CH](https://leetcode.cn/problems/closest-binary-search-tree-value/) (Easy)

-   Tags: binary search, tree, depth first search, binary search tree, binary tree
## 272. Closest Binary Search Tree Value II

-   [LeetCode](https://leetcode.com/problems/closest-binary-search-tree-value-ii/) | [LeetCode CH](https://leetcode.cn/problems/closest-binary-search-tree-value-ii/) (Hard)

-   Tags: two pointers, stack, tree, depth first search, binary search tree, heap priority queue, binary tree
## 255. Verify Preorder Sequence in Binary Search Tree

-   [LeetCode](https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/) | [LeetCode CH](https://leetcode.cn/problems/verify-preorder-sequence-in-binary-search-tree/) (Medium)

-   Tags: array, stack, tree, binary search tree, recursion, monotonic stack, binary tree
```python title="255. Verify Preorder Sequence in Binary Search Tree - Python Solution"
from typing import List


# BST
def verifyPreorder(preorder: List[int]) -> bool:
    stack = []
    low = float("-inf")

    for value in preorder:
        if value < low:
            return False
        while stack and value > stack[-1]:
            low = stack.pop()
        stack.append(value)

    return True


if __name__ == "__main__":
    assert verifyPreorder([8, 5, 1, 7, 10, 12]) is True
    assert verifyPreorder([8, 5, 4, 3, 2, 1]) is True

```

## 1214. Two Sum BSTs

-   [LeetCode](https://leetcode.com/problems/two-sum-bsts/) | [LeetCode CH](https://leetcode.cn/problems/two-sum-bsts/) (Medium)

-   Tags: two pointers, binary search, stack, tree, depth first search, binary search tree, binary tree
## 333. Largest BST Subtree

-   [LeetCode](https://leetcode.com/problems/largest-bst-subtree/) | [LeetCode CH](https://leetcode.cn/problems/largest-bst-subtree/) (Medium)

-   Tags: dynamic programming, tree, depth first search, binary search tree, binary tree
