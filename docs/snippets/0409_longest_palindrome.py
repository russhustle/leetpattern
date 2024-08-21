def longestPalindrome(s: str) -> int:
    hashmap = dict()
    result = 0

    for char in s:
        if char not in hashmap or hashmap[char] == 0:
            hashmap[char] = 1
        else:
            result += 2
            hashmap[char] = 0

    if any(hashmap.values()):
        result += 1

    return result


print(longestPalindrome("abccccdd"))  # 7
