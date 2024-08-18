from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    p1, p2 = m - 1, n - 1
    tail = m + n - 1

    while p1 >= 0 or p2 >= 0:
        if p1 == -1:
            nums1[tail] = nums2[p2]
            p2 -= 1
        elif p2 == -1:
            nums1[tail] = nums1[p1]
            p1 -= 1

        elif nums1[p1] > nums2[p2]:
            nums1[tail] = nums1[p1]
            p1 -= 1
        else:
            nums1[tail] = nums2[p2]
            p2 -= 1
        tail -= 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  # [1, 2, 2, 3, 5, 6]
