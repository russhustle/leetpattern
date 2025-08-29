#include <iostream>
#include <string>
using namespace std;

// Valid Parentheses Strings
bool canBeValid(string s, string locked) {
    if (s.length() % 2 != 0) {
        return false;
    }

    int mx = 0, mn = 0;
    for (size_t i = 0; i < s.length(); ++i) {
        char ch = s[i];
        char lock = locked[i];

        if (lock == '1') {
            int d = (ch == '(') ? 1 : -1;
            mx += d;
            if (mx < 0) {
                return false;
            }
            mn += d;
        } else {
            mx += 1;
            mn -= 1;
        }

        if (mn < 0) {
            mn = 1;
        }
    }

    return mn == 0;
}

int main() {
    string s = "))()))";
    string locked = "010100";
    cout << (canBeValid(s, locked) ? "true" : "false") << endl;  // true
    return 0;
}
