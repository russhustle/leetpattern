from typing import List


# BST
def verifyPreorder(preorder: List[int]) -> bool:
    stack = []
    low = float("-inf")

    for value in preorder:
        if value < low:
            return False
        while stack and value > stack[-1]:
            low = stack.pop()
        stack.append(value)

    return True


if __name__ == "__main__":
    assert verifyPreorder([8, 5, 1, 7, 10, 12]) is True
    assert verifyPreorder([8, 5, 4, 3, 2, 1]) is True
