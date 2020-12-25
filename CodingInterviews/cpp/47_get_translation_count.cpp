#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int getTranslationCount(string s) {
        int n = s.size();
        vector<int> f(n + 1);
        f[0] = 1;
        for (int i = 1; i <= n; i ++ ) {
            f[i] = f[i - 1];
            int t = (s[i - 2] - '0') * 10 + s[i - 1] - '0';
            if (10 <= t && t <= 25) f[i] += f[i - 2];
        }
        return f[n];
    }
};

int main() {
    string str = "12258";

    Solution s;
    int ans = s.getTranslationCount(str);
    cout << ans << endl;

    return 0;
}
