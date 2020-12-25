#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int findNumberAppearingOnce(vector<int>& nums) {
        int ones = 0, twos = 0;
        for (int num : nums) {
            ones = (ones ^ num) & ~twos;
            twos = (twos ^ num) & ~ones;
        }
        return ones;
    }
};

int main() {
    vector<int> nums{1, 1, 1, 2, 2, 2, 3, 4, 4, 4};

    Solution s;
    int ans = s.findNumberAppearingOnce(nums);
    cout << ans << endl;

    return 0;
}
