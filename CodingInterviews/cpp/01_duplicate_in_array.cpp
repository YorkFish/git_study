#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int duplicateInArray(vector<int>& nums) {
        int n = nums.size();
        for (int x : nums) if (x < 0 || x > n - 1) return -1;
        for (int i = 0; i < n; i ++ ) {
            while (i != nums[i] && nums[i] != nums[nums[i]]) swap(nums[i], nums[nums[i]]);
            if (i != nums[i] && nums[i] == nums[nums[i]]) return nums[i];
        }
        return -1;
    }
};

int main() {
    vector<int> nums{3, 1, -10, 1, 1, 4, 3, 10, 1, 1};
    Solution s;
    int ans = s.duplicateInArray(nums);
    cout << ans << endl;
    
    return 0;
}
