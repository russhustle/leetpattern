from typing import Optional

from helper import ListNode


# Hash Set
def getIntersectionNodeHash(
    headA: ListNode, headB: ListNode
) -> Optional[ListNode]:
    """Return the intersection node of two linked lists."""
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
    """Return the intersection node of two linked lists."""
    if not headA or not headB:
        return None

    a, b = headA, headB

    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA

    return a


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# |  Hash Set  | O(n+m) |  O(n)   |
# |Two Pointers| O(n+m) |  O(1)   |
# |------------|--------|---------|


listA = [4, 1, 8, 4, 5]
listB = [5, 6, 1, 8, 4, 5]
headA = ListNode.create(listA)
print(headA)
# 4 -> 1 -> 8 -> 4 -> 5
headB = ListNode.create(listB)
print(headB)
# 5 -> 6 -> 1 -> 8 -> 4 -> 5

headA.intersect(headB, 8)

print(getIntersectionNodeHash(headA, headB))
# 8 -> 4 -> 5
print(getIntersectionNodeTP(headA, headB))
# 8 -> 4 -> 5
