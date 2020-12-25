#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int getNumberOfK(vector<int>& nums, int k) {
        if (nums.empty()) return 0;

        int l = 0, r = nums.size() - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] < k) l = mid + 1;
            else r = mid;
        }
        if (nums[l] != k) return 0;
        int left = l;

        l = 0, r = nums.size() - 1;
        while (l < r) {
            int mid = l + (r - l + 1) / 2;
            if (k < nums[mid]) r = mid - 1;
            else l = mid;
        }
        return r - left + 1;
    }
};

int main() {
    vector<int> nums{1, 2, 3, 3, 3, 3, 4, 5};
    int k = 3;

    Solution s;
    int ans = s.getNumberOfK(nums, k);
    cout << ans << endl;

    return 0;
}
