#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int moreThanHalfNum_Solution(vector<int>& nums) {
        int cnt = 0, val = -1;
        for (int num : nums) {
            if (cnt == 0) val = num, cnt = 1;
            else {
                if (num == val) cnt ++ ;
                else cnt -- ;
            }
        }
        return val;
    }
};

int main() {
    vector<int> nums{1, 2, 1, 1, 3};

    Solution s;
    int ans = s.moreThanHalfNum_Solution(nums);
    cout << ans << endl;

    return 0;
}
