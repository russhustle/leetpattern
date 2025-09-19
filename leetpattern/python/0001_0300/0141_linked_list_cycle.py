from typing import Optional

from leetpattern.utils import LinkedList, ListNode


def has_cycle(head: Optional[ListNode]) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def test_has_cycle():
    ll = LinkedList([3, 2, 0, -4])
    ll.make_cycle(pos=1)
    assert has_cycle(ll.head)

    ll = LinkedList([1, 2])
    ll.make_cycle(pos=0)
    assert has_cycle(ll.head)

    ll = LinkedList([1, 2, 3, 4, 5])
    assert not has_cycle(ll.head)
