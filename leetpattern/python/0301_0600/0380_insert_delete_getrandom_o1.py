import random


class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.pos = {}  # num: idx

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False

        idx = self.pos[val]
        last_val = self.nums[-1]
        self.nums[idx] = last_val
        self.pos[last_val] = idx

        self.nums.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


def test_RandomizedSet():
    obj = RandomizedSet()
    assert obj.insert(1)
    assert not obj.remove(2)
    assert obj.insert(2)
    assert obj.getRandom() in [1, 2]
    assert obj.remove(1)
    assert not obj.insert(2)
    assert obj.getRandom() == 2
