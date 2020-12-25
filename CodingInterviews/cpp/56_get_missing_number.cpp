#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int getMissingNumber(vector<int>& nums) {
        int left = 0, right = nums.size();
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (mid == nums[mid]) left = mid + 1;
            else right = mid;
        }
        return left;
    }
};

int main() {
    vector<int> nums{0, 1, 2, 4};

    Solution s;
    int ans = s.getMissingNumber(nums);
    cout << ans << endl;

    return 0;
}
