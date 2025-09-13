#include <cassert>
#include <iostream>
using namespace std;

int climbStairs(int n) {
    if (n <= 2) return n;
    int f1 = 1, f2 = 2;
    int res;

    int i = 3;
    while (i <= n) {
        res = f1 + f2;
        f1 = f2;
        f2 = res;
        i++;
    }
    return res;
}

int main() {
    assert(climbStairs(2) == 2);
    assert(climbStairs(5) == 8);
    assert(climbStairs(10) == 89);
    return 0;
}
