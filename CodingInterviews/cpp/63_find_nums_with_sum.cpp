#include <iostream>
#include <vector>
#include <unordered_set>
#include <cstdio>

using namespace std;

class Solution {
public:
    vector<int> findNumbersWithSum(vector<int>& nums, int target) {
        unordered_set<int> set;
        for (int num : nums) {
            int sub = target - num;
            if (set.count(sub)) return vector<int>{sub, num};
            else set.insert(num);
        }
        return vector<int>{};
    }
};

int main() {
    vector<int> nums{1, 2, 3, 4};
    int sum = 7;

    Solution s;
    vector<int> ans = s.findNumbersWithSum(nums, sum);
    printf("[%d, %d]\n", ans[0], ans[1]);

    return 0;
}
