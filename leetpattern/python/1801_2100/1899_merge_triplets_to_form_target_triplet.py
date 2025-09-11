from typing import List


def mergeTriplets(triplets: List[List[int]], target: List[int]) -> bool:
    can_form = [False, False, False]

    for triplet in triplets:
        if all(triplet[i] <= target[i] for i in range(3)):
            for i in range(3):
                if triplet[i] == target[i]:
                    can_form[i] = True

    return all(can_form)


triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
target = [2, 7, 5]
print(mergeTriplets(triplets, target))  # True
