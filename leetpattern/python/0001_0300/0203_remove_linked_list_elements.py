"""
-   Remove all elements from a linked list of integers that have value `val`.
"""

from typing import Optional

from leetpattern.utils import LinkedList, ListNode


# Iterative
def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head
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


def test_removeElements():
    # Test case 1: Remove elements from middle and end
    nums = [1, 2, 6, 3, 4, 5, 6]
    val = 6
    ll = LinkedList(nums)
    assert ll.to_array() == [1, 2, 6, 3, 4, 5, 6]
    result = removeElements(ll.head, val)
    ll_result = LinkedList(result)
    assert ll_result.to_array() == [1, 2, 3, 4, 5]

    # Test case 2: Remove all elements
    ll2 = LinkedList([7, 7, 7, 7])
    result2 = removeElements(ll2.head, 7)
    assert result2 is None

    # Test case 3: Remove elements from beginning
    ll3 = LinkedList([1, 1, 2, 3, 4])
    result3 = removeElements(ll3.head, 1)
    ll_result3 = LinkedList(result3)
    assert ll_result3.to_array() == [2, 3, 4]

    # Test case 4: No elements to remove
    ll4 = LinkedList([1, 2, 3, 4])
    result4 = removeElements(ll4.head, 5)
    ll_result4 = LinkedList(result4)
    assert ll_result4.to_array() == [1, 2, 3, 4]
