# Monotonic Stack
def removeDuplicateLetters(s: str) -> str:
    stack = []
    seen = set()
    last = {c: i for i, c in enumerate(s)}

    for i, c in enumerate(s):
        if c not in seen:
            while stack and c < stack[-1] and i < last[stack[-1]]:
                seen.discard(stack.pop())
            seen.add(c)
            stack.append(c)

    return "".join(stack)


s = "cbacdcbc"
print(removeDuplicateLetters(s))  # acdb
