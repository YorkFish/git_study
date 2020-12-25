#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int res = INT_MIN, sum = 0;
        for (int num : nums) {
            if (sum < 0) sum = 0;
            sum += num;
            res = max(res, sum);
        }
        return res;
    }
};

int main() {
    vector<int> nums{1, -2, 3, 10, -4, 7, 2, -5};

    Solution s;
    int ans = s.maxSubArray(nums);
    cout << ans << endl;

    return 0;
}
