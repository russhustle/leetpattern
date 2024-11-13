from typing import List


# Monotonic Stack
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    # Returns a list of days you would have to wait until a warmer temperature.

    result = [0 for _ in range(len(temperatures))]
    stack = []

    for idx, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            _, last_index = stack.pop()
            result[last_index] = idx - last_index

        stack.append([temp, idx])

    return result


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# [1, 1, 4, 2, 1, 1, 0, 0]

# | Index | Temp | > stack last   | stack                         | result    |
# | ----- | ---- | -------------- | ----------------------------- | --------- |
# | 0     | 73   | False          | [ [73, 0] ]                   | 1 - 0 = 1 |
# | 1     | 74   | True           | [ [74, 1] ]                   | 2 - 1 = 1 |
# | 2     | 75   | True           | [ [75, 2] ]                   | 6 - 2 = 4 |
# | 3     | 71   | False          | [ [75, 2], [71, 3] ]          | 5 - 3 = 2 |
# | 4     | 69   | False          | [ [75, 2], [71, 3], [69, 4] ] | 5 - 4 = 1 |
# | 5     | 72   | True           | [ [75, 2], [72, 5] ]          | 6 - 5 = 1 |
# | 6     | 76   | True           | [ [76, 6] ]                   | 0         |
# | 7     | 73   | False          | [[76, 6], [73, 7]]            | 0         |
# | ----- | ---- | -------------- | ----------------------------- | --------- |
