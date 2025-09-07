from leetpattern.utils import (ListNode, LinkedList, get_length, has_cycle,
                               list_from_array, list_to_array, make_cycle,
                               reverse_list)


# Tests for ListNode
def test_listnode_creation():
    node = ListNode(5)
    assert node.val == 5
    assert node.next is None


def test_listnode_with_next():
    node2 = ListNode(10)
    node1 = ListNode(5, node2)
    assert node1.val == 5
    assert node1.next == node2
    assert node1.next.val == 10


# Tests for list_from_array
def test_list_from_array_empty():
    result = list_from_array([])
    assert result is None


def test_list_from_array_single():
    result = list_from_array([5])
    assert result is not None
    assert result.val == 5
    assert result.next is None


def test_list_from_array_multiple():
    result = list_from_array([1, 2, 3, 4])
    assert result is not None
    assert result.val == 1
    assert result.next.val == 2
    assert result.next.next.val == 3
    assert result.next.next.next.val == 4
    assert result.next.next.next.next is None


def test_list_from_array_negative_values():
    result = list_from_array([-1, 0, 1])
    assert result is not None
    assert result.val == -1
    assert result.next.val == 0
    assert result.next.next.val == 1


# Tests for list_to_array
def test_list_to_array_none():
    result = list_to_array(None)
    assert result == []


def test_list_to_array_single():
    node = ListNode(5)
    result = list_to_array(node)
    assert result == [5]


def test_list_to_array_multiple():
    head = list_from_array([1, 2, 3, 4])
    result = list_to_array(head)
    assert result == [1, 2, 3, 4]


def test_list_to_array_negative_values():
    head = list_from_array([-5, -1, 0, 1, 5])
    result = list_to_array(head)
    assert result == [-5, -1, 0, 1, 5]


# Tests for get_length
def test_get_length_none():
    result = get_length(None)
    assert result == 0


def test_get_length_single():
    node = ListNode(5)
    result = get_length(node)
    assert result == 1


def test_get_length_multiple():
    head = list_from_array([1, 2, 3, 4, 5])
    result = get_length(head)
    assert result == 5


def test_get_length_long_list():
    head = list_from_array(list(range(100)))
    result = get_length(head)
    assert result == 100


# Tests for make_cycle
def test_make_cycle_none():
    result = make_cycle(None, 0)
    assert result is None


def test_make_cycle_negative_pos():
    head = list_from_array([1, 2, 3])
    result = make_cycle(head, -1)
    assert result == head
    assert not has_cycle(result)


def test_make_cycle_valid_pos():
    head = list_from_array([1, 2, 3, 4])
    result = make_cycle(head, 1)
    assert result == head
    assert has_cycle(result)


def test_make_cycle_pos_zero():
    head = list_from_array([1, 2, 3])
    result = make_cycle(head, 0)
    assert result == head
    assert has_cycle(result)


def test_make_cycle_pos_out_of_bounds():
    head = list_from_array([1, 2, 3])
    result = make_cycle(head, 5)
    assert result == head
    assert not has_cycle(result)


# Tests for has_cycle
def test_has_cycle_none():
    result = has_cycle(None)
    assert result is False


def test_has_cycle_single_no_cycle():
    node = ListNode(1)
    result = has_cycle(node)
    assert result is False


def test_has_cycle_single_with_self_cycle():
    node = ListNode(1)
    node.next = node
    result = has_cycle(node)
    assert result is True


def test_has_cycle_no_cycle():
    head = list_from_array([1, 2, 3, 4, 5])
    result = has_cycle(head)
    assert result is False


def test_has_cycle_with_cycle():
    head = list_from_array([1, 2, 3, 4])
    make_cycle(head, 1)
    result = has_cycle(head)
    assert result is True


def test_has_cycle_cycle_at_head():
    head = list_from_array([1, 2, 3])
    make_cycle(head, 0)
    result = has_cycle(head)
    assert result is True


def test_has_cycle_two_nodes():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    result = has_cycle(node1)
    assert result is False

    node2.next = node1
    result = has_cycle(node1)
    assert result is True


# Tests for reverse_list
def test_reverse_list_none():
    result = reverse_list(None)
    assert result is None


def test_reverse_list_single():
    node = ListNode(5)
    result = reverse_list(node)
    assert result.val == 5
    assert result.next is None


def test_reverse_list_two_nodes():
    head = list_from_array([1, 2])
    result = reverse_list(head)
    assert list_to_array(result) == [2, 1]


def test_reverse_list_multiple():
    head = list_from_array([1, 2, 3, 4, 5])
    result = reverse_list(head)
    assert list_to_array(result) == [5, 4, 3, 2, 1]


def test_reverse_list_with_duplicates():
    head = list_from_array([1, 2, 2, 3])
    result = reverse_list(head)
    assert list_to_array(result) == [3, 2, 2, 1]


def test_reverse_list_all_same():
    head = list_from_array([5, 5, 5, 5])
    result = reverse_list(head)
    assert list_to_array(result) == [5, 5, 5, 5]


# Integration tests
def test_round_trip_conversion():
    original = [1, 2, 3, 4, 5]
    head = list_from_array(original)
    result = list_to_array(head)
    assert result == original


def test_reverse_twice():
    original = [1, 2, 3, 4, 5]
    head = list_from_array(original)
    reversed_once = reverse_list(head)
    reversed_twice = reverse_list(reversed_once)
    result = list_to_array(reversed_twice)
    assert result == original


def test_length_after_operations():
    head = list_from_array([1, 2, 3, 4])
    original_length = get_length(head)

    reversed_head = reverse_list(head)
    reversed_length = get_length(reversed_head)

    assert original_length == reversed_length == 4


