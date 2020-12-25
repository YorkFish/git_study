#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    static bool cmp(int a, int b) {
        string sa = to_string(a), sb = to_string(b);
        return sa + sb < sb + sa;
    }

    string printMinNumber(vector<int>& nums) {
        string res;
        sort(nums.begin(), nums.end(), cmp);
        for (int num : nums) res += to_string(num);
        return res;
    }
};

int main() {
    vector<int> nums{3, 32, 321};

    Solution s;
    string ans = s.printMinNumber(nums);
    cout << ans << endl;

    return 0;
}
