from typing import Optional

from helper import ListNode


# Linked List
def reorderList(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    if not head or not head.next:
        return

    # Middle of the linked list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half
    pre, cur = None, slow
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp

    # Merge two linked lists
    first, second = head, pre
    while second.next:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2


head = ListNode.create([1, 2, 3, 4, 5, 6])
print(head)  # 1 -> 2 -> 3 -> 4 -> 5 -> 6
reorderList(head)
print(head)  # 1 -> 6 -> 2 -> 5 -> 3 -> 4
