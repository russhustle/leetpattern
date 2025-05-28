#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
   public:
    string stringShift(string s, vector<vector<int>>& shift) {
        int total_shift = 0;
        for (const auto& op : shift) {
            if (op[0] == 0) {
                total_shift -= op[1];
            } else {
                total_shift += op[1];
            }
        }

        int n = s.length();
        total_shift =
            ((total_shift % n) + n) % n;  // Handle negative shift properly

        if (total_shift == 0) {
            return s;
        }

        return s.substr(n - total_shift) + s.substr(0, n - total_shift);
    }
};

int main() {
    Solution solution;

    string s1 = "abc";
    vector<vector<int>> shift1 = {{0, 1}, {1, 2}};
    cout << "Input: s = \"abc\", shift = [[0,1],[1,2]]" << endl;
    cout << "Output: " << solution.stringShift(s1, shift1) << endl;

    string s2 = "abcdefg";
    vector<vector<int>> shift2 = {{1, 1}, {1, 1}, {0, 2}, {1, 3}};
    cout << "Input: s = \"abcdefg\", shift = [[1,1],[1,1],[0,2],[1,3]]" << endl;
    cout << "Output: " << solution.stringShift(s2, shift2) << endl;

    return 0;
}
