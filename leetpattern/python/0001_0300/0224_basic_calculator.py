class Solution:
    def calculate(self, s: str) -> int:
        """Stack: O(n) time, O(n) space.
        Use stack to save result and sign before '(',
        restore after ')'.
        """
        stack = []
        res = 0
        num = 0
        sign = 1

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == "+":
                res += sign * num
                num = 0
                sign = 1
            elif char == "-":
                res += sign * num
                num = 0
                sign = -1
            elif char == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif char == ")":
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()

        res += sign * num
        return res


def test_calculate():
    s = Solution()
    for fn in (s.calculate,):
        assert fn("1 + 1") == 2
        assert fn(" 2-1 + 2 ") == 3
        assert fn("(1+(4+5+2)-3)+(6+8)") == 23
        assert fn("0") == 0
