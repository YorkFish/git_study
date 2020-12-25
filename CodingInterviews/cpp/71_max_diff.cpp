#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxDiff(vector<int>& nums) {
        if (nums.empty()) return 0;
        int res = 0;
        for (int i = 1, minv = nums[0]; i < nums.size(); i ++ ) {
            res = max(res, nums[i] - minv);
            minv = min(minv, nums[i]);
        }
        return res;
    }
};

int main() {
    vector<int> nums{9, 11, 8, 5, 7, 12, 16, 14};

    Solution s;
    int ans = s.maxDiff(nums);
    cout << ans << endl;

    return 0;
}
