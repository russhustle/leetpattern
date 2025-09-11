def lengthOfLastWord(s: str) -> int:
    n = 0

    for i in range(len(s) - 1, -1, -1):
        if s[i] != " ":
            n += 1
        if s[i] == " " and n > 0:
            return n

    return n


print(lengthOfLastWord("Hello World"))  # 5
