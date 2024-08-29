from typing import List


# Left Right Pointers
def twoSum(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]

        if total > target:
            right -= 1
        elif total < target:
            left += 1
        else:
            return [left + 1, right + 1]


# |-------------|-----------------|--------------|
# |  Approach   |      Time       |    Space     |
# |-------------|-----------------|--------------|
# | Left Right  |      O(n)       |    O(1)      |
# |-------------|-----------------|--------------|


numbers = [2, 7, 11, 15]
target = 9
print(twoSum(numbers, target))  # [1, 2]
