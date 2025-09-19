from typing import Optional

from leetpattern.utils import LinkedList, ListNode


def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
    fast, slow = head, head
    dummy = ListNode(0, head)
    cur = dummy

    while fast and fast.next:
        fast = fast.next.next
        cur = cur.next
        slow = slow.next

    cur.next = slow.next

    return dummy.next


def test_deleteMiddle():
    ll = LinkedList([1, 3, 4, 7, 1, 2, 6])
    ll = LinkedList(deleteMiddle(ll.head))
    assert ll.to_array() == [1, 3, 4, 1, 2, 6]

    ll = LinkedList([1, 2, 3, 4])
    ll = LinkedList(deleteMiddle(ll.head))
    assert ll.to_array() == [1, 2, 4]
