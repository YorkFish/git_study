#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int getNumberSameAsIndex(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (mid <= nums[mid]) right = mid;
            else left = mid + 1;
        }
        return right == nums[right] ? right : -1;
    }
};

int main() {
    vector<int> nums{-3, -1, 1, 3, 5};

    Solution s;
    int ans = s.getNumberSameAsIndex(nums);
    cout << ans << endl;

    return 0;
}
