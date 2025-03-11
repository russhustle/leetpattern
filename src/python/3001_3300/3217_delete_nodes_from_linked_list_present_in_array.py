from typing import List, Optional

from template import ListNode


# Linked List
def modifiedList(
    nums: List[int], head: Optional[ListNode]
) -> Optional[ListNode]:
    numSet = set(nums)
    dummy = ListNode(0, head)
    cur = dummy

    while cur.next:
        if cur.next.val in numSet:
            cur.next = cur.next.next
        else:
            cur = cur.next

    return dummy.next


nums = [1, 2, 3]
head = ListNode().create([1, 2, 3, 4, 5])
print(modifiedList(nums, head))  # 4 -> 5
