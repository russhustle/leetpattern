---
comments: True
---

# Math Others

## Table of Contents

- [ ] [1523. Count Odd Numbers in an Interval Range](https://leetcode.cn/problems/count-odd-numbers-in-an-interval-range/) (Easy)
- [x] [2829. Determine the Minimum Sum of a k-avoiding Array](https://leetcode.cn/problems/determine-the-minimum-sum-of-a-k-avoiding-array/) (Medium)
- [ ] [2579. Count Total Number of Colored Cells](https://leetcode.cn/problems/count-total-number-of-colored-cells/) (Medium)
- [ ] [2834. Find the Minimum Possible Sum of a Beautiful Array](https://leetcode.cn/problems/find-the-minimum-possible-sum-of-a-beautiful-array/) (Medium)
- [ ] [1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K](https://leetcode.cn/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/) (Medium)
- [ ] [319. Bulb Switcher](https://leetcode.cn/problems/bulb-switcher/) (Medium)
- [ ] [1780. Check if Number is a Sum of Powers of Three](https://leetcode.cn/problems/check-if-number-is-a-sum-of-powers-of-three/) (Medium)
- [ ] [3091. Apply Operations to Make Sum of Array Greater Than or Equal to k](https://leetcode.cn/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/) (Medium)
- [ ] [2310. Sum of Numbers With Units Digit K](https://leetcode.cn/problems/sum-of-numbers-with-units-digit-k/) (Medium)
- [ ] [2844. Minimum Operations to Make a Special Number](https://leetcode.cn/problems/minimum-operations-to-make-a-special-number/) (Medium)
- [ ] [2541. Minimum Operations to Make Array Equal II](https://leetcode.cn/problems/minimum-operations-to-make-array-equal-ii/) (Medium)
- [ ] [2195. Append K Integers With Minimal Sum](https://leetcode.cn/problems/append-k-integers-with-minimal-sum/) (Medium)
- [ ] [2457. Minimum Addition to Make Integer Beautiful](https://leetcode.cn/problems/minimum-addition-to-make-integer-beautiful/) (Medium)
- [ ] [1017. Convert to Base -2](https://leetcode.cn/problems/convert-to-base-2/) (Medium)
- [ ] [1954. Minimum Garden Perimeter to Collect Enough Apples](https://leetcode.cn/problems/minimum-garden-perimeter-to-collect-enough-apples/) (Medium)
- [ ] [1073. Adding Two Negabinary Numbers](https://leetcode.cn/problems/adding-two-negabinary-numbers/) (Medium)
- [ ] [1823. Find the Winner of the Circular Game](https://leetcode.cn/problems/find-the-winner-of-the-circular-game/) (Medium)
- [x] [166. Fraction to Recurring Decimal](https://leetcode.cn/problems/fraction-to-recurring-decimal/) (Medium)
- [ ] [3012. Minimize Length of Array Using Operations](https://leetcode.cn/problems/minimize-length-of-array-using-operations/) (Medium)
- [ ] [483. Smallest Good Base](https://leetcode.cn/problems/smallest-good-base/) (Hard)
- [ ] [972. Equal Rational Numbers](https://leetcode.cn/problems/equal-rational-numbers/) (Hard)
- [ ] [1862. Sum of Floored Pairs](https://leetcode.cn/problems/sum-of-floored-pairs/) (Hard)
- [ ] [1739. Building Boxes](https://leetcode.cn/problems/building-boxes/) (Hard)
- [ ] [2443. Sum of Number and Its Reverse](https://leetcode.cn/problems/sum-of-number-and-its-reverse/) (Medium)
- [ ] [1806. Minimum Number of Operations to Reinitialize a Permutation](https://leetcode.cn/problems/minimum-number-of-operations-to-reinitialize-a-permutation/) (Medium)
- [ ] [458. Poor Pigs](https://leetcode.cn/problems/poor-pigs/) (Hard)
- [ ] [60. Permutation Sequence](https://leetcode.cn/problems/permutation-sequence/) (Hard)
- [ ] [2117. Abbreviating the Product of a Range](https://leetcode.cn/problems/abbreviating-the-product-of-a-range/) (Hard)
- [ ] [660. Remove 9](https://leetcode.cn/problems/remove-9/) (Hard) 👑
- [ ] [2979. Most Expensive Item That Can Not Be Bought](https://leetcode.cn/problems/most-expensive-item-that-can-not-be-bought/) (Medium) 👑
- [ ] [2647. Color the Triangle Red](https://leetcode.cn/problems/color-the-triangle-red/) (Hard) 👑

## 1523. Count Odd Numbers in an Interval Range

-   [LeetCode](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/) | [LeetCode CH](https://leetcode.cn/problems/count-odd-numbers-in-an-interval-range/) (Easy)

-   Tags: math

## 2829. Determine the Minimum Sum of a k-avoiding Array

-   [LeetCode](https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/) | [LeetCode CH](https://leetcode.cn/problems/determine-the-minimum-sum-of-a-k-avoiding-array/) (Medium)

-   Tags: math, greedy

```python title="2829. Determine the Minimum Sum of a k-avoiding Array - Python Solution"
def minimumSum(n: int, k: int) -> int:
    m = min(k // 2, n)
    return (m * (m + 1) + (k * 2 + n - m - 1) * (n - m)) // 2


if __name__ == "__main__":
    n = 5
    k = 4
    print(minimumSum(n, k))  # 18

```

## 2579. Count Total Number of Colored Cells

-   [LeetCode](https://leetcode.com/problems/count-total-number-of-colored-cells/) | [LeetCode CH](https://leetcode.cn/problems/count-total-number-of-colored-cells/) (Medium)

-   Tags: math

## 2834. Find the Minimum Possible Sum of a Beautiful Array

-   [LeetCode](https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/) | [LeetCode CH](https://leetcode.cn/problems/find-the-minimum-possible-sum-of-a-beautiful-array/) (Medium)

-   Tags: math, greedy

## 1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K

-   [LeetCode](https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/) | [LeetCode CH](https://leetcode.cn/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/) (Medium)

-   Tags: math, greedy

## 319. Bulb Switcher

-   [LeetCode](https://leetcode.com/problems/bulb-switcher/) | [LeetCode CH](https://leetcode.cn/problems/bulb-switcher/) (Medium)

-   Tags: math, brainteaser

## 1780. Check if Number is a Sum of Powers of Three

-   [LeetCode](https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/) | [LeetCode CH](https://leetcode.cn/problems/check-if-number-is-a-sum-of-powers-of-three/) (Medium)

-   Tags: math

## 3091. Apply Operations to Make Sum of Array Greater Than or Equal to k

-   [LeetCode](https://leetcode.com/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/) | [LeetCode CH](https://leetcode.cn/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/) (Medium)

-   Tags: math, greedy, enumeration

## 2310. Sum of Numbers With Units Digit K

-   [LeetCode](https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-numbers-with-units-digit-k/) (Medium)

-   Tags: math, dynamic programming, greedy, enumeration

## 2844. Minimum Operations to Make a Special Number

-   [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-a-special-number/) | [LeetCode CH](https://leetcode.cn/problems/minimum-operations-to-make-a-special-number/) (Medium)

-   Tags: math, string, greedy, enumeration

## 2541. Minimum Operations to Make Array Equal II

-   [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/) | [LeetCode CH](https://leetcode.cn/problems/minimum-operations-to-make-array-equal-ii/) (Medium)

-   Tags: array, math, greedy

## 2195. Append K Integers With Minimal Sum

-   [LeetCode](https://leetcode.com/problems/append-k-integers-with-minimal-sum/) | [LeetCode CH](https://leetcode.cn/problems/append-k-integers-with-minimal-sum/) (Medium)

-   Tags: array, math, greedy, sorting

## 2457. Minimum Addition to Make Integer Beautiful

-   [LeetCode](https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/) | [LeetCode CH](https://leetcode.cn/problems/minimum-addition-to-make-integer-beautiful/) (Medium)

-   Tags: math, greedy

## 1017. Convert to Base -2

-   [LeetCode](https://leetcode.com/problems/convert-to-base-2/) | [LeetCode CH](https://leetcode.cn/problems/convert-to-base-2/) (Medium)

-   Tags: math

## 1954. Minimum Garden Perimeter to Collect Enough Apples

-   [LeetCode](https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/) | [LeetCode CH](https://leetcode.cn/problems/minimum-garden-perimeter-to-collect-enough-apples/) (Medium)

-   Tags: math, binary search

## 1073. Adding Two Negabinary Numbers

-   [LeetCode](https://leetcode.com/problems/adding-two-negabinary-numbers/) | [LeetCode CH](https://leetcode.cn/problems/adding-two-negabinary-numbers/) (Medium)

-   Tags: array, math

## 1823. Find the Winner of the Circular Game

-   [LeetCode](https://leetcode.com/problems/find-the-winner-of-the-circular-game/) | [LeetCode CH](https://leetcode.cn/problems/find-the-winner-of-the-circular-game/) (Medium)

-   Tags: array, math, recursion, queue, simulation

## 166. Fraction to Recurring Decimal

-   [LeetCode](https://leetcode.com/problems/fraction-to-recurring-decimal/) | [LeetCode CH](https://leetcode.cn/problems/fraction-to-recurring-decimal/) (Medium)

-   Tags: hash table, math, string

```python title="166. Fraction to Recurring Decimal - Python Solution"
# Math
def fractionToDecimal(numerator: int, denominator: int) -> str:
    if numerator == 0:
        return "0"

    res = []

    if (numerator < 0) ^ (denominator < 0):
        res.append("-")

    numerator, denominator = abs(numerator), abs(denominator)

    # Integer part
    res.append(str(numerator // denominator))
    remainder = numerator % denominator

    if remainder == 0:
        return "".join(res)

    res.append(".")

    # Dictionary to store remainders and their corresponding indices
    remainder_map = {}

    while remainder != 0:
        if remainder in remainder_map:
            res.insert(remainder_map[remainder], "(")
            res.append(")")
            break

        remainder_map[remainder] = len(res)
        remainder *= 10
        res.append(str(remainder // denominator))
        remainder %= denominator

    return "".join(res)


numerator = 4
denominator = 333
print(fractionToDecimal(numerator, denominator))  # 0.(012)

```

## 3012. Minimize Length of Array Using Operations

-   [LeetCode](https://leetcode.com/problems/minimize-length-of-array-using-operations/) | [LeetCode CH](https://leetcode.cn/problems/minimize-length-of-array-using-operations/) (Medium)

-   Tags: array, math, greedy, number theory

## 483. Smallest Good Base

-   [LeetCode](https://leetcode.com/problems/smallest-good-base/) | [LeetCode CH](https://leetcode.cn/problems/smallest-good-base/) (Hard)

-   Tags: math, binary search

## 972. Equal Rational Numbers

-   [LeetCode](https://leetcode.com/problems/equal-rational-numbers/) | [LeetCode CH](https://leetcode.cn/problems/equal-rational-numbers/) (Hard)

-   Tags: math, string

## 1862. Sum of Floored Pairs

-   [LeetCode](https://leetcode.com/problems/sum-of-floored-pairs/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-floored-pairs/) (Hard)

-   Tags: array, math, binary search, prefix sum

## 1739. Building Boxes

-   [LeetCode](https://leetcode.com/problems/building-boxes/) | [LeetCode CH](https://leetcode.cn/problems/building-boxes/) (Hard)

-   Tags: math, binary search, greedy

## 2443. Sum of Number and Its Reverse

-   [LeetCode](https://leetcode.com/problems/sum-of-number-and-its-reverse/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-number-and-its-reverse/) (Medium)

-   Tags: math, enumeration

## 1806. Minimum Number of Operations to Reinitialize a Permutation

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-operations-to-reinitialize-a-permutation/) (Medium)

-   Tags: array, math, simulation

## 458. Poor Pigs

-   [LeetCode](https://leetcode.com/problems/poor-pigs/) | [LeetCode CH](https://leetcode.cn/problems/poor-pigs/) (Hard)

-   Tags: math, dynamic programming, combinatorics

## 60. Permutation Sequence

-   [LeetCode](https://leetcode.com/problems/permutation-sequence/) | [LeetCode CH](https://leetcode.cn/problems/permutation-sequence/) (Hard)

-   Tags: math, recursion

## 2117. Abbreviating the Product of a Range

-   [LeetCode](https://leetcode.com/problems/abbreviating-the-product-of-a-range/) | [LeetCode CH](https://leetcode.cn/problems/abbreviating-the-product-of-a-range/) (Hard)

-   Tags: math

## 660. Remove 9

-   [LeetCode](https://leetcode.com/problems/remove-9/) | [LeetCode CH](https://leetcode.cn/problems/remove-9/) (Hard)

-   Tags: math

## 2979. Most Expensive Item That Can Not Be Bought

-   [LeetCode](https://leetcode.com/problems/most-expensive-item-that-can-not-be-bought/) | [LeetCode CH](https://leetcode.cn/problems/most-expensive-item-that-can-not-be-bought/) (Medium)

-   Tags: math, dynamic programming, number theory

## 2647. Color the Triangle Red

-   [LeetCode](https://leetcode.com/problems/color-the-triangle-red/) | [LeetCode CH](https://leetcode.cn/problems/color-the-triangle-red/) (Hard)

-   Tags: array, math
