def confusingNumber(n: int) -> bool:
    rotate_map = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
    original = str(n)
    rotated = ""

    for ch in reversed(original):
        if ch not in rotate_map:
            return False
        rotated += rotate_map[ch]

    return rotated != original


if __name__ == "__main__":
    print(confusingNumber(6))  # True
    print(confusingNumber(89))  # True
    print(confusingNumber(11))  # False
