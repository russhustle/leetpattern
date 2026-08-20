import heapq
import random
from typing import List


class Solution:
    @staticmethod
    def _partition(nums: List[int], left: int, right: int) -> tuple[int, int]:
        """Split a range into values smaller than, equal to, and greater than pivot."""
        pivot = nums[(left + right) // 2]
        smaller = current = left
        greater = right

        while current <= greater:
            if nums[current] < pivot:
                nums[smaller], nums[current] = nums[current], nums[smaller]
                smaller += 1
                current += 1
            elif nums[current] > pivot:
                nums[current], nums[greater] = nums[greater], nums[current]
                greater -= 1
            else:
                current += 1

        return smaller, greater

    def sort(self, nums: List[int], k: int) -> int:
        """Built-in sort: O(n log n) time, O(n) space in Python."""
        nums.sort(reverse=True)
        return nums[k - 1]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """LeetCode entry point using randomized in-place quickselect."""
        return self.quick_select_in_place(nums, k)

    def min_heap(self, nums: List[int], k: int) -> int:
        """Min-heap: O(n log k) time, O(k) space."""
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]

    def quick_sort(self, nums: List[int], k: int) -> int:
        """In-place quicksort: O(n log n) average time, O(log n) average space."""
        ranges = [(0, len(nums) - 1)]

        while ranges:
            left, right = ranges.pop()
            if left >= right:
                continue

            equal_start, equal_end = self._partition(nums, left, right)
            left_range = (left, equal_start - 1)
            right_range = (equal_end + 1, right)

            # Process the smaller range first to keep the stack small.
            if left_range[1] - left_range[0] > right_range[1] - right_range[0]:
                left_range, right_range = right_range, left_range
            ranges.append(right_range)
            ranges.append(left_range)

        return nums[-k]

    def quick_select_recursive(self, nums: List[int], k: int) -> int:
        """
        Find the kth largest using recursive list partitions.

        k largest
        3, 2, 1, 5, 6, 4
        0  1  2  3  4  5

        Time: O(n) average, O(n^2) worst case.
        Space: O(n) average for partitions and recursion.
        """
        pivot = random.choice(nums)

        left = [number for number in nums if number > pivot]
        mid = [number for number in nums if number == pivot]
        right = [number for number in nums if number < pivot]

        if len(left) >= k:
            return self.quick_select_recursive(left, k)
        if len(left) + len(mid) >= k:
            return pivot
        return self.quick_select_recursive(right, k - len(left) - len(mid))

    def quick_select_in_place(self, nums: List[int], k: int) -> int:
        """
        Find the kth largest using randomized in-place quickselect.

        The kth largest is the (n - k)th smallest using a zero-based index.
        Time: O(n) average, O(n^2) worst case.
        Space: O(1), because partitioning is iterative and in place.
        """
        target = len(nums) - k

        def partition(left: int, right: int) -> int:
            pivot = random.randint(left, right)
            nums[pivot], nums[right] = nums[right], nums[pivot]
            pivot = nums[right]

            store = left
            for index in range(left, right):
                if nums[index] < pivot:
                    nums[index], nums[store] = nums[store], nums[index]
                    store += 1

            nums[store], nums[right] = nums[right], nums[store]
            return store

        left, right = 0, len(nums) - 1

        while left <= right:
            pivot_index = partition(left, right)
            if pivot_index == target:
                return nums[pivot_index]
            if pivot_index < target:
                left = pivot_index + 1
            else:
                right = pivot_index - 1

        raise RuntimeError("quickselect failed to find the target")


if __name__ == "__main__":
    solution = Solution()
    methods = (
        solution.findKthLargest,
        solution.sort,
        solution.min_heap,
        solution.quick_sort,
        solution.quick_select_recursive,
        solution.quick_select_in_place,
    )
    cases = (
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([-1, -1], 2, -1),
        ([1], 1, 1),
    )

    for method in methods:
        for nums, k, expected in cases:
            assert method(nums.copy(), k) == expected
