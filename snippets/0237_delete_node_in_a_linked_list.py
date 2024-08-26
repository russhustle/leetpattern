from helper import ListNode


def deleteNode(node: ListNode) -> None:
    node.val = node.next.val
    node.next = node.next.next


head = ListNode.create([4, 5, 1, 9])
node = head.next
deleteNode(node)
print(head)  # 4 -> 1 -> 9
