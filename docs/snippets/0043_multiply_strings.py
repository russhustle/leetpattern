# Math
def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    m, n = len(num1), len(num2)
    result = [0 for _ in range(m + n)]

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            mul = int(num1[i]) * int(num2[j])
            sum = mul + result[i + j + 1]

            result[i + j + 1] = sum % 10
            result[i + j] += sum // 10

    result_str = "".join(map(str, result)).lstrip("0")

    return result_str if result_str else "0"


num1 = "2"
num2 = "3"
print(multiply(num1, num2))  # "6"
