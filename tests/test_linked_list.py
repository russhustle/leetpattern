from leetpattern.utils import LinkedList, ListNode


# ListNode tests
def test_listnode():
    node = ListNode(5)
    assert node.val == 5
    assert node.next is None
    assert repr(node) == "ListNode(5)"

    node2 = ListNode(10)
    node1 = ListNode(5, node2)
    assert node1.val == 5
    assert node1.next == node2


# LinkedList creation tests
def test_creation():
    ll = LinkedList()
    assert ll.head is None
    assert len(ll) == 0
    assert not ll
    assert str(ll) == "Empty"

    ll = LinkedList([1, 2, 3])
    assert ll.to_array() == [1, 2, 3]
    assert len(ll) == 3
    assert bool(ll)
    assert str(ll) == "1 -> 2 -> 3"

    node = ListNode(5)
    ll = LinkedList(node)
    assert ll.head == node
    assert ll.to_array() == [5]


# LinkedList basic operations
def test_append_prepend():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    assert ll.to_array() == [1, 2]

    ll.prepend(0)
    assert ll.to_array() == [0, 1, 2]


def test_insert_delete():
    ll = LinkedList([1, 3, 4])
    ll.insert(1, 2)
    assert ll.to_array() == [1, 2, 3, 4]

    assert ll.delete(2) is True
    assert ll.to_array() == [1, 3, 4]
    assert ll.delete(5) is False

    assert ll.delete_at(1) == 3
    assert ll.to_array() == [1, 4]


def test_find_get():
    ll = LinkedList([1, 2, 3, 2, 4])
    assert ll.find(2) == 1
    assert ll.find(5) == -1
    assert ll.get(0) == 1
    assert ll.get(2) == 3


def test_utility_methods():
    ll = LinkedList([1, 2, 3])
    ll2 = ll.copy()
    assert ll == ll2
    assert ll.head is not ll2.head

    ll.reverse()
    assert ll.to_array() == [3, 2, 1]

    ll.clear()
    assert len(ll) == 0
    assert not ll


# LinkedList advanced features
def test_cycle_detection():
    ll = LinkedList([1, 2, 3, 4])
    assert not ll.has_cycle()

    ll.make_cycle(1)
    assert ll.has_cycle()


def test_get_middle():
    assert LinkedList().get_middle() is None
    assert LinkedList([1]).get_middle() == 1
    assert LinkedList([1, 2, 3]).get_middle() == 2
    assert LinkedList([1, 2, 3, 4]).get_middle() == 2


def test_remove_duplicates():
    ll = LinkedList([1, 1, 2, 3, 3, 4])
    ll.remove_duplicates()
    assert ll.to_array() == [1, 2, 3, 4]

    ll = LinkedList([1, 1, 1])
    ll.remove_duplicates()
    assert ll.to_array() == [1]


# Error handling
def test_errors():
    ll = LinkedList([1, 2, 3])

    try:
        ll.insert(-1, 5)
        assert False
    except ValueError:
        pass

    try:
        ll.get(10)
        assert False
    except IndexError:
        pass

    try:
        LinkedList("invalid")
        assert False
    except ValueError:
        pass
