#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int merge(vector<int>& nums, int l, int r) {
        if (r <= l) return 0;
        int mid = l + (r - l) / 2;
        int res = merge(nums, l, mid) + merge(nums, mid + 1, r);
        int i = l, j = mid + 1;
        vector<int> temp;
        while (i <= mid && j <= r) {
            if (nums[i] <= nums[j])
                temp.push_back(nums[i ++ ]);
            else {
                temp.push_back(nums[j ++ ]);
                res += mid - i + 1;
            }
        }
        while (i <= mid) temp.push_back(nums[i ++ ]);
        while (j <= r) temp.push_back(nums[j ++ ]);
        i = l;
        for (int num : temp) nums[i ++ ] = num;

        return res;
    }

    int inversePairs(vector<int>& nums) {
        return merge(nums, 0, nums.size() - 1);
    }
};

int main() {
    vector<int> nums{1, 2, 3, 4, 5, 6, 0};

    Solution s;
    int ans = s.inversePairs(nums);
    cout << ans << endl;

    return 0;
}
