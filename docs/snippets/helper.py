class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def create(nums, pos=-1):
        if not nums:
            return None

        head = ListNode(nums[0])
        cur = head
        cycle_node = None

        for i, val in enumerate(nums[1:], start=1):
            cur.next = ListNode(val)
            cur = cur.next
            if i == pos:
                cycle_node = cur

        if pos >= 0:
            cur.next = cycle_node

        return head

    def __str__(self):
        result = []
        cur = self
        visited = set()

        while cur and cur not in visited:
            result.append(str(cur.val))
            visited.add(cur)
            cur = cur.next

        if cur:
            result.append("...")

        return " -> ".join(result)
