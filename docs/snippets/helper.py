class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def create(nums, pos=-1):
        if not nums:
            return None

        head = ListNode(nums[0])
        current = head
        cycle_node = None

        for i, val in enumerate(nums[1:], start=1):
            current.next = ListNode(val)
            current = current.next
            if i == pos:
                cycle_node = current

        if pos >= 0:
            current.next = cycle_node

        return head

    def __str__(self):
        result = []
        current = self
        visited = set()

        while current and current not in visited:
            result.append(str(current.val))
            visited.add(current)
            current = current.next

        if current:
            result.append("...")

        return " -> ".join(result)
