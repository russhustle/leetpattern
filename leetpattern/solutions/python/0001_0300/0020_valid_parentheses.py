# Stack
def is_valid(s: str) -> bool:
    if len(s) % 2:
        return False

    pairs = {
        "(": ")",
        "{": "}",
        "[": "]",
    }
    stack = []
    for ch in s:
        if ch in pairs:
            stack.append(ch)
        elif not stack or ch != pairs[stack.pop()]:
            return False

    return True if not stack else False


def test_is_valid():
    assert is_valid("()[]{}")
    assert not is_valid("(]")
    assert not is_valid("([)]")
    assert is_valid("{[]}")
