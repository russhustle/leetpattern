from typing import Optional

from leetpattern.utils import ListNode, list_from_array, list_to_array


# Linked List
def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    n = 0
    cur = head
    while cur:
        n += 1
        cur = cur.next

    p0 = dummy = ListNode(next=head)
    pre = None
    cur = head

    while n >= k:
        n -= k
        for _ in range(k):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        nxt = p0.next
        nxt.next = cur
        p0.next = pre
        p0 = nxt

    return dummy.next


def test_reverse_k_group():
    head = list_from_array([1, 2, 3, 4, 5])
    assert list_to_array(reverse_k_group(head, 2)) == [2, 1, 4, 3, 5]
