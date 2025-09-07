---
comments: True
---

# Divide and Conquer

## Table of Contents

- [x] [108. Convert Sorted Array to Binary Search Tree](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/) (Easy)
- [x] [148. Sort List](https://leetcode.cn/problems/sort-list/) (Medium)
- [ ] [427. Construct Quad Tree](https://leetcode.cn/problems/construct-quad-tree/) (Medium)
- [x] [23. Merge k Sorted Lists](https://leetcode.cn/problems/merge-k-sorted-lists/) (Hard)

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

## 148. Sort List

-   [LeetCode](https://leetcode.com/problems/sort-list/) | [LeetCode CH](https://leetcode.cn/problems/sort-list/) (Medium)

-   Tags: linked list, two pointers, divide and conquer, sorting, merge sort
```python title="148. Sort List - Python Solution"
from typing import Optional

from leetpattern.utils import ListNode, list_from_array


# Linked List
def sortListSort(head: Optional[ListNode]) -> Optional[ListNode]:
    nums = []

    while head:
        nums.append(head.val)
        head = head.next

    dummy = ListNode()
    cur = dummy
    nums.sort()

    for num in nums:
        cur.next = ListNode(val=num)
        cur = cur.next

    return dummy.next


# Linked List
def sortListDivideConquer(head: Optional[ListNode]) -> Optional[ListNode]:
    def middle(node):
        fast, slow = node, node
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        return slow

    def merge_two_lists(l1, l2):
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 if l1 else l2
        return dummy.next

    if not head or not head.next:
        return head

    head2 = middle(head)
    head = sortListDivideConquer(head)
    head2 = sortListDivideConquer(head2)

    return merge_two_lists(head, head2)


head = list_from_array([4, 2, 1, 3])
print(head)  # 4 -> 2 -> 1 -> 3
print(sortListSort(head))  # 1 -> 2 -> 3 -> 4
print(sortListDivideConquer(head))  # 1 -> 2 -> 3 -> 4

```

## 427. Construct Quad Tree

-   [LeetCode](https://leetcode.com/problems/construct-quad-tree/) | [LeetCode CH](https://leetcode.cn/problems/construct-quad-tree/) (Medium)

-   Tags: array, divide and conquer, tree, matrix
## 23. Merge k Sorted Lists

-   [LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/) | [LeetCode CH](https://leetcode.cn/problems/merge-k-sorted-lists/) (Hard)

-   Tags: linked list, divide and conquer, heap priority queue, merge sort
-   Prerequisite: 21. Merge Two Sorted Lists
-   Video explanation: [23. Merge K Sorted Lists - NeetCode](https://youtu.be/q5a5OiGbT6Q?si=SQ2dCvsYQ3LQctPh)

```python title="23. Merge k Sorted Lists - Python Solution"
import copy
import heapq
from typing import List, Optional

from leetpattern.utils import ListNode, list_from_array, list_to_array


def merge_k_lists_divide_conquer(
    lists: List[Optional[ListNode]],
) -> Optional[ListNode]:
    if not lists or len(lists) == 0:
        return None

    def mergeTwo(l1, l2):
        dummy = ListNode()
        cur = dummy

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next

        cur.next = l1 if l1 else l2

        return dummy.next

    while len(lists) > 1:
        merged = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged.append(mergeTwo(l1, l2))

        lists = merged

    return lists[0]


def merge_k_lists_heap(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy

    min_heap = []  # (val, idx, node)

    for idx, head in enumerate(lists):
        if head:
            heapq.heappush(min_heap, (head.val, idx, head))

    while min_heap:
        _, idx, node = heapq.heappop(min_heap)
        cur.next = node
        cur = cur.next

        node = node.next
        if node:
            heapq.heappush(min_heap, (node.val, idx, node))

    return dummy.next


def test_merge_k_lists() -> None:
    n1 = list_from_array([1, 4])
    n2 = list_from_array([1, 3])
    n3 = list_from_array([2, 6])
    lists = [n1, n2, n3]
    lists1 = copy.deepcopy(lists)
    lists2 = copy.deepcopy(lists)
    assert (list_to_array(merge_k_lists_divide_conquer(lists1))) == [
        1,
        1,
        2,
        3,
        4,
        6,
    ]
    assert (list_to_array(merge_k_lists_heap(lists2))) == [1, 1, 2, 3, 4, 6]

```
