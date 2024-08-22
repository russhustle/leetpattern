from typing import List


# Sliding Window - Variable
def subarraysWithKDistinct(nums: List[int], k: int) -> int:
    def atMost(k: int) -> int:
        count = 0
        left = 0
        freq = {}

        for right in range(len(nums)):
            if nums[right] not in freq:
                freq[nums[right]] = 0
            freq[nums[right]] += 1

            while len(freq) > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            count += right - left + 1

        return count

    return atMost(k) - atMost(k - 1)


nums = [1, 2, 1, 2, 3]
k = 2
print(subarraysWithKDistinct(nums, k))  # 7
