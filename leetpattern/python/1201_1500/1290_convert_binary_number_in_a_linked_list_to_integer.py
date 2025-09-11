from typing import Optional

from leetpattern.utils import ListNode


# Linked List
def getDecimalValue(head: Optional[ListNode]) -> int:
    res = 0

    while head:
        res = res * 2 + head.val
        head = head.next

    return res


node = ListNode().create([1, 0, 1])
print(node)  # 1 -> 0 -> 1
print(getDecimalValue(node))  # 5
