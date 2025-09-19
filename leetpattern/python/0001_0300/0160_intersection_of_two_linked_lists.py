"""
-   Find the node at which the intersection of two singly linked lists begins.
"""

from typing import Optional

from leetpattern.utils import LinkedList, ListNode


# Hash Set
def getIntersectionNodeHash(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
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
def getIntersectionNodeTP(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    if not headA or not headB:
        return None

    a, b = headA, headB

    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA

    return a


def test_intersection():
    # Test case 1: Lists with intersection
    llA = LinkedList([4, 1, 8, 4, 5])
    llB = LinkedList([5, 6, 1])

    # Create intersection at node with value 8
    nodeA = llA.head
    while nodeA and nodeA.val != 8:
        nodeA = nodeA.next

    # Connect listB to the intersection point
    llB.head.next.next.next = nodeA

    assert llA.to_array() == [4, 1, 8, 4, 5]

    intersection_hash = getIntersectionNodeHash(llA.head, llB.head)
    intersection_tp = getIntersectionNodeTP(llA.head, llB.head)

    assert intersection_hash is not None
    assert intersection_tp is not None
    assert intersection_hash.val == 8
    assert intersection_tp.val == 8
    assert intersection_hash == intersection_tp

    # Test case 2: Lists without intersection
    llC = LinkedList([2, 6, 4])
    llD = LinkedList([1, 5])

    intersection_hash = getIntersectionNodeHash(llC.head, llD.head)
    intersection_tp = getIntersectionNodeTP(llC.head, llD.head)

    assert intersection_hash is None
    assert intersection_tp is None
