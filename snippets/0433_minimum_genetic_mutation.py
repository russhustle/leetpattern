from collections import deque
from typing import List


# BFS
def minMutation(startGene: str, endGene: str, bank: List[str]) -> int:
    if endGene not in bank:
        return -1

    bank = set(bank)
    q = deque([(startGene, 0)])

    while q:
        gene, step = q.popleft()
        if gene == endGene:
            return step

        for i in range(8):
            for c in "ACGT":
                if gene[i] == c:
                    continue
                newGene = gene[:i] + c + gene[i + 1 :]
                if newGene in bank:
                    bank.remove(newGene)
                    q.append((newGene, step + 1))
    return -1


startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
print(minMutation(startGene, endGene, bank))  # 2
