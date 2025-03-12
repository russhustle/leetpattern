from typing import Optional

from template import ListNode


# Linked List
def reverseBetween(
    head: Optional[ListNode], left: int, right: int
) -> Optional[ListNode]:
    dummy = ListNode(next=head)
    p0 = dummy
    for _ in range(left - 1):
        p0 = p0.next

    pre = None
    cur = p0.next
    for _ in range(right - left + 1):
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt

    p0.next.next = cur
    p0.next = pre

    return dummy.next


head = ListNode().create([1, 2, 3, 4, 5])
left = 2
right = 4
print(reverseBetween(head, left, right))
# 1 -> 4 -> 3 -> 2 -> 5
