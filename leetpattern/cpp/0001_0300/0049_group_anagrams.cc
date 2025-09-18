#include <algorithm>
#include <cassert>
#include <ranges>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
   public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;

        for (string& s : strs) {
            string sorted = s;
            ranges::sort(sorted);
            map[sorted].push_back(s);
        }

        vector<vector<string>> res;

        for (auto& kv : map) {
            res.push_back(kv.second);
        }
        return res;
    }
};

int main() {
    Solution solution;
    vector<string> strs = {"eat", "tea", "tan"};
    vector<vector<string>> res = solution.groupAnagrams(strs);
    assert((res == vector<vector<string>>{{"eat", "tea"}, {"tan"}} ||
            res == vector<vector<string>>{{"tan"}, {"eat", "tea"}}));

    return 0;
}
