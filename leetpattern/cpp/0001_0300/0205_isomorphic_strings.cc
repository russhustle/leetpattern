#include <cassert>
#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
   public:
    bool isIsomorphic(string s, string t) {
        if (s.size() != t.size()) return false;

        unordered_map<char, char> map_s2t;
        unordered_map<char, char> map_t2s;

        for (size_t i = 0; i < s.size(); i++) {
            char a = s[i];
            char b = t[i];

            if (map_s2t.count(a) && map_s2t[a] != b) return false;
            if (map_t2s.count(b) && map_t2s[b] != a) return false;

            map_s2t[a] = b;
            map_t2s[b] = a;
        }
        return true;
    }
};

int main() {
    Solution sol;
    assert(sol.isIsomorphic("egg", "add") == true);
    return 0;
}