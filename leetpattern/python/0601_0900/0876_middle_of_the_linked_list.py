from typing import Optional

from leetpattern.utils import LinkedList, ListNode


# Linked List
def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    fast, slow = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow


def test_middleNode():
    # Test case 1: Odd number of nodes
    ll1 = LinkedList([1, 2, 3, 4, 5])
    middle1 = middleNode(ll1.head)
    result1 = LinkedList(middle1)
    assert result1.to_array() == [3, 4, 5]

    # Test case 2: Even number of nodes
    ll2 = LinkedList([1, 2, 3, 4, 5, 6])
    middle2 = middleNode(ll2.head)
    result2 = LinkedList(middle2)
    assert result2.to_array() == [4, 5, 6]

    # Test case 3: Single node
    ll3 = LinkedList([1])
    middle3 = middleNode(ll3.head)
    result3 = LinkedList(middle3)
    assert result3.to_array() == [1]

    # Test case 4: Two nodes
    ll4 = LinkedList([1, 2])
    middle4 = middleNode(ll4.head)
    result4 = LinkedList(middle4)
    assert result4.to_array() == [2]
