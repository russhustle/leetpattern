from typing import Optional

from leetpattern.utils import LinkedList, ListNode


def doubleIt(head: Optional[ListNode]) -> Optional[ListNode]:

    def twice(node):
        if not node:
            return 0
        doubled = node.val * 2 + twice(node.next)
        node.val = doubled % 10
        return doubled // 10

    carry = twice(head)

    if carry:
        head = ListNode(val=carry, next=head)

    return head


def test_doubleIt() -> None:
    ll = LinkedList([9, 9, 9])
    ll = LinkedList(doubleIt(ll.head))
    assert ll.to_array() == [1, 9, 9, 8]
