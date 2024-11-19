import heapq

heap = []

# Push
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 4)
heapq.heappush(heap, 2)
print(heap)  # [1, 2, 4, 3]

# Pop
heapq.heappop(heap)
print(heap)  # [2, 3, 4]
heapq.heappop(heap)
print(heap)  # [3, 4]

# Peek
print(heap[0])  # 3
