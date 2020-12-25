#include <iostream>
#include <vector>
#include <deque>
#include "helper.h"

using namespace std;

class Solution {
public:
    vector<int> maxInWindows(vector<int>& nums, int k) {
        vector<int> res;
        deque<int> q;
        for (int i = 0; i < nums.size(); i ++ ) {
            while (q.size() && q.front() <= i - k) q.pop_front();
            while (q.size() && nums[q.back()] <= nums[i]) q.pop_back();
            q.push_back(i);
            if (k <= i + 1) res.push_back(nums[q.front()]);
        }
        return res;
    }
};

int main() {
    vector<int> nums{2, 3, 4, 2, 6, 2, 5, 1};
    int k = 3;

    Solution s;
    vector<int> ans = s.maxInWindows(nums, k);
    print_array(ans);

    return 0;
}
