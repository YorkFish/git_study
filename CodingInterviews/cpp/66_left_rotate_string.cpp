#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    string leftRotateString(string str, int n) {
        reverse(str.begin(), str.begin() + n);  // [begin, n)
        reverse(str.begin() + n, str.end());
        reverse(str.begin(), str.end());
        return str;
    }
};

int main() {
    string str = "abcdefg";
    int n = 2;

    Solution s;
    string ans = s.leftRotateString(str, n);
    cout << ans << endl;

    return 0;
}
