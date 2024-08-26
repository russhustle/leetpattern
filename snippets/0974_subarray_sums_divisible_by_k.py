from typing import List


def subarraysDivByK_1(nums: List[int], k: int) -> int:
    mods = {0: 1}
    prefixSum, result = 0, 0

    for num in nums:
        prefixSum += num
        mod = prefixSum % k

        if mod < 0:
            mod += k

        if mod in mods:
            result += mods[mod]

        if mod in mods:
            mods[mod] += 1
        else:
            mods[mod] = 1

    return result


def subarraysDivByK_2(nums: List[int], k: int) -> int:
    mods = {0: 1}
    prefixSum, result = 0, 0

    for num in nums:
        prefixSum += num
        mod = prefixSum % k
        result += mods.get(mod, 0)
        mods[mod] = mods.get(mod, 0) + 1

    return result


nums = [4, 5, 0, -2, -3, 1]
k = 5
print(subarraysDivByK_1(nums, k))  # 7
print(subarraysDivByK_2(nums, k))  # 7
