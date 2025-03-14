from typing import Optional

from template import ListNode


# Linked List
def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    fast, slow = dummy, dummy

    for _ in range(n):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next


head = [1, 2, 3, 4, 5]
n = 2
head = ListNode.create(head)
print(head)  # 1 -> 2 -> 3 -> 4 -> 5
print(removeNthFromEnd(head, n))  # 1 -> 2 -> 3 -> 5
