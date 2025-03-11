from typing import Optional

from template import ListNode


def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    slow, fast = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow

    return None


head1 = ListNode.create([3, 2, 0, -4], 1)
print(detectCycle(head1).val)  # 2
head2 = ListNode.create([3, 2, 0, -4])
print(detectCycle(head2))  # None
