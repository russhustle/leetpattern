#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
   public:
    bool confusingNumber(int n) {
        static const unordered_map<char, char> rotationMap = {
            {'0', '0'}, {'1', '1'}, {'6', '9'}, {'8', '8'}, {'9', '6'}};

        string numStr = to_string(n);
        string rotated;
        rotated.reserve(numStr.size());

        for (int i = numStr.size() - 1; i >= 0; --i) {
            char currentDigit = numStr[i];

            auto it = rotationMap.find(currentDigit);
            if (it == rotationMap.end()) {
                return false;
            }

            rotated.push_back(it->second);
        }

        return rotated != numStr;
    }
};

int main() {
    Solution sol;
    cout << boolalpha;  // Print boolean values as true/false
    cout << sol.confusingNumber(6) << endl;    // true
    cout << sol.confusingNumber(89) << endl;   // true
    cout << sol.confusingNumber(11) << endl;   // false
    cout << sol.confusingNumber(25) << endl;   // false
    cout << sol.confusingNumber(916) << endl;  // true
    cout << sol.confusingNumber(101) << endl;  // false

    return 0;
}
