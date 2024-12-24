from collections import defaultdict
from typing import List


# Stack
class Solution:
    def __init__(self):
        self.operators = set(["+", "-", "*"])

    def basicCalculatorIV(
        self, expression: str, evalvars: List[str], evalints: List[int]
    ) -> List[str]:
        evalmap = dict(zip(evalvars, evalints))
        tokens = self.parse_expression(expression)
        result_terms = self.evaluate(tokens, evalmap)
        return self.format_result(result_terms)

    def parse_expression(self, expression):
        tokens = []
        i = 0
        while i < len(expression):
            if expression[i].isalnum():  # Variable or digit
                start = i
                while i < len(expression) and (
                    expression[i].isalnum() or expression[i] == "_"
                ):
                    i += 1
                tokens.append(expression[start:i])
            elif expression[i] in self.operators or expression[i] in "()":
                tokens.append(expression[i])
                i += 1
            elif expression[i] == " ":
                i += 1  # skip whitespace
        return tokens

    def evaluate(self, tokens, evalmap):
        def apply_operator(op, b, a):
            if op == "+":
                return self.add_terms(a, b)
            elif op == "-":
                return self.add_terms(a, self.negate_terms(b))
            elif op == "*":
                return self.multiply_terms(a, b)

        def process_token(token):
            if token.isalnum():
                if token in evalmap:
                    stack.append({(): evalmap[token]})
                elif token.isdigit():
                    stack.append({(): int(token)})
                else:
                    stack.append({(token,): 1})
            elif token == "(":
                ops.append(token)
            elif token == ")":
                while ops and ops[-1] != "(":
                    operate()
                ops.pop()
            else:
                while (
                    ops
                    and ops[-1] in precedence
                    and precedence[ops[-1]] >= precedence[token]
                ):
                    operate()
                ops.append(token)

        def operate():
            if len(stack) < 2 or not ops:
                return
            b = stack.pop()
            a = stack.pop()
            op = ops.pop()
            stack.append(apply_operator(op, b, a))

        stack = []
        ops = []
        precedence = {"+": 1, "-": 1, "*": 2}

        for token in tokens:
            process_token(token)

        while ops:
            operate()
        return self.combine_terms(stack[-1])

    def add_terms(self, a, b):
        result = defaultdict(int, a)
        for term, coef in b.items():
            result[term] += coef
        return dict(result)

    def negate_terms(self, a):
        return {term: -coef for term, coef in a.items()}

    def multiply_terms(self, a, b):
        result = defaultdict(int)
        for term1, coef1 in a.items():
            for term2, coef2 in b.items():
                new_term = tuple(sorted(term1 + term2))
                result[new_term] += coef1 * coef2
        return dict(result)

    def combine_terms(self, terms):
        result = defaultdict(int)
        for term, coef in terms.items():
            if coef != 0:
                result[term] = coef
        return dict(result)

    def format_result(self, result_terms):
        result = []
        for term in sorted(result_terms.keys(), key=lambda x: (-len(x), x)):
            coef = result_terms[term]
            if coef != 0:
                term_str = "*".join(term)
                if term_str:
                    result.append(f"{coef}*{term_str}")
                else:
                    result.append(str(coef))
        return result


calculator = Solution()
expression = "e + 8 - a + 5"
evalvars = ["e"]
evalints = [1]
print(calculator.basicCalculatorIV(expression, evalvars, evalints))
# ['-1*a', '14']
