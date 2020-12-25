#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> findNumsAppearOnce(vector<int>& nums) {
        int all_xor = 0;
        for (int num : nums) all_xor ^= num;
        int low_bit = -all_xor & all_xor;
        int first = 0;
        for (int num : nums) if (num & low_bit) first ^= num;
        return vector<int> {first, all_xor ^ first};
    }
};

int main() {
    vector<int> nums{1, 2, 3, 3, 4, 4};

    Solution s;
    vector<int> ans = s.findNumsAppearOnce(nums);
    cout << ans[0] << ' ' << ans[1] << endl;

    return 0;
}
