#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int getUglyNumber(int n) {
        vector<int> list{1};
        int idx2 = 0, idx3 = 0, idx5 = 0;
        while ( -- n) {
            int t = min(min(list[idx2] * 2, list[idx3] * 3), list[idx5] * 5);
            list.push_back(t);
            if (t == list[idx2] * 2) idx2 ++ ;
            if (t == list[idx3] * 3) idx3 ++ ;
            if (t == list[idx5] * 5) idx5 ++ ;
        }
        return list.back();
    }
};

int main() {
    int n = 7;

    Solution s;
    int ans = s.getUglyNumber(n);
    cout << ans << endl;

    return 0;
}
