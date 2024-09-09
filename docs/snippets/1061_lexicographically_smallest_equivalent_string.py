# Union Find
def smallestEquivalentString(s1: str, s2: str, baseStr: str) -> str:
    parent = {chr(i): chr(i) for i in range(ord("a"), ord("z") + 1)}

    def find(n):
        p = parent[n]
        while parent[p] != p:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        if p1 != p2:
            if p1 < p2:
                parent[p2] = p1
            else:
                parent[p1] = p2

    for i in range(len(s1)):
        union(s1[i], s2[i])

    result = []
    for c in baseStr:
        result.append(find(c))

    return "".join(result)


s1 = "parker"
s2 = "morris"
baseStr = "parser"
print(smallestEquivalentString(s1, s2, baseStr))  # "makkek"
