from collections import Counter
from functools import reduce
from math import gcd
from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            return False
        return reduce(gcd, Counter(deck).values()) >= 2
