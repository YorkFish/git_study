#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {
        int n = nums.size() - 1;
        if (n < 0) return -1;
        while (n > 0 && nums[n] == nums[0]) n -- ;
        if (nums[0] < nums[n]) return nums[0];
        int left = 0, right = n;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < nums[0]) right = mid;
            else left = mid + 1;
        }
        return nums[right];
    }
};

int main() {
    vector<int> nums1{2, 2, 2, 0, 1};
    vector<int> nums2{0, 1, 3, 5, 5};
    Solution s;
    cout << s.findMin(nums1) << endl;
    cout << s.findMin(nums2) << endl;
    
    return 0;
}
