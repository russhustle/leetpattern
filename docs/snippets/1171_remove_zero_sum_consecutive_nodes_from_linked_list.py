from typing import Optional

from helper import ListNode


# Prefix Sum
def removeZeroSumSublists(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head
    cur = head
    prefix_sum = 0
    seen = {0: dummy}

    while cur:
        prefix_sum += cur.val
        if prefix_sum in seen:
            node = seen[prefix_sum].next
            temp_sum = prefix_sum
            while node != cur:
                temp_sum += node.val
                del seen[temp_sum]
                node = node.next
            seen[prefix_sum].next = cur.next
        else:
            seen[prefix_sum] = cur
        cur = cur.next

    return dummy.next


head = ListNode().create([1, 2, -3, 3, 1])
print(removeZeroSumSublists(head))  # 3 -> 1
