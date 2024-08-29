from typing import Optional

from helper import ListNode


# Iterative
def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy = ListNode(next=head)
    cur = dummy

    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next

    return dummy.next


# |-------------|-----------------|--------------|
# |  Approach   |      Time       |    Space     |
# |-------------|-----------------|--------------|
# |  Iterative  |      O(N)       |    O(1)      |
# |-------------|-----------------|--------------|


nums = [1, 2, 6, 3, 4, 5, 6]
val = 6
head = ListNode.create(nums)
print(head)
# 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
print(removeElements(head, val))
# 1 -> 2 -> 3 -> 4 -> 5
