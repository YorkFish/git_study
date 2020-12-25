#include <iostream>

using namespace std;

class Solution {
public:
    string replaceSpaces(string &str) {
        string res;
        for (auto c : str)
            if (c != ' ') res += c;
            else res += "%20";
        return res;
    }
};

int main() {
    string str = "We are happy.";
    Solution s;
    string ans = s.replaceSpaces(str);
    cout << ans << endl;
    
    return 0;
}
