from collections import defaultdict, deque
from typing import List


# Deque
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.all = set()
        self.multi = set()

        for num in nums:
            if num in self.all:
                self.multi.add(num)
            self.all.add(num)

        self.q = deque([i for i in nums if i not in self.multi])

    def showFirstUnique(self) -> int:
        while self.q and self.q[0] in self.multi:
            self.q.popleft()
        return self.q[0] if self.q else -1

    def add(self, value: int) -> None:
        if value not in self.all:
            self.all.add(value)
            self.q.append(value)
        elif value not in self.multi:
            self.multi.add(value)


if __name__ == "__main__":
    nums = [2, 3, 5]
    firstUnique = FirstUnique(nums)
    assert firstUnique.showFirstUnique() == 2
    firstUnique.add(5)
    assert firstUnique.showFirstUnique() == 2
    firstUnique.add(2)
    assert firstUnique.showFirstUnique() == 3
    firstUnique.add(3)
    assert firstUnique.showFirstUnique() == -1
