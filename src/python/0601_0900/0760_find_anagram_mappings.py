from typing import List


def anagramMappings(nums1: List[int], nums2: List[int]) -> List[int]:
    hashmap = {val: idx for idx, val in enumerate(nums2)}

    return [hashmap[num] for num in nums1]


if __name__ == "__main__":
    nums1 = [12, 28, 46, 32, 50]
    nums2 = [50, 12, 32, 46, 28]
    print(anagramMappings(nums1, nums2))  # [1, 4, 3, 2, 0]
    nums1 = [1, 2, 3]
    nums2 = [3, 2, 1]
    print(anagramMappings(nums1, nums2))  # [2, 1, 0]
