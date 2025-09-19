def distributeCandies(n: int, limit: int) -> int:
    def c2(n: int) -> int:
        return n * (n - 1) // 2 if n > 1 else 0

    return (
        c2(n + 2) - 3 * c2(n - limit + 1) + 3 * c2(n - 2 * limit) - c2(n - 3 * limit - 1)
    )


if __name__ == "__main__":
    assert distributeCandies(5, 2) == 3
    assert distributeCandies(3, 3) == 10
