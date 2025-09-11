"""
-   Prerequisite: 21. Merge Two Sorted Lists
-   Video explanation: [23. Merge K Sorted Lists - NeetCode](https://youtu.be/q5a5OiGbT6Q?si=SQ2dCvsYQ3LQctPh)
"""

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
