# Stack
def removeStars(s: str) -> str:
    stack = []

    for char in s:
        if char == "*":
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)


s = "leet**cod*e"
print(removeStars(s))  # "lecoe"