def test_cycle_detection_comprehensive():
    # Test various cycle scenarios
    scenarios = [
        ([1], 0),
        ([1, 2], 0),
        ([1, 2], 1),
        ([1, 2, 3, 4], 2),
        ([1, 2, 3, 4, 5], 0),
    ]

    for arr, pos in scenarios:
        head = list_from_array(arr)
        assert not has_cycle(head)

        make_cycle(head, pos)
        assert has_cycle(head)


# Tests for LinkedList class
def test_linkedlist_creation_empty():
    ll = LinkedList()
    assert ll.head is None
    assert len(ll) == 0
    assert not ll
    assert str(ll) == "Empty"


def test_linkedlist_creation_from_list():
    ll = LinkedList([1, 2, 3, 4])
    assert ll.to_array() == [1, 2, 3, 4]
    assert len(ll) == 4
    assert bool(ll)
    assert str(ll) == "1 -> 2 -> 3 -> 4"


def test_linkedlist_creation_from_node():
    node = ListNode(5)
    ll = LinkedList(node)
    assert ll.head == node
    assert ll.to_array() == [5]


def test_linkedlist_append():
    ll = LinkedList()
    ll.append(1)
    assert ll.to_array() == [1]

    ll.append(2)
    ll.append(3)
    assert ll.to_array() == [1, 2, 3]


def test_linkedlist_prepend():
    ll = LinkedList([2, 3])
    ll.prepend(1)
    assert ll.to_array() == [1, 2, 3]


def test_linkedlist_insert():
    ll = LinkedList([1, 3, 4])
    ll.insert(1, 2)
    assert ll.to_array() == [1, 2, 3, 4]

    ll.insert(0, 0)
    assert ll.to_array() == [0, 1, 2, 3, 4]

    try:
        ll.insert(-1, 5)
        assert False, "Should raise ValueError"
    except ValueError:
        pass

    try:
        ll.insert(10, 5)
        assert False, "Should raise IndexError"
    except IndexError:
        pass


def test_linkedlist_delete():
    ll = LinkedList([1, 2, 3, 2, 4])
    assert ll.delete(2) is True
    assert ll.to_array() == [1, 3, 2, 4]

    assert ll.delete(1) is True
    assert ll.to_array() == [3, 2, 4]

    assert ll.delete(5) is False
    assert ll.to_array() == [3, 2, 4]


def test_linkedlist_delete_at():
    ll = LinkedList([1, 2, 3, 4])
    assert ll.delete_at(1) == 2
    assert ll.to_array() == [1, 3, 4]

    assert ll.delete_at(0) == 1
    assert ll.to_array() == [3, 4]

    try:
        ll.delete_at(5)
        assert False, "Should raise IndexError"
    except IndexError:
        pass


def test_linkedlist_find():
    ll = LinkedList([1, 2, 3, 2, 4])
    assert ll.find(2) == 1
    assert ll.find(4) == 4
    assert ll.find(5) == -1


def test_linkedlist_get():
    ll = LinkedList([1, 2, 3, 4])
    assert ll.get(0) == 1
    assert ll.get(2) == 3

    try:
        ll.get(-1)
        assert False, "Should raise IndexError"
    except IndexError:
        pass

    try:
        ll.get(10)
        assert False, "Should raise IndexError"
    except IndexError:
        pass


def test_linkedlist_clear():
    ll = LinkedList([1, 2, 3])
    assert len(ll) == 3

    ll.clear()
    assert len(ll) == 0
    assert not ll
    assert ll.head is None


def test_linkedlist_copy():
    ll1 = LinkedList([1, 2, 3])
    ll2 = ll1.copy()

    assert ll1 == ll2
    assert ll1.head is not ll2.head

    ll2.append(4)
    assert ll1.to_array() == [1, 2, 3]
    assert ll2.to_array() == [1, 2, 3, 4]


def test_linkedlist_equality():
    ll1 = LinkedList([1, 2, 3])
    ll2 = LinkedList([1, 2, 3])
    ll3 = LinkedList([1, 2, 4])

    assert ll1 == ll2
    assert ll1 != ll3
    assert ll1 != "not a linkedlist"


def test_linkedlist_reverse():
    ll = LinkedList([1, 2, 3, 4])
    ll.reverse()
    assert ll.to_array() == [4, 3, 2, 1]


def test_linkedlist_has_cycle():
    ll = LinkedList([1, 2, 3, 4])
    assert not ll.has_cycle()

    ll.make_cycle(1)
    assert ll.has_cycle()


def test_linkedlist_get_middle():
    ll = LinkedList()
    assert ll.get_middle() is None

    ll = LinkedList([1])
    assert ll.get_middle() == 1

    ll = LinkedList([1, 2, 3])
    assert ll.get_middle() == 2

    ll = LinkedList([1, 2, 3, 4])
    assert ll.get_middle() == 2

    ll = LinkedList([1, 2, 3, 4, 5])
    assert ll.get_middle() == 3


def test_linkedlist_remove_duplicates():
    ll = LinkedList([1, 1, 2, 3, 3, 4])
    ll.remove_duplicates()
    assert ll.to_array() == [1, 2, 3, 4]

    ll = LinkedList([1, 1, 1, 1])
    ll.remove_duplicates()
    assert ll.to_array() == [1]

    ll = LinkedList()
    ll.remove_duplicates()
    assert ll.to_array() == []


def test_linkedlist_edge_cases():
    ll = LinkedList([])
    assert len(ll) == 0
    assert not ll

    ll.append(1)
    assert len(ll) == 1
    assert bool(ll)

    assert ll.delete(1) is True
    assert len(ll) == 0
    assert not ll
