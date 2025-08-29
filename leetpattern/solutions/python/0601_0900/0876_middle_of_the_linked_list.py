from typing import Optional

from template import ListNode


# Linked List
def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    fast, slow = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow


print(middleNode(ListNode.create([1, 2, 3, 4, 5])))
# 3 -> 4 -> 5
print(middleNode(ListNode.create([1, 2, 3, 4, 5, 6])))
# 4 -> 5 -> 6
