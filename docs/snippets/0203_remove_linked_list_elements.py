from typing import Optional

from helper import ListNode


def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy = ListNode(next=head)
    cur = dummy

    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next

    return dummy.next


nums = [1, 2, 6, 3, 4, 5, 6]
val = 6
head = ListNode.create(nums)
print(head)
# 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
print(removeElements(head, val))
# 1 -> 2 -> 3 -> 4 -> 5
