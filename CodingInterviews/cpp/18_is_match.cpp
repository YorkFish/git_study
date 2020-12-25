#include <iostream>
#include <vector>

using namespace std;

/**
状态表示：f[i][j] 表示 s[i:] == p[j:]
状态转移：
    1. p[j] != '*' && p[j] != '.', f[i][j] = s[i] == p[j] && f[i + 1][j + 1]
    2. p[j] == '.', f[i][j] = f[i + 1][j + 1]
    3. p[j + 1] == '*', f[i][j] = f[i][j + 2] || (s[i] == p[j] && f[i + 1][j])
*/
class Solution {
public:
    int n, m;
    vector<vector<int>> f;

    bool isMatch(string s, string p) {
        n = s.size(), m = p.size();
        f = vector<vector<int>>(n + 1, vector<int>(m + 1, -1));
        f[n][m] = 1;
        return dp(0, 0, s, p);
    }

    int dp(int x, int y, string &s, string &p)
    {
        if (f[x][y] != -1) return f[x][y];
        if (y == m) {
            f[x][y] = x == n;
            return f[x][y];
        }

        bool first_match = x < n && (s[x] == p[y] || p[y] == '.');
        if (y + 1 < m && p[y + 1] == '*')
            f[x][y] = dp(x, y + 2, s, p) || (first_match && dp(x + 1, y, s, p));
        else
            f[x][y] = first_match && dp(x + 1, y + 1, s, p);
        return f[x][y];
    }
};

int main() {
    string s = "aaa", p = "b*";
    Solution sol;
    if (sol.isMatch(s, p)) cout << s << " match " << p << endl;
    else cout << s << " not match " << p << endl;

    return 0;
}
