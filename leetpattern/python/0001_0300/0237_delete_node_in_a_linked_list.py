"""
-   Delete a node in a singly linked list. You are given only the node to be deleted.
"""

from leetpattern.utils import LinkedList, ListNode


def deleteNode(node: ListNode) -> None:
    node.val = node.next.val
    node.next = node.next.next


def test_deleteNode():
    # Test case 1: Delete middle node
    ll = LinkedList([4, 5, 1, 9])
    assert ll.to_array() == [4, 5, 1, 9]
    node = ll.head.next  # node with value 5
    deleteNode(node)
    assert ll.to_array() == [4, 1, 9]

    # Test case 2: Delete another middle node
    ll2 = LinkedList([4, 5, 1, 9])
    node2 = ll2.head.next.next  # node with value 1
    deleteNode(node2)
    assert ll2.to_array() == [4, 5, 9]
