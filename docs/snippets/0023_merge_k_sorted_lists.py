import heapq
from typing import List, Optional

from helper import ListNode


# Heap - Merge k Sorted
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy

    heap = []

    for idx, head in enumerate(lists):
        if head:
            heapq.heappush(heap, (head.val, idx, head))

    while heap:
        _, idx, node = heapq.heappop(heap)
        cur.next = node
        cur = cur.next

        node = node.next
        if node:
            heapq.heappush(heap, (node.val, idx, node))

    return dummy.next


n1 = ListNode.create([1, 4, 5])
n2 = ListNode.create([1, 3, 4])
n3 = ListNode.create([2, 6])
lists = [n1, n2, n3]
print(mergeKLists(lists))
# 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
