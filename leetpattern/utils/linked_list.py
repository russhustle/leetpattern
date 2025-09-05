class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_from_array(nums: list[int]) -> ListNode | None:
    if not nums:
        return None

    head = ListNode(nums[0])
    cur = head
    for num in nums[1:]:
        cur.next = ListNode(num)
        cur = cur.next
    return head


def list_to_array(head: ListNode | None) -> list[int]:
    array = []
    while head:
        array.append(head.val)
        head = head.next
    return array


def get_length(head: ListNode | None) -> int:
    length = 0
    while head:
        length += 1
        head = head.next
    return length


def make_cycle(head: ListNode | None, pos: int) -> ListNode | None:
    """Create a cycle in the linked list at the given position (0-indexed)."""
    if not head or pos < 0:
        return head

    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next

    if pos < len(nodes):
        nodes[-1].next = nodes[pos]
    return head


def has_cycle(head: ListNode | None) -> bool:
    """Detect if a linked list has a cycle using Floyd's Cycle Detection Algorithm."""
    if not head or not head.next:
        return False

    fast, slow = head, head

    while fast and fast.next:
        slow = slow.next  # type: ignore
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def reverse_list(head: ListNode | None) -> ListNode | None:
    prev = None
    cur = head
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    return prev
