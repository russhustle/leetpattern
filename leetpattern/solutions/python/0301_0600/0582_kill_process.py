from collections import defaultdict, deque
from typing import List


# BFS
def killProcess(pid: List[int], ppid: List[int], kill: int) -> List[int]:
    graph = defaultdict(list)

    for u, v in zip(ppid, pid):
        graph[u].append(v)

    q = deque([kill])
    res = []

    while q:
        cur = q.popleft()
        res.append(cur)
        for nxt in graph[cur]:
            q.append(nxt)

    return res


if __name__ == "__main__":
    pid = [1, 3, 10, 5]
    ppid = [3, 0, 5, 3]
    kill = 5
    assert killProcess(pid, ppid, kill) == [5, 10]
