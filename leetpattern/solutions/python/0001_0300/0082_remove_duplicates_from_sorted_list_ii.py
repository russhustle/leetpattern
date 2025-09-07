from typing import Optional

from leetpattern.utils import ListNode


# Linked List
def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    cur = dummy

    while cur.next and cur.next.next:
        val = cur.next.val
        if cur.next.next.val == val:
            while cur.next and cur.next.val == val:
                cur.next = cur.next.next
        else:
            cur = cur.next

    return dummy.next


head = ListNode().create([1, 1, 2, 3, 3, 4, 5])
print(deleteDuplicates(head))  # 2 -> 4 -> 5
