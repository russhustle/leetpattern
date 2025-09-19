from typing import Optional

from leetpattern.utils import LinkedList, ListNode


def reverse_list_iterative(head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head
    prev = None

    while cur:
        temp = cur.next
        cur.next = prev

        prev = cur
        cur = temp

    return prev


def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    def reverse(cur, prev):
        if not cur:
            return prev

        temp = cur.next
        cur.next = prev
        return reverse(temp, cur)

    return reverse(head, None)


def test_reverse_list():
    ll = LinkedList([1, 2, 3, 4, 5])
    ll.head = reverse_list_iterative(ll.head)
    assert ll.to_array() == [5, 4, 3, 2, 1]

    ll = LinkedList([1, 2, 3, 4, 5])
    ll.head = reverse_list_recursive(ll.head)
    assert ll.to_array() == [5, 4, 3, 2, 1]
