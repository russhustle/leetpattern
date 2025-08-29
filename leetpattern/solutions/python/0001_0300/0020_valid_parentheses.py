"""
-   Determine if the input string is valid.
-   Steps for the string `()[]{}`:

| char | action | stack |
| ---- | ------ | ----- |
| `(`  | push   | "("   |
| `)`  | pop    | ""    |
| `[`  | push   | "["   |
| `]`  | pop    | ""    |
| `{`  | push   | "{"   |
| `}`  | pop    | ""    |
"""


# Stack
def isValid(s: str) -> bool:
    hashmap = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    stack = []

    for ch in s:
        if ch in hashmap:
            if stack and stack[-1] == hashmap[ch]:
                stack.pop()
            else:
                return False
        else:
            stack.append(ch)

    return True if not stack else False


if __name__ == "__main__":
    assert isValid("()[]{}")
    assert not isValid("(]")
    assert not isValid("([)]")
    assert isValid("{[]}")
    assert isValid("")
