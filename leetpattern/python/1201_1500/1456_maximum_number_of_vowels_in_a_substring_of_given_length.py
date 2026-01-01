class maxVowels:
    """
    Template problem for Fixed Size Sliding Window.
    Technique: add-update-remove (入-更新-出)
    """

    @staticmethod
    def fixed_sliding_window(s: str, k: int) -> int:
        res, cnt = 0, 0

        for idx, ch in enumerate(s):
            # ADD
            if ch in "aeiou":
                cnt += 1

            # FORM
            if idx < k - 1:
                continue

            # UPDATE
            res = max(res, cnt)

            # REMOVE
            if s[idx - k + 1] in "aeiou":
                cnt -= 1

        return res

    @staticmethod
    def fixed_sliding_window_substring(s: str, k: int) -> int:
        """Sliding Window on Substring"""

        vowels = set("aeiou")
        n = len(s)
        cnt, res = 0, 0

        # init
        for i in range(k):
            if s[i] in vowels:
                cnt += 1

        res = cnt

        # slide
        for i in range(k, n):
            if s[i] in vowels:
                cnt += 1
            if s[i - k] in vowels:
                cnt -= 1
            res = max(res, cnt)

        return res


if __name__ == "__main__":
    s = "abciiidef"
    k = 3
    assert maxVowels.fixed_sliding_window(s, k) == 3
    assert maxVowels.fixed_sliding_window_substring(s, k) == 3
