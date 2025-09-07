from typing import Optional

from leetpattern.utils import ListNode


# Linked List
def mergeNodes(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy

    head = head.next
    temp = 0

    while head.next:
        if head.val == 0:
            cur.next = ListNode(temp)
            cur = cur.next
            temp = 0
        else:
            temp += head.val

        head = head.next

    if temp != 0:
        cur.next = ListNode(temp)

    return dummy.next


root = list_from_array([0, 3, 1, 0, 4, 5, 2, 0])
print(root)  # 0 -> 3 -> 1 -> 0 -> 4 -> 5 -> 2 -> 0
print(mergeNodes(root))  # 4 -> 11
