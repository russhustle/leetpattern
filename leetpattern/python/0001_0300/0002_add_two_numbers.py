from typing import Optional

from leetpattern.utils import LinkedList, ListNode


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """Digit Carry Simulation: O(max(m, n)) time, O(max(m, n)) space.
        Walk both reversed lists while carrying overflow into the next digit.
        """
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            carry, val = divmod(v1 + v2 + carry, 10)
            cur.next = ListNode(val)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


def test_add_two_numbers():
    s = Solution()

    l1 = LinkedList([2, 4, 3]).head
    l2 = LinkedList([5, 6, 4]).head
    assert LinkedList(s.addTwoNumbers(l1, l2)).to_array() == [7, 0, 8]

    l1 = LinkedList([0]).head
    l2 = LinkedList([0]).head
    assert LinkedList(s.addTwoNumbers(l1, l2)).to_array() == [0]

    l1 = LinkedList([9, 9, 9, 9, 9, 9, 9]).head
    l2 = LinkedList([9, 9, 9, 9]).head
    assert LinkedList(s.addTwoNumbers(l1, l2)).to_array() == [
        8,
        9,
        9,
        9,
        0,
        0,
        0,
        1,
    ]
