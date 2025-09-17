#include <cassert>
#include <string>
#include <vector>
using namespace std;

class Solution {
   public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;

        vector<int> count(26, 0);

        for (char ch : s) count[ch - 'a']++;
        for (char ch : t) count[ch - 'a']--;
        for (int c : count) {
            if (c != 0) return false;
        }

        return true;
    }
};

int main() {
    Solution solution;
    assert(solution.isAnagram("anagram", "nagaram") == true);
    assert(solution.isAnagram("rat", "car") == false);
    assert(solution.isAnagram("a", "ab") == false);
    assert(solution.isAnagram("a", "a") == true);
    return 0;
}