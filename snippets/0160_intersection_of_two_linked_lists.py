from typing import Optional

from helper import ListNode


def getIntersectionNode(
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
headA = ListNode.create(listA)
print(headA)
# 4 -> 1 -> 8 -> 4 -> 5
headB = ListNode.create(listB)
print(headB)
# 5 -> 6 -> 1 -> 8 -> 4 -> 5
print(getIntersectionNode(headA, headB))
# 8 -> 4 -> 5
