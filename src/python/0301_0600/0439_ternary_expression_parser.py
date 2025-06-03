# Stack
def parseTernary(expression: str) -> str:
    stack = []
    i = len(expression) - 1

    while i >= 0:
        c = expression[i]
        if stack and stack[-1] == "?":
            stack.pop()  # remove '?'
            true_val = stack.pop()
            stack.pop()  # remove ':'
            false_val = stack.pop()
            if c == "T":
                stack.append(true_val)
            else:
                stack.append(false_val)
        else:
            stack.append(c)
        i -= 1

    return stack[-1]


if __name__ == "__main__":
    assert parseTernary("T?2:3") == "2"
    assert parseTernary("F?1:T?4:5") == "4"
    assert parseTernary("T?T?F:5:3") == "F"
