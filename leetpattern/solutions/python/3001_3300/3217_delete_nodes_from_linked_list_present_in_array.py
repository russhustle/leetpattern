from typing import List, Optional

from leetpattern.utils import ListNode, list_from_array, list_to_array


def modified_list(
    nums: List[int], head: Optional[ListNode]
) -> Optional[ListNode]:
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
    nums = [1, 2, 3]
    head = list_from_array([1, 2, 3, 4, 5])
    assert list_to_array(modified_list(nums, head)) == [4, 5]
