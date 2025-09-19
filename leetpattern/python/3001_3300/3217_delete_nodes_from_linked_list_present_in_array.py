from typing import List, Optional

from leetpattern.utils import LinkedList, ListNode


def modified_list(nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
    num_set = set(nums)
    dummy = ListNode(0, head)
    cur = dummy

    while cur.next:
        if cur.next.val in num_set:
            cur.next = cur.next.next
        else:
            cur = cur.next

    return dummy.next


def test_modified_list():
    ll = LinkedList([1, 2, 3, 4, 5])
    ll = LinkedList(modified_list([2, 3], ll.head))
    assert ll.to_array() == [1, 4, 5]
