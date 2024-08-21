from collections import Counter


# 1. Hashmap
def isAnagramHash(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    hashmap = dict()

    for i in s:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1

    for j in t:
        if j in hashmap:
            hashmap[j] -= 1
        else:
            return False

    for count in hashmap.values():
        if count != 0:
            return False

    return True


# 2. Array
def isAnagramArray(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    record = [0 for _ in range(26)]

    for i in s:
        record[ord(i) - ord("a")] += 1

    for j in t:
        record[ord(j) - ord("a")] -= 1

    for i in record:
        if i != 0:
            return False

    return True


# 3. Counter
def isAnagramCounter(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


s = "anagram"
t = "nagaram"
print(isAnagramHash(s, t))  # True
print(isAnagramArray(s, t))  # True
print(isAnagramCounter(s, t))  # True
