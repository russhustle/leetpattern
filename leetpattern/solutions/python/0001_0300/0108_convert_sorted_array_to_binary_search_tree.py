from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    if len(nums) == 0:
        return None

    mid = len(nums) // 2
    root = TreeNode(nums[mid])

    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1 :])

    return root


nums = [-10, -3, 0, 5, 9]
root = sortedArrayToBST(nums)
#      0
#     / \
#   -3   9
#   /   /
# -10  5
