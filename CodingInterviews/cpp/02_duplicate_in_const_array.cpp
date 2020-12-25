#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int duplicateInArray(vector<int>& nums) {
        int left = 1, right = nums.size() - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;  // [left, mid], [mid + 1, right]
            int sum = 0;
            for (int x : nums) sum += x >= left && x <= mid;
            if (mid - left + 1 < sum) right = mid;
            else left = mid + 1;
        }
        return right;
    }
};

int main() {
    vector<int> nums{2, 3, 5, 4, 3, 2, 6, 7};
    Solution s;
    int ans = s.duplicateInArray(nums);
    cout << ans << endl;
    
    return 0;
}
