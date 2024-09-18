# Stack
def calculate(s: str) -> int:
    def helper(index):
        stack = []
        num = 0
        sign = "+"

        while index < len(s):
            char = s[index]
            if char.isdigit():
                num = num * 10 + int(char)
            if char == "(":
                num, index = helper(index + 1)
            if char in "+-*/)" or index == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(int(stack.pop() / num))  # 向零取整
                num = 0
                sign = char
            if char == ")":
                break
            index += 1

        return sum(stack), index

    s = s.replace(" ", "")
    result, _ = helper(0)

    return result


s = "2*(5+5*2)/3+(6/2+8)"
print(calculate(s))  # 21
