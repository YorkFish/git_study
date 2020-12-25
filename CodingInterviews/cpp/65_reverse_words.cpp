#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        reverse(s.begin(), s.end());
        for (unsigned i = 0; i < s.size(); i ++ ) {
            unsigned j = i;
            while (j < s.size() && s[j] != ' ') j ++ ;
            reverse(s.begin() + i, s.begin() + j);
            i = j;
        }
        return s;
    }
};

int main() {
    string str = "I am a student.";

    Solution s;
    string ans = s.reverseWords(str);
    cout << ans << endl;

    return 0;
}
