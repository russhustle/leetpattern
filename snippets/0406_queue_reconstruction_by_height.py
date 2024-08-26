from typing import List


# Greedy
def reconstructQueue(people: List[List[int]]) -> List[List[int]]:
    queue = []
    people.sort(key=lambda x: (-x[0], x[1]))

    for i in people:
        queue.insert(i[1], i)

    return queue


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(reconstructQueue(people))
# [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
