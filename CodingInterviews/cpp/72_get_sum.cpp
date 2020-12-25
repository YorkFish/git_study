#include <iostream>

using namespace std;

class Solution {
public:
    int getSum(int n) {
        n && (n += getSum(n - 1));
        return n;
    }
};

int main() {
    int n = 10;

    Solution s;
    int ans = s.getSum(n);
    cout << ans << endl;

    return 0;
}
