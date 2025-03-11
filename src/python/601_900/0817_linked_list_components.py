from typing import List, Optional

from template import ListNode


# Linked List
def numComponents(head: Optional[ListNode], nums: List[int]) -> int:
    numSet = set(nums)
    res = 0

    while head:
        if head.val in numSet:
            while head and head.val in numSet:
                head = head.next
            res += 1
        else:
            head = head.next

    return res


head = ListNode().create([0, 1, 2, 3, 4])
nums = [0, 3, 1, 4]
print(numComponents(head, nums))  # 2
