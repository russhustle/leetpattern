from collections import deque
from typing import List


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = deque(food)
        self.snake = deque([(0, 0)])  # Snake starts at the top-left corner
        self.snake_body = set([(0, 0)])  # To quickly check for collisions
        self.score = 0
        self.dirs = {"U": (-1, 0), "L": (0, -1), "R": (0, 1), "D": (1, 0)}

    def move(self, direction: str) -> int:
        head = self.snake[0]
        dx, dy = self.dirs[direction]
        new_head = (head[0] + dx, head[1] + dy)

        # Check if the new head is out of bounds
        if not (
            0 <= new_head[0] < self.height and 0 <= new_head[1] < self.width
        ):
            return -1

        # Check if the new head collides with the snake body (excluding the tail)
        if new_head in self.snake_body and new_head != self.snake[-1]:
            return -1

        # Check if the new head is on a food cell
        if self.food and self.food[0] == list(new_head):
            self.food.popleft()
            self.score += 1
        else:
            tail = self.snake.pop()
            self.snake_body.remove(tail)

        # Add the new head to the snake
        self.snake.appendleft(new_head)
        self.snake_body.add(new_head)

        return self.score


snake = SnakeGame(3, 2, [[1, 2], [0, 1]])
print(snake.move("R"))  # 0
print(snake.move("D"))  # 0
print(snake.move("R"))  # 1
print(snake.move("U"))  # 1
print(snake.move("L"))  # 2
print(snake.move("U"))  # -1
