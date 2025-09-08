from typing import Optional

from leetpattern.utils import LinkedList, ListNode


def merge_nodes(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

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


def test_merge_nodes():
    root = LinkedList([0, 3, 1, 0, 4, 5, 2, 0])
    res = merge_nodes(root.head)
    assert LinkedList(res).to_array() == [4, 11]
