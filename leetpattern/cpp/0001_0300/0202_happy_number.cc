#include <cassert>
#include <unordered_set>
using namespace std;

class Solution {
   public:
    int getNext(int n) {
        int res = 0;
        while (n) {
            int mod = n % 10;
            res += mod * mod;
            n /= 10;
        }
        return res;
    }

    bool isHappy(int n) {
        unordered_set<int> seen;
        while (n != 1) {
            n = getNext(n);
            if (seen.find(n) != seen.end()) return false;
            seen.insert(n);
        }
        return true;
    }
};

int main() {
    Solution s;
    assert(s.isHappy(19) == true);
    assert(s.isHappy(2) == false);
    return 0;
}
