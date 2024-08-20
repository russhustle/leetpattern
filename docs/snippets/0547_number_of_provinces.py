from typing import List


def findCircleNum(isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    par = list(range(n))
    rank = [1] * n

    def find(p):
        if par[p] != p:
            par[p] = find(par[p])
        return par[p]

    def union(n1, n2):
        p1 = find(n1)
        p2 = find(n2)

        if p1 != p2:
            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p1] < rank[p2]:
                par[p1] = p2
            else:
                par[p2] = p1
                rank[p1] += 1

    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j] == 1:
                union(i, j)

    provinces = len(set(find(i) for i in range(n)))

    return provinces


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(findCircleNum(isConnected))  # 2
