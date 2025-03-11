from typing import Optional

from template import ListNode


# Linked List
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


node = ListNode.create([1, 2, 3, 4, 5])
print(deleteMiddle(node))
# 1 -> 2 -> 4 -> 5
