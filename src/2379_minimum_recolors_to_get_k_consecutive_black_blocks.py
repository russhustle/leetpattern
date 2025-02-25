# Sliding Window Fixed Size
def minimumRecolors(blocks: str, k: int) -> int:
    cnt, res = 0, float("inf")

    for idx, block in enumerate(blocks):
        if block == "W":
            cnt += 1

        if idx < k - 1:
            continue

        res = min(res, cnt)

        if blocks[idx - k + 1] == "W":
            cnt -= 1

    return res


blocks = "WBBWWBBWBW"
k = 7
print(minimumRecolors(blocks, k))  # 3
