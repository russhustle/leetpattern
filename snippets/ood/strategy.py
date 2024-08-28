from abc import ABC, abstractmethod


class FilterStrategy(ABC):
    @abstractmethod
    def removeValue(self, val):
        pass


class RemoveNegativeStrategy(FilterStrategy):
    def removeValue(self, val):
        return val < 0


class RemoveOddStrategy(FilterStrategy):
    def removeValue(self, val):
        return abs(val) % 2 != 0


class Values:
    def __init__(self, vals):
        self.vals = vals

    def filter(self, strategy: FilterStrategy):
        filtered = []

        for val in self.vals:
            if not strategy.removeValue(val):
                filtered.append(val)

        return filtered


values = Values([-6, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6])
print(values.filter(RemoveNegativeStrategy()))  # [0, 1, 2, 3, 4, 5, 6]
print(values.filter(RemoveOddStrategy()))  # [-6, -4, -2, 0, 2, 4, 6]
