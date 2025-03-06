from typing import Optional

from template import ListNode


# Linked List
def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    cur = head
    while cur.next:
        if cur.next.val == cur.val:
            cur.next = cur.next.next
        else:
            cur = cur.next

    return head


head = ListNode().create([1, 1, 2, 3, 3])
print(deleteDuplicates(head))  # 1 -> 2 -> 3
