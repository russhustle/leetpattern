---
comments: True
---

# Binary Tree Linked List

## Table of Contents

- [x] [114. Flatten Binary Tree to Linked List](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/) (Medium)
- [ ] [1367. Linked List in Binary Tree](https://leetcode.cn/problems/linked-list-in-binary-tree/) (Medium)
- [x] [109. Convert Sorted List to Binary Search Tree](https://leetcode.cn/problems/convert-sorted-list-to-binary-search-tree/) (Medium)
- [x] [116. Populating Next Right Pointers in Each Node](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/) (Medium)
- [x] [117. Populating Next Right Pointers in Each Node II](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/) (Medium)
- [ ] [426. Convert Binary Search Tree to Sorted Doubly Linked List](https://leetcode.cn/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/) (Medium) 👑

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

## 1367. Linked List in Binary Tree

-   [LeetCode](https://leetcode.com/problems/linked-list-in-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/linked-list-in-binary-tree/) (Medium)

-   Tags: linked list, tree, depth first search, binary tree

## 109. Convert Sorted List to Binary Search Tree

-   [LeetCode](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/) | [LeetCode CH](https://leetcode.cn/problems/convert-sorted-list-to-binary-search-tree/) (Medium)

-   Tags: linked list, divide and conquer, tree, binary search tree, binary tree
![109](https://assets.leetcode.com/uploads/2020/08/17/linked.jpg)

```python title="109. Convert Sorted List to Binary Search Tree - Python Solution"
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedListToBST(head: Optional[ListNode]) -> Optional[TreeNode]:
    if not head:
        return None

    def find_mid(head: ListNode) -> ListNode:
        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = None

        return slow

    mid = find_mid(head)

    node = TreeNode(mid.val)

    if head == mid:
        return node

    node.left = sortedListToBST(head)
    node.right = sortedListToBST(mid.next)

    return node


head = ListNode(-10)
head.next = ListNode(-3)
head.next.next = ListNode(0)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(9)

root = sortedListToBST(head)
assert root.val == 0
assert root.left.val == -3
assert root.left.left.val == -10
assert root.right.val == 9
assert root.right.left.val == 5
print("All passed")

#      0
#     / \
#   -3   9
#   /   /
# -10  5

```

## 116. Populating Next Right Pointers in Each Node

-   [LeetCode](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/) | [LeetCode CH](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/) (Medium)

-   Tags: linked list, tree, depth first search, breadth first search, binary tree
-   Perfect Binary Tree

```python title="116. Populating Next Right Pointers in Each Node - Python Solution"
from collections import deque
from typing import Optional


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


def connect(root: "Optional[Node]") -> "Optional[Node]":
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


# Perfect binary tree creation
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
#     __1__
#    /     \
#   2__     3
#  /   \   / \
# 4     5 6   7


# Connect the nodes
connect(root)
#      __1__ -> None
#     /     \
#   _2_ ->  3 -> None
#  /   \   / \
# 4 -> 5->6-> 7 -> None


assert root.next is None
assert root.left.next == root.right
assert root.left.left.next == root.left.right
assert root.left.right.next == root.right.left
assert root.right.left.next == root.right.right
assert root.right.right.next is None
print("All tests passed.")

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

## 426. Convert Binary Search Tree to Sorted Doubly Linked List

-   [LeetCode](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/) | [LeetCode CH](https://leetcode.cn/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/) (Medium)

-   Tags: linked list, stack, tree, depth first search, binary search tree, binary tree, doubly linked list
