"""
-   Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.dummy = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        current = self.dummy.next
        for _ in range(index):
            current = current.next

        return current.val

    def addAtHead(self, val: int) -> None:
        self.dummy.next = ListNode(val, self.dummy.next)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        current = self.dummy
        while current.next:
            current = current.next
        current.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        current = self.dummy
        for i in range(index):
            current = current.next
        current.next = ListNode(val, current.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        current = self.dummy
        for i in range(index):
            current = current.next
        current.next = current.next.next
        self.size -= 1


ll = MyLinkedList()
ll.addAtHead(1)
ll.addAtTail(3)
ll.addAtIndex(1, 2)  # 1 -> 2 -> 3
print(ll.get(1))  # 2
