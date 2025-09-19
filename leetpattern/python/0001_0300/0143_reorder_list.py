from typing import Optional

from leetpattern.utils import LinkedList, ListNode


# Linked List
def reorderList(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    if not head or not head.next:
        return

    # Middle of the linked list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half
    pre, cur = None, slow
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp

    # Merge two linked lists
    first, second = head, pre
    while second.next:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2


def test_reorderList():
    ll = LinkedList([1, 2, 3, 4, 5, 6])
    assert ll.to_array() == [1, 2, 3, 4, 5, 6]
    reorderList(ll.head)
    assert ll.to_array() == [1, 6, 2, 5, 3, 4]

    ll2 = LinkedList([1, 2, 3, 4, 5])
    assert ll2.to_array() == [1, 2, 3, 4, 5]
    reorderList(ll2.head)
    assert ll2.to_array() == [1, 5, 2, 4, 3]
