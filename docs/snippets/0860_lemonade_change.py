from typing import List


# Greedy
def lemonadeChange(bills: List[int]) -> bool:
    hashmap = {5: 0, 10: 0, 20: 0}

    for i in bills:
        if i == 5:
            hashmap[5] += 1

        if i == 10:
            if hashmap[5] < 1:
                return False

            hashmap[5] -= 1
            hashmap[10] += 1

        if i == 20:
            if hashmap[5] >= 1 and hashmap[10] >= 1:
                hashmap[5] -= 1
                hashmap[10] -= 1
                hashmap[20] += 1

            elif hashmap[5] >= 3:
                hashmap[5] -= 3
                hashmap[20] += 1

            else:
                return False

    return True


print(lemonadeChange([5, 5, 5, 10, 20]))  # True
