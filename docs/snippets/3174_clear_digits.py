# Stack
def clearDigits(s: str) -> str:
    stack = []

    for char in s:
        if char.isdigit():
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)


s = "abc"
print(clearDigits(s))  # abc
