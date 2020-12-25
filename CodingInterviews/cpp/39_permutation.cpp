#include <iostream>
#include <vector>
#include <algorithm>
#include "helper.h"

using namespace std;

class Solution {
public:
    vector<vector<int>> res;
    vector<int> path;

    vector<vector<int>> permutation(vector<int>& nums) {
        path.resize(nums.size());
        dfs(nums, 0, 0, 0);
        return res;
    }
    
    void dfs(vector<int> &nums, int u, int start, int status) {
        if (u == nums.size()) {
            res.push_back(path);
            return;
        }
        if (u == 0 || nums[u] != nums[u - 1]) start = 0;
        for (int i = start; i < nums.size(); i ++ ) {
            if ((1 << i & status) == 0) {
                path[i] = nums[u];
                dfs(nums, u + 1, i + 1, 1 << i | status);
            }
        }
    }
};

int main() {
    vector<int> nums{1, 2, 2, 3};

    Solution s;
    vector<vector<int>> ans = s.permutation(nums);
    print_matrix(ans);

    return 0;
}
