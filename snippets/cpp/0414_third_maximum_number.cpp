#include <vector>
#include <iostream>
#include <limits>

using namespace std;

int thirdMax(vector<int> &nums)
{
    long first = numeric_limits<long>::min(), second = numeric_limits<long>::min(), third = numeric_limits<long>::min();

    for (int num : nums)
    {
        if (num == first || num == second || num == third)
        {
            continue;
        }

        if (num > first)
        {
            third = second;
            second = first;
            first = num;
        }
        else if (num > second)
        {
            third = second;
            second = num;
        }
        else if (num > third)
        {
            third = num;
        }
    }

    return third == numeric_limits<long>::min() ? first : third;
}

int main()
{
    vector<int> nums = {3, 2, 1, 5, 6, 4};
    printf("%d\n", thirdMax(nums)); // 4
}
