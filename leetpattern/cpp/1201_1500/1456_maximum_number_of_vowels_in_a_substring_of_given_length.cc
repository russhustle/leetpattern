#include <cassert>
#include <string>
#include <unordered_set>
using namespace std;

class Solution {
   public:
    int maxVowels(string s, int k) {
        int n = s.size();
        int res = 0, cnt = 0;
        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};

        for (int right = 0; right < n; right++) {
            if (vowels.count(s[right])) cnt++;

            int left = right - k + 1;
            if (left < 0) continue;

            res = max(res, cnt);
            if (vowels.count(s[left])) cnt--;
        }
        return res;
    }
};

int main() {
    Solution solution;
    assert(solution.maxVowels("abciiidef", 3) == 3);
    assert(solution.maxVowels("aeiou", 2) == 2);
    return 0;
}
