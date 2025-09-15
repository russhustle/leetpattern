#include <cassert>
#include <vector>
using namespace std;

class Solution {
   public:
    vector<int> plusOne(vector<int>& digits) {
        for (int i = digits.size() - 1; i >= 0; i--) {
            digits[i]++;
            if (digits[i] == 10)
                digits[i] = 0;
            else
                return digits;
        }
        digits.insert(digits.begin(), 1);
        return digits;
    }
};

int main() {
    Solution solution;
    vector<int> digits;
    digits = {4, 3, 2, 1};
    assert((solution.plusOne(digits) == vector<int>{4, 3, 2, 2}));
    return 0;
}
