from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next

    def __eq__(self, other: object) -> bool:
        return isinstance(other, ListNode) and self.val == other.val

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


class LinkedList:
    def __init__(self, input_data: Optional[List[int] | ListNode] = None) -> None:
        if isinstance(input_data, list):
            self.head = self._from_array(input_data)
        elif isinstance(input_data, ListNode) or input_data is None:
            self.head = input_data
        else:
            raise ValueError("Invalid input: must be a list of ints or a ListNode")

    def _from_array(self, arr: List[int]) -> Optional[ListNode]:
        """Convert array to linked list."""
        if not arr:
            return None
        head = ListNode(arr[0])
        cur = head
        for val in arr[1:]:
            cur.next = ListNode(val)
            cur = cur.next
        return head

    def to_array(self) -> List[int]:
        """Convert linked list to array."""
        result = []
        cur = self.head
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result

    def __str__(self) -> str:
        return " -> ".join(map(str, self.to_array())) or "Empty"

    def __len__(self) -> int:
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

    def __bool__(self) -> bool:
        return self.head is not None

    def __eq__(self, other: object) -> bool:
        return isinstance(other, LinkedList) and self.to_array() == other.to_array()

    def append(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def prepend(self, val: int) -> None:
        self.head = ListNode(val, self.head)

    def insert(self, index: int, val: int) -> None:
        if index < 0:
            raise ValueError("Index cannot be negative")
        if index == 0:
            self.prepend(val)
            return

        cur = self.head
        for _ in range(index - 1):
            if not cur:
                raise IndexError("Index out of range")
            cur = cur.next

        if not cur:
            raise IndexError("Index out of range")
        cur.next = ListNode(val, cur.next)

    def delete(self, val: int) -> bool:
        if not self.head:
            return False
        if self.head.val == val:
            self.head = self.head.next
            return True

        cur = self.head
        while cur.next and cur.next.val != val:
            cur = cur.next

        if cur.next:
            cur.next = cur.next.next
            return True
        return False

    def delete_at(self, index: int) -> int:
        if index < 0 or not self.head:
            raise IndexError("Index out of range")

        if index == 0:
            val = self.head.val
            self.head = self.head.next
            return val

        cur = self.head
        for _ in range(index - 1):
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
        for index in range(len(self)):
            if cur.val == val:
                return index
            cur = cur.next
        return -1

    def get(self, index: int) -> int:
        if index < 0:
            raise IndexError("Index cannot be negative")

        cur = self.head
        for _ in range(index):
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

    def reverse(self) -> None:
        prev = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev

    def has_cycle(self) -> bool:
        if not self.head or not self.head.next:
            return False

        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def get_middle(self) -> Optional[int]:
        if not self.head:
            return None

        slow = fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val

    def remove_duplicates(self) -> None:
        cur = self.head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

    def make_cycle(self, pos: int) -> None:
        if not self.head or pos < 0:
            return

        cycle_start = None
        cur = self.head
        prev = None

        for index in range(len(self)):
            if index == pos:
                cycle_start = cur
            prev = cur
            cur = cur.next

        if prev and cycle_start:
            prev.next = cycle_start

    @classmethod
    def from_array(cls, arr: List[int]) -> "LinkedList":
        return cls(arr)
