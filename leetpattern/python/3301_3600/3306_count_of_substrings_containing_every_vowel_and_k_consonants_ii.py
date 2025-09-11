from collections import defaultdict


# Sliding Window Variable Subarrays Exact
def countOfSubstrings(word: str, k: int) -> int:
    vowels = {"a", "e", "i", "o", "u"}
    n = len(word)

    def count(m: int) -> int:
        occur = defaultdict(int)
        valid_vow_cnt, con_cnt = 0, 0
        left = 0
        res = 0

        for right in range(n):
            while left < n and (con_cnt < m or valid_vow_cnt < 5):
                if word[left] in vowels:
                    if occur[word[left]] == 0:
                        valid_vow_cnt += 1
                    occur[word[left]] += 1
                else:
                    con_cnt += 1
                left += 1

            if con_cnt >= m and valid_vow_cnt == 5:
                res += n - left + 1

            if word[right] in vowels:
                occur[word[right]] -= 1
                if occur[word[right]] == 0:
                    valid_vow_cnt -= 1
            else:
                con_cnt -= 1

        return res

    return count(k) - count(k + 1)


word = "ieaouqqieaouqq"
k = 1
print(countOfSubstrings(word, k))  # 3
