#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int longestSubstringWithoutDuplication(string s) {
        unordered_map<char, int> count;
        int res = 0;
        // i <= j
        for (int i = 0, j = 0; j < s.size(); j ++ ) {
            count[s[j]] ++ ;
            while (count[s[j]] > 1) count[s[i ++ ]] -- ;
            res = max(res, j - i + 1);
        }
        return res;
    }
};

int main() {
    string str = "abcabc";

    Solution s;
    int ans = s.longestSubstringWithoutDuplication(str);
    cout << ans << endl;

    return 0;
}
