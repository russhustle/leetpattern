# Valid Parentheses Strings
def canBeValid(s: str, locked: str) -> bool:
    if len(s) % 2:
        return False

    mx, mn = 0, 0
    for ch, lock in zip(s, locked):
        if lock == "1":
            d = 1 if ch == "(" else -1
            mx += d
            if mx < 0:
                return False
            mn += d
        else:
            mx += 1
            mn -= 1

        if mn < 0:
            mn = 1

    return mn == 0


if __name__ == "__main__":
    s = "))()))"
    locked = "010100"
    print(canBeValid(s, locked))  # True
