#include <iostream>
#include <vector>
#include "helper.h"

using namespace std;

class Solution {
public:
    vector<vector<int> > findContinuousSequence(int sum) {
        vector<vector<int>> res;
        int stop = sum / 2 + 1;
        // i <= j
        for (int i = 1, j = 1, s = 1; i <= stop; i ++ ) {
            while (s < sum) s += ++ j;
            if (s == sum && i < j) {
                vector<int> line;
                for (int k = i; k <= j; k ++ ) line.push_back(k);
                res.push_back(line);
            }
            s -= i;
        }
        return res;
    }
};

int main() {
    int sum = 15;

    Solution s;
    vector<vector<int>> ans = s.findContinuousSequence(sum);
    print_matrix(ans);

    return 0;
}
