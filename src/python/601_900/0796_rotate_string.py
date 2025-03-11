# String
def rotateString(s: str, goal: str) -> bool:
    n = len(s)
    s += s

    for i in range(n):
        if s[i : i + n] == goal:
            return True

    return False


s = "abcde"
goal = "cdeab"
print(rotateString(s, goal))  # True
