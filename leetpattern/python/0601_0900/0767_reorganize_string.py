import heapq
from collections import Counter


def reorganizeString(s: str) -> str:
    if not s:
        return ""

    heap = [(-freq, char) for char, freq in Counter(s).items()]  # max heap
    heapq.heapify(heap)

    result = []
    prev_count, prev_char = 0, ""

    while heap:
        count, char = heapq.heappop(heap)  # pop the most frequent character
        result.append(char)  # append the character to the result

        if prev_count < 0:  # if the previous character still has remaining count
            heapq.heappush(heap, (prev_count, prev_char))

        prev_count = count + 1  # update the current character's remaining count
        prev_char = char  # update the current character

    # check if there is any invalid result
    if len(result) != len(s):
        return ""

    return "".join(result)


print(reorganizeString("aab"))
