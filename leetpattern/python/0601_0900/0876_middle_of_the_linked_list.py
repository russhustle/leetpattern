from typing import Optional

from leetpattern.utils import ListNode


# Linked List
def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    fast, slow = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow


print(middleNode(list_from_array([1, 2, 3, 4, 5])))
# 3 -> 4 -> 5
print(middleNode(list_from_array([1, 2, 3, 4, 5, 6])))
# 4 -> 5 -> 6
