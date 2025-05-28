---
comments: True
---

# Heap Rearrange Elements

## Table of Contents

- [ ] [984. String Without AAA or BBB](https://leetcode.cn/problems/string-without-aaa-or-bbb/) (Medium)
- [x] [767. Reorganize String](https://leetcode.cn/problems/reorganize-string/) (Medium)
- [ ] [1054. Distant Barcodes](https://leetcode.cn/problems/distant-barcodes/) (Medium)
- [ ] [1953. Maximum Number of Weeks for Which You Can Work](https://leetcode.cn/problems/maximum-number-of-weeks-for-which-you-can-work/) (Medium)
- [ ] [1405. Longest Happy String](https://leetcode.cn/problems/longest-happy-string/) (Medium)
- [ ] [3081. Replace Question Marks in String to Minimize Its Value](https://leetcode.cn/problems/replace-question-marks-in-string-to-minimize-its-value/) (Medium)
- [x] [621. Task Scheduler](https://leetcode.cn/problems/task-scheduler/) (Medium)
- [ ] [358. Rearrange String k Distance Apart](https://leetcode.cn/problems/rearrange-string-k-distance-apart/) (Hard) 👑

## 984. String Without AAA or BBB

-   [LeetCode](https://leetcode.com/problems/string-without-aaa-or-bbb/) | [LeetCode CH](https://leetcode.cn/problems/string-without-aaa-or-bbb/) (Medium)

-   Tags: string, greedy
## 767. Reorganize String

-   [LeetCode](https://leetcode.com/problems/reorganize-string/) | [LeetCode CH](https://leetcode.cn/problems/reorganize-string/) (Medium)

-   Tags: hash table, string, greedy, sorting, heap priority queue, counting

```python title="767. Reorganize String - Python Solution"
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

        if (
            prev_count < 0
        ):  # if the previous character still has remaining count
            heapq.heappush(heap, (prev_count, prev_char))

        prev_count = (
            count + 1
        )  # update the current character's remaining count
        prev_char = char  # update the current character

    # check if there is any invalid result
    if len(result) != len(s):
        return ""

    return "".join(result)


print(reorganizeString("aab"))

```

## 1054. Distant Barcodes

-   [LeetCode](https://leetcode.com/problems/distant-barcodes/) | [LeetCode CH](https://leetcode.cn/problems/distant-barcodes/) (Medium)

-   Tags: array, hash table, greedy, sorting, heap priority queue, counting
## 1953. Maximum Number of Weeks for Which You Can Work

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-weeks-for-which-you-can-work/) (Medium)

-   Tags: array, greedy
## 1405. Longest Happy String

-   [LeetCode](https://leetcode.com/problems/longest-happy-string/) | [LeetCode CH](https://leetcode.cn/problems/longest-happy-string/) (Medium)

-   Tags: string, greedy, heap priority queue
## 3081. Replace Question Marks in String to Minimize Its Value

-   [LeetCode](https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/) | [LeetCode CH](https://leetcode.cn/problems/replace-question-marks-in-string-to-minimize-its-value/) (Medium)

-   Tags: hash table, string, greedy, sorting, heap priority queue, counting
## 621. Task Scheduler

-   [LeetCode](https://leetcode.com/problems/task-scheduler/) | [LeetCode CH](https://leetcode.cn/problems/task-scheduler/) (Medium)

-   Tags: array, hash table, greedy, sorting, heap priority queue, counting

```python title="621. Task Scheduler - Python Solution"
import heapq
from collections import Counter, deque
from typing import List


# Heap
def leastInterval1(tasks: List[str], n: int) -> int:
    count = Counter(tasks)
    heap = [-c for c in count.values()]
    heapq.heapify(heap)

    time = 0

    q = deque()

    while heap or q:
        time += 1

        if heap:
            cnt = 1 + heapq.heappop(heap)
            if cnt:
                q.append((cnt, time + n))

        if q and q[0][1] == time:
            heapq.heappush(heap, q.popleft()[0])

    return time


def leastInterval2(tasks: List[str], n: int) -> int:
    freq = Counter(tasks)

    maxExec = max(freq.values())
    maxCount = sum(1 for v in freq.values() if v == maxExec)

    return max((maxExec - 1) * (n + 1) + maxCount, len(tasks))


tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(leastInterval1(tasks, n))  # 8
print(leastInterval2(tasks, n))  # 8

```

## 358. Rearrange String k Distance Apart

-   [LeetCode](https://leetcode.com/problems/rearrange-string-k-distance-apart/) | [LeetCode CH](https://leetcode.cn/problems/rearrange-string-k-distance-apart/) (Hard)

-   Tags: hash table, string, greedy, sorting, heap priority queue, counting
