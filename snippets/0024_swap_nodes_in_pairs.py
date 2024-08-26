from typing import Optional

from helper import ListNode


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(next=head)
    cur = dummy

    while cur.next and cur.next.next:
        temp = cur.next
        temp1 = cur.next.next.next

        cur.next = cur.next.next
        cur.next.next = temp
        temp.next = temp1
        cur = cur.next.next

    return dummy.next


nums = [1, 2, 3, 4, 5]
head = ListNode.create(nums)
print(head)
# 1 -> 2 -> 3 -> 4 -> 5
print(swapPairs(head))
# 2 -> 1 -> 4 -> 3 -> 5
