from typing import List

import matplotlib.pyplot as plt


# Monotonic Stack
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    res = [0 for _ in range(len(temperatures))]
    stack = []

    for idx, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            _, last_index = stack.pop()
            res[last_index] = idx - last_index

        stack.append([temp, idx])

    return res


def utils_plot(idx: int, temps: List[int], stack: List[List[int]]) -> None:
    """Plot the current state of the stack and the temperatures."""
    plt.figure(figsize=(8, 3))
    plt.plot(
        range(len(temps)),
        temps,
        marker="o",
        linestyle="-",
        color="b",
        label="Temperatures",
    )

    # Highlight the current temperature in red
    plt.scatter(idx, temps[idx], color="r", s=100, label="Current")

    # Display the current state of the stack
    for temp, stack_idx in stack:
        plt.scatter(stack_idx, temp, color="g", s=70)
        plt.text(
            stack_idx,
            temp,
            f"({temp}, {stack_idx})",
            fontsize=10,
            ha="center",
            va="bottom",
            color="red",
        )

    plt.title(f"Day {idx}")
    plt.xlabel("Days")
    plt.ylabel("Temperature")
    plt.legend()
    plt.grid(True)
    plt.show()


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# [1, 1, 4, 2, 1, 1, 0, 0]
