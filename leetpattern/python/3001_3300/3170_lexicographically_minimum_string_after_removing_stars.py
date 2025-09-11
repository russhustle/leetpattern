from itertools import chain


# Stack
def clearStars(s: str) -> str:
    stacks = [[] for _ in range(26)]
    for i, c in enumerate(s):
        if c != "*":
            stacks[ord(c) - ord("a")].append(i)
            continue

        for st in stacks:
            if st:
                st.pop()
                break
    return "".join(s[i] for i in sorted(chain.from_iterable(stacks)))


if __name__ == "__main__":
    assert clearStars("aaba*") == "aab"
