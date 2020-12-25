#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    char firstNotRepeatingChar(string s) {
        unordered_map<char, int> count;
        for (char c : s) count[c] ++ ;
        for (char c : s) if (count[c] == 1) return c;
        return '#';
    }
};

int main() {
    string str = "abaccdeff";

    Solution s;
    char ans = s.firstNotRepeatingChar(str);
    cout << ans << endl;

    return 0;
}
