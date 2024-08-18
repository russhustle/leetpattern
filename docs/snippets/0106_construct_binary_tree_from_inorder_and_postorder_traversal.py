from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    """
    inorder:    left root  right   1  2  3
    postorder:  left right root    4  5  6
    """

    if not postorder:
        return None

    root_val = postorder[-1]  # 6
    root = TreeNode(root_val)

    separator_idx = inorder.index(root_val)  # 2

    left_inorder = inorder[:separator_idx]  # 1
    right_inorder = inorder[separator_idx + 1 :]  # 3

    left_postorder = postorder[: len(left_inorder)]  # 4
    right_postorder = postorder[len(left_inorder) : -1]  # 5

    root.left = buildTree(left_inorder, left_postorder)
    root.right = buildTree(right_inorder, right_postorder)

    return root


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
root = buildTree(inorder, postorder)
print(root)
#     3
#    / \
#   9  20
#     /  \
#    15   7
