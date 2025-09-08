from typing import List, Optional


class ListNode:
    def __init__(
        self, val: int = 0, next: Optional["ListNode"] = None
    ) -> None:
        self.val = val
        self.next = next

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ListNode):
            return False
        return self.val == other.val

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


class LinkedList:
    def __init__(
        self, input_data: Optional[List[int] | ListNode] = None
    ) -> None:
        if isinstance(input_data, list):
            self.head = list_from_array(input_data)
        elif isinstance(input_data, ListNode) or input_data is None:
            self.head = input_data
        else:
            raise ValueError(
                "Invalid input: must be a list of ints or a ListNode"
            )

    def to_array(self) -> List[int]:
        return list_to_array(self.head)

    def __str__(self) -> str:
        return " -> ".join(map(str, self.to_array())) or "Empty"

    def __len__(self) -> int:
        return get_length(self.head)

    def __bool__(self) -> bool:
        return self.head is not None

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LinkedList):
            return False
        return self.to_array() == other.to_array()

    def append(self, val: int) -> None:
        new = ListNode(val)
        if not self.head:
            self.head = new
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new

    def prepend(self, val: int) -> None:
        new = ListNode(val)
        new.next = self.head
        self.head = new

    def insert(self, index: int, val: int) -> None:
        if index < 0:
            raise ValueError("Index cannot be negative")
        if index == 0:
            self.prepend(val)
            return

        cur = self.head
        for i in range(index - 1):
            if not cur:
                raise IndexError("Index out of range")
            cur = cur.next

        if not cur:
            raise IndexError("Index out of range")

        new_node = ListNode(val)
        new_node.next = cur.next
        cur.next = new_node

    def delete(self, val: int) -> bool:
        if not self.head:
            return False

        if self.head.val == val:
            self.head = self.head.next
            return True

        cur = self.head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                return True
            cur = cur.next
        return False

    def delete_at(self, index: int) -> int:
        if index < 0 or not self.head:
            raise IndexError("Index out of range")

        if index == 0:
            val = self.head.val
            self.head = self.head.next
            return val

        cur = self.head
        for i in range(index - 1):
            if not cur or not cur.next:
                raise IndexError("Index out of range")
            cur = cur.next

        if not cur.next:
            raise IndexError("Index out of range")

        val = cur.next.val
        cur.next = cur.next.next
        return val

    def find(self, val: int) -> int:
        cur = self.head
        index = 0
        while cur:
            if cur.val == val:
                return index
            cur = cur.next
            index += 1
        return -1

    def get(self, index: int) -> int:
        if index < 0:
            raise IndexError("Index cannot be negative")

        cur = self.head
        for i in range(index):
            if not cur:
                raise IndexError("Index out of range")
            cur = cur.next

        if not cur:
            raise IndexError("Index out of range")

        return cur.val

    def clear(self) -> None:
        self.head = None

    def copy(self) -> "LinkedList":
        return LinkedList(self.to_array())

    def make_cycle(self, pos: int) -> None:
        make_cycle(self.head, pos)

    def reverse(self) -> None:
        self.head = reverse_list(self.head)

    def has_cycle(self) -> bool:
        return has_cycle(self.head)

    def get_middle(self) -> Optional[int]:
        if not self.head:
            return None

        slow = fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next  # type: ignore
            fast = fast.next.next

        return slow.val  # type: ignore

    def remove_duplicates(self) -> None:
        if not self.head:
            return

        cur = self.head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next


def list_from_array(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None

    head = ListNode(arr[0])
    cur = head
    for val in arr[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head


def list_to_array(head: Optional[ListNode]) -> List[int]:
    arr = []
    cur = head
    while cur:
        arr.append(cur.val)
        cur = cur.next
    return arr


def get_length(head: Optional[ListNode]) -> int:
    count = 0
    cur = head
    while cur:
        count += 1
        cur = cur.next
    return count


def make_cycle(head: Optional[ListNode], pos: int) -> Optional[ListNode]:
    if not head or pos < 0:
        return head

    cycle_start = None
    cur = head
    index = 0
    prev = None

    while cur:
        if index == pos:
            cycle_start = cur
        prev = cur
        cur = cur.next
        index += 1

    if prev and cycle_start:
        prev.next = cycle_start

    return head


def has_cycle(head: Optional[ListNode]) -> bool:
    if not head or not head.next:
        return False

    slow = fast = head

    while fast and fast.next:
        slow = slow.next  # type: ignore
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    cur = head

    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node

    return prev


if __name__ == "__main__":
    ll = LinkedList([1, 2, 3, 4, 5])
    print(ll)
