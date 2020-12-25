#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int getMaxValue(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();
        vector<vector<int>> f(n + 1, vector<int>(m + 1));
        for (int i = 1; i <= n; i ++ )
            for (int j = 1; j <= m; j ++ )
                f[i][j] = max(f[i - 1][j], f[i][j - 1]) + grid[i - 1][j - 1];
        return f[n][m];
    }
};

int main() {
    vector<vector<int>> grid{
      {2, 3, 1},
      {1, 7, 1},
      {4, 6, 1}
    };

    Solution s;
    int ans = s.getMaxValue(grid);
    cout << ans << endl;

    return 0;
}
