def minimizedStringLength(s: str) -> int:
    return len(set(s))


if __name__ == "__main__":
    s = "aaabc"
    print(minimizedStringLength(s))  # 3
