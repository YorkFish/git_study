#include <iostream>
#include <vector>
#include "helper.h"

using namespace std;

class Solution {
public:
    vector<int> numberOfDice(int n) {
        int len = 6 * n + 1;
        vector<vector<int>> f(n + 1, vector<int>(len));
        f[0][0] = 1;
        for (int i = 1; i <= n; i ++ )
            for (int j = 1; j < len; j ++ )
                for (int k = 1; k <= min(j, 6); k ++ )
                    f[i][j] += f[i - 1][j - k];
        vector<int> res;
        for (int i = n; i < len; i ++ ) res.push_back(f[n][i]);
        return res;
    }
};

int main() {
    int n = 2;

    Solution s;
    vector<int> ans = s.numberOfDice(n);
    print_array(ans);

    return 0;
}
