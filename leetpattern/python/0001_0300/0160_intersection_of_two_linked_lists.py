"""
-   Find the node at which the intersection of two singly linked lists begins.
"""

from typing import Optional

from leetpattern.utils import ListNode


# Hash Set
def getIntersectionNodeHash(
    headA: ListNode, headB: ListNode
) -> Optional[ListNode]:
    if not headA or not headB:
        return None

    visited = set()
    cur = headA
    while cur:
        visited.add(cur)
        cur = cur.next

    cur = headB
    while cur:
        if cur in visited:
            return cur
        cur = cur.next

    return None


# Two Pointers
def getIntersectionNodeTP(
    headA: ListNode, headB: ListNode
) -> Optional[ListNode]:
    if not headA or not headB:
        return None

    a, b = headA, headB

    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA

    return a


listA = [4, 1, 8, 4, 5]
listB = [5, 6, 1, 8, 4, 5]
headA = list_from_array(listA)
print(headA)
# 4 -> 1 -> 8 -> 4 -> 5
headB = list_from_array(listB)
print(headB)
# 5 -> 6 -> 1 -> 8 -> 4 -> 5

headA.intersect(headB, 8)

print(getIntersectionNodeHash(headA, headB))
# 8 -> 4 -> 5
print(getIntersectionNodeTP(headA, headB))
# 8 -> 4 -> 5
