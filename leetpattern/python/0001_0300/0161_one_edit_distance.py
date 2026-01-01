class IsOneEditDistance:
    def traverse(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)

        # ensure s is the shorter one
        if m > n:
            return self.traverse(t, s)

        # len difference > 1
        if n - m > 1:
            return False

        for i in range(m):
            if s[i] == t[i]:
                continue

            if m == n:
                return s[i + 1 :] == t[i + 1 :]
            else:
                return s[i:] == t[i + 1 :]

        return m + 1 == n


if __name__ == "__main__":
    sol = IsOneEditDistance()
    assert sol.traverse("ab", "acb") is True
    assert sol.traverse("cab", "ad") is False
    assert sol.traverse("1203", "1213") is True
