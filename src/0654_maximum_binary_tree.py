from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def constructMaximumBinaryTree(nums: List[int]) -> Optional[TreeNode]:
    if len(nums) == 0:
        return None

    maximum = max(nums)
    rootIndex = nums.index(maximum)

    root = TreeNode(maximum)

    left_nums = nums[:rootIndex]
    right_nums = nums[rootIndex + 1 :]

    root.left = constructMaximumBinaryTree(left_nums)
    root.right = constructMaximumBinaryTree(right_nums)

    return root


nums = [3, 2, 1, 6, 0, 5]
root = constructMaximumBinaryTree(nums)
#     __6__
#    /     \
#   3       5
#    \     /
#     2   0
#      \
#       1
