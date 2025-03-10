from typing import Optional

from template import ListNode


# Linked List
def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    nums = []

    while head:
        nums.append(head.val)
        head = head.next

    dummy = ListNode()
    cur = dummy
    nums.sort()

    for num in nums:
        cur.next = ListNode(val=num)
        cur = cur.next

    return dummy.next
