# Sliding Window - Variable
def maxConsecutiveAnswers1(answerKey: str, k: int) -> int:
    def maxConsecutiveChar(s: str, k: int, char: str) -> int:
        max_len = 0
        left = 0
        count = 0  # num of str != char

        for right in range(len(s)):
            if s[right] != char:
                count += 1

            while count > k:
                if s[left] != char:
                    count -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

    max_t = maxConsecutiveChar(answerKey, k, "T")
    max_f = maxConsecutiveChar(answerKey, k, "F")

    return max(max_t, max_f)


# Sliding Window - Variable
def maxConsecutiveAnswers2(answerKey: str, k: int) -> int:
    def maxConsecutiveChar(s: str, k: int, char: str) -> int:
        max_len = 0
        left, right = 0, 0

        while right < len(s):
            if s[right] != char:
                k -= 1

            while k < 0:
                if s[left] != char:
                    k += 1
                left += 1

            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len

    max_t = maxConsecutiveChar(answerKey, k, "T")
    max_f = maxConsecutiveChar(answerKey, k, "F")

    return max(max_t, max_f)


# |-----------------|---------|------------|
# |  Approach       |  Time   |  Space     |
# |-----------------|---------|------------|
# | Sliding Window  |  O(N)   |  O(1)      |
# |-----------------|---------|------------|


answerKey = "TTFF"
k = 2
print(maxConsecutiveAnswers1(answerKey, k))  # 4
print(maxConsecutiveAnswers2(answerKey, k))  # 4
