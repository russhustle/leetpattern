"""
-   Design a class `StockSpanner` to return the number of consecutive days (including the current day) the price of the stock has been less than or equal to the current price.
"""

from typing import List


# Monotonic Stack
class StockSpanner:

    def __init__(self):
        self.stack = [(-1, float("inf"))]
        self.cur_day = -1

    def next(self, price: int) -> int:
        while price >= self.stack[-1][1]:
            self.stack.pop()
        self.cur_day += 1
        self.stack.append((self.cur_day, price))
        return self.cur_day - self.stack[-2][0]


if __name__ == "__main__":
    ss = StockSpanner()
    prices = [100, 80, 60, 70, 60, 75, 85]
    print([ss.next(price) for price in prices])  # [1, 1, 1, 2, 1, 4, 6]
