class lengthOfLastWord:
    def array(self, s: str) -> int:
        res = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                res += 1
            elif s[i] == " " and res > 0:
                return res

        return res


if __name__ == "__main__":
    solution = lengthOfLastWord()
    assert solution.array("Hello World") == 5
