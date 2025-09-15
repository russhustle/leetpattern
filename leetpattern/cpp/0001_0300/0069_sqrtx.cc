#include <cassert>
using namespace std;

class Solution {
   public:
    int mySqrt(int x) {
        if (x < 2) return x;
        int left = 0, right = x / 2;
        int mid = 0;

        while (left <= right) {
            mid = left + (right - left) / 2;
            long long a = 1LL * mid * mid;
            long long b = 1LL * (mid + 1) * (mid + 1);

            if (a <= x && x < b) {
                return mid;
            } else if (a < x)
                left = mid + 1;
            else
                right = mid - 1;
        }
        return right;
    }
};

int main() {
    Solution solution;
    assert(solution.mySqrt(4) == 2);
    assert(solution.mySqrt(8) == 2);
    assert(solution.mySqrt(1999) == 44);
    return 0;
}