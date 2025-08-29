#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;

int lengthOfLongestSubstring(string s) {
    int n = s.length();
    int res = 0;
    int left = 0;
    unordered_set<char> window;

    for (int right = 0; right < n; right++) {
        char ch = s[right];

        while (window.find(ch) != window.end()) {
            window.erase(s[left]);
            left++;
        }

        window.insert(ch);
        res = max(res, right - left + 1);
    }
    return (int)res;
}

int main() {
    string s = "abcabcbb";
    cout << lengthOfLongestSubstring(s) << endl;  // 3
    s = "bbbbb";
    cout << lengthOfLongestSubstring(s) << endl;  // 1
    s = "pwwkew";
    cout << lengthOfLongestSubstring(s) << endl;  // 3
    return 0;
}
