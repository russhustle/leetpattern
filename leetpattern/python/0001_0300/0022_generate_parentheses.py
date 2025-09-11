from typing import List


# Backtracking
def generateParenthesis1(n: int) -> List[str]:
    path, res = [], []

    def dfs(openN, closeN):
        if openN == closeN == n:
            res.append("".join(path))
            return

        if openN < n:
            path.append("(")
            dfs(openN + 1, closeN)
            path.pop()

        if closeN < openN:
            path.append(")")
            dfs(openN, closeN + 1)
            path.pop()

    dfs(0, 0)

    return res


# Backtracking
def generateParenthesis2(n: int) -> List[str]:
    m = n * 2
    res, path = [], [""] * m

    def dfs(i, left):
        if i == m:
            res.append("".join(path))
            return

        if left < n:
            path[i] = "("
            dfs(i + 1, left + 1)
        if i - left < left:
            path[i] = ")"
            dfs(i + 1, left)

    dfs(0, 0)
    return res


if __name__ == "__main__":
    print(generateParenthesis1(3))
    # ['((()))', '(()())', '(())()', '()(())', '()()()']
    print(generateParenthesis2(3))
    # ['((()))', '(()())', '(())()', '()(())', '()()()']
