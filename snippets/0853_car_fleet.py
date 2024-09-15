from typing import List


# Stack
def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    cars = sorted(zip(position, speed), reverse=True)
    stack = []

    for p, s in cars:
        time = (target - p) / s

        if not stack or time > stack[-1]:
            stack.append(time)

    return len(stack)


print(carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))  # 3
