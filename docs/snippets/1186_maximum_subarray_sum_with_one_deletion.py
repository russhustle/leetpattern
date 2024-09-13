from typing import List


# DP - Kadane
def maximumSum(arr: List[int]) -> int:
    dp0 = arr[0]
    dp1 = 0
    maxSum = dp0

    for i in range(1, len(arr)):
        dp1 = max(dp1 + arr[i], dp0)  # delete previous element or not
        dp0 = max(dp0, 0) + arr[i]  # delete current element or not
        maxSum = max(maxSum, dp0, dp1)  # update result

    return maxSum


arr = [1, -2, 0, 3]
print(maximumSum(arr))  # 4
