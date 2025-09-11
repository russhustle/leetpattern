# Stack
def longestValidParentheses(s: str) -> int:
    stack = [-1]
    res = 0

    for i, ch in enumerate(s):
        if ch == "(":
            stack.append(i)
        elif ch == ")":
            stack.pop()
            if stack:
                res = max(res, i - stack[-1])
            else:
                stack.append(i)

    return res


if __name__ == "__main__":
    print(longestValidParentheses("(()"))  # 2
    print(longestValidParentheses(")()())"))  # 4
