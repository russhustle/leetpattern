import heapq
from collections import Counter
from typing import List


class WordFrequency:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        # If the frequency is different
        if self.freq != other.freq:
            # The word with the lower frequency comes first
            return self.freq < other.freq
        else:
            # The word with the lower alphabetical order comes first
            return self.word > other.word


def topKFrequent(words: List[str], k: int) -> List[str]:
    heap = []

    for word, freq in Counter(words).items():
        heapq.heappush(heap, WordFrequency(word, freq))

        if len(heap) > k:
            heapq.heappop(heap)

    heap.sort(reverse=True)
    return [x.word for x in heap]


words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print(topKFrequent(words, k))  # ["i", "love"]
