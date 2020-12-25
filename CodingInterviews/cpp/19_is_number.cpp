#include <iostream>

using namespace std;

class Solution {
public:
    bool isNumber(string s) {
        int i = 0, j = s.size() - 1;
        while (i < j && s[i] == ' ') i ++ ;
        while (i < j && s[j] == ' ') j -- ;
        if (j < i) return false;

        s = s.substr(i, j - i + 1);
        if (s[0] == '-' || s[0] == '+') s = s.substr(1);
        if (s.empty()) return false;
        if (s.size() == 1 && (s[0] < '0' || s[0] > '9')) return false;

        int dot = 0, e = 0, symbol = 0;
        for (i = 0; i < s.size(); i ++ ) {
            if (s[i] >= '0' && s[i] <= '9') continue;
            if (s[i] == '.') {
                dot ++ ;
                if (dot > 1 || e) return false;
            }
            else if (s[i] == 'e' || s[i] == 'E') {
                e ++ ;
                if (i == 0 || i == s.size() - 1 || e > 1) return false;
                if (i == 1 && s[0] == '.') return false;
            }
            else if (s[i] == '-' || s[i] == '+') {
                symbol ++ ;
                if (e == 0 || symbol > 1 || i == s.size() - 1) return false;
            }
            else return false;
        }
        return true;
    }
};

int main() {
    string s = "0";
    Solution sol;
    if (sol.isNumber(s)) cout << "true" << endl;
    else cout << "false" << endl;

    return 0;
}
