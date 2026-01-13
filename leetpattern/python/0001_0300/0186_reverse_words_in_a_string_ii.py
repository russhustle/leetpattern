from typing import List


class reverseWords:
    def left_right_pointers(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        s.reverse()

        left = 0
        while left < n:
            if s[left] == " ":
                left += 1
                continue

            # detect the word boundary
            right = left
            while right < n and s[right] != " ":
                right += 1

            # reverse the word
            l, r = left, right - 1
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

            left = right


if __name__ == "__main__":
    sol = reverseWords()
    s = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s"]
    sol.left_right_pointers(s)
    assert s == ["i", "s", " ", "s", "k", "y", " ", "t", "h", "e"]
