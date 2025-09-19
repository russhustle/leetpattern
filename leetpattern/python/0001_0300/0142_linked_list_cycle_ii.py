from typing import Optional

from leetpattern.utils import LinkedList, ListNode


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


def test_detectCycle():
    l1 = LinkedList([3, 2, 0, -4])
    l1.make_cycle(1)
    assert detectCycle(l1.head).val == 2
    l2 = LinkedList([3, 2, 0, -4])
    assert not detectCycle(l2.head)
