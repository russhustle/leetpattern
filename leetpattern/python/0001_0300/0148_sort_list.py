from typing import Optional

from leetpattern.utils import ListNode, list_from_array


# Linked List
def sortListSort(head: Optional[ListNode]) -> Optional[ListNode]:
    nums = []

    while head:
        nums.append(head.val)
        head = head.next

    dummy = ListNode()
    cur = dummy
    nums.sort()

    for num in nums:
        cur.next = ListNode(val=num)
        cur = cur.next

    return dummy.next


# Linked List
def sortListDivideConquer(head: Optional[ListNode]) -> Optional[ListNode]:
    def middle(node):
        fast, slow = node, node
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        return slow

    def merge_two_lists(l1, l2):
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 if l1 else l2
        return dummy.next

    if not head or not head.next:
        return head

    head2 = middle(head)
    head = sortListDivideConquer(head)
    head2 = sortListDivideConquer(head2)

    return merge_two_lists(head, head2)


head = list_from_array([4, 2, 1, 3])
print(head)  # 4 -> 2 -> 1 -> 3
print(sortListSort(head))  # 1 -> 2 -> 3 -> 4
print(sortListDivideConquer(head))  # 1 -> 2 -> 3 -> 4
