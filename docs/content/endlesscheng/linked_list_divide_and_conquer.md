---
comments: True
---

# Linked List Divide and Conquer

## Table of Contents

- [x] [23. Merge k Sorted Lists](https://leetcode.cn/problems/merge-k-sorted-lists/) (Hard)
- [x] [148. Sort List](https://leetcode.cn/problems/sort-list/) (Medium)

## 23. Merge k Sorted Lists

-   [LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/) | [LeetCode CH](https://leetcode.cn/problems/merge-k-sorted-lists/) (Hard)

-   Tags: linked list, divide and conquer, heap priority queue, merge sort
-   Prerequisite: 21. Merge Two Sorted Lists
-   Video explanation: [23. Merge K Sorted Lists - NeetCode](https://youtu.be/q5a5OiGbT6Q?si=SQ2dCvsYQ3LQctPh)

```python title="23. Merge k Sorted Lists - Python Solution"
import copy
import heapq
from typing import List, Optional

from template import ListNode


# Divide and Conquer
def mergeKListsDC(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
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


# Heap - Merge k Sorted
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy

    minHeap = []  # (val, idx, node)

    for idx, head in enumerate(lists):
        if head:
            heapq.heappush(minHeap, (head.val, idx, head))

    while minHeap:
        _, idx, node = heapq.heappop(minHeap)
        cur.next = node
        cur = cur.next

        node = node.next
        if node:
            heapq.heappush(minHeap, (node.val, idx, node))

    return dummy.next


n1 = ListNode.create([1, 4, 5])
n2 = ListNode.create([1, 3, 4])
n3 = ListNode.create([2, 6])
lists = [n1, n2, n3]
lists1 = copy.deepcopy(lists)
lists2 = copy.deepcopy(lists)
print(mergeKListsDC(lists1))
# 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
print(mergeKLists(lists2))
# 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

```

## 148. Sort List

-   [LeetCode](https://leetcode.com/problems/sort-list/) | [LeetCode CH](https://leetcode.cn/problems/sort-list/) (Medium)

-   Tags: linked list, two pointers, divide and conquer, sorting, merge sort

```python title="148. Sort List - Python Solution"
from typing import Optional

from template import ListNode


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


head = ListNode().create([4, 2, 1, 3])
print(head)  # 4 -> 2 -> 1 -> 3
print(sortListSort(head))  # 1 -> 2 -> 3 -> 4
print(sortListDivideConquer(head))  # 1 -> 2 -> 3 -> 4

```
