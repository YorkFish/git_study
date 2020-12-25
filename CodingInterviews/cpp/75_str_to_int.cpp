#include <iostream>

using namespace std;

class Solution {
public:
    int strToInt(string str) {
        bool is_negative = false;
        unsigned i = 0;
        long long num = 0;
        while (i < str.size() && str[i] == ' ') i ++ ;
        if (str[i] == '+') i ++ ;
        else if (str[i] == '-') i ++, is_negative = true;
        while (i < str.size() && '0' <= str[i] && str[i] <= '9') {
            num = num * 10 + str[i ++ ] - '0';
            if (INT_MAX < num) break;
        }
        if (is_negative) num *= -1;
        if (INT_MAX < num) num = INT_MAX;
        if (num < INT_MIN) num = INT_MIN;
        return num;
    }
};

int main() {
    string str = "$";

    Solution s;
    int ans = s.strToInt(str);
    cout << ans << endl;

    return 0;
}
