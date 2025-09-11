from collections import deque


# Deque
class MovingAverage:
    def __init__(self, size: int):
        self.q = deque()
        self.cur = 0
        self.sum = 0
        self.size = size

    def next(self, val: int) -> float:
        if self.cur >= self.size:
            self.sum -= self.q.popleft()
            self.cur -= 1

        self.q.append(val)
        self.sum += val
        self.cur += 1

        return self.sum / self.cur


if __name__ == "__main__":
    ma = MovingAverage(3)
    assert ma.next(1) == 1.0
    assert ma.next(10) == 5.5
    assert ma.next(3) == 4.666666666666667
    assert ma.next(5) == 6.0
