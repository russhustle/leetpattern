from typing import List


def largestAltitude(gain: List[int]) -> int:
    result, altitude = 0, 0

    for i in gain:
        altitude += i
        result = max(result, altitude)

    return result


gain = [-5, 1, 5, 0, -7]
print(largestAltitude(gain))  # 1
