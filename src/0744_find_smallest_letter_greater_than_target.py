from typing import List


# Binary Search
def nextGreatestLetter(letters: List[str], target: str) -> str:
    left, right = 0, len(letters)

    while left < right:
        mid = left + (right - left) // 2
        if letters[mid] > target:
            right = mid
        else:
            left = mid + 1

    return letters[left] if left < len(letters) else letters[0]


letters = ["c", "f", "j"]
target = "a"
print(nextGreatestLetter(letters, target))  # c
