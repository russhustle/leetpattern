"""
-   Remove all adjacent characters that are the same and have different cases.
-   Steps for the string `leEeetcode`:

| char | action | stack      |
| ---- | ------ | ---------- |
| l    | push   | "l"        |
| e    | push   | "le"       |
| E    | pop    | "l"        |
| e    | push   | "le"       |
| e    | push   | "lee"      |
| t    | push   | "leet"     |
| c    | push   | "leetc"    |
| o    | push   | "leetco"   |
| d    | push   | "leetcod"  |
| e    | push   | "leetcode" |
"""


# Stack
def makeGood(s: str) -> str:
    stack = []

    for i in range(len(s)):
        if stack and stack[-1] == s[i].swapcase():
            stack.pop()
        else:
            stack.append(s[i])
    return "".join(stack)


print(makeGood("leEeetcode"))  # "leetcode"
