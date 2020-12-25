#include <iostream>

using namespace std;

class Solution {
public:
    int lastRemaining(int n, int m){
        if (n == 1) return 0;  // 剩下一个人，就是 0 号索引
        return (lastRemaining(n - 1, m) + m) % n;
    }
};

int main() {
    int n = 5, m = 3;

    Solution s;
    int ans = s.lastRemaining(n, m);
    cout << ans << endl;

    return 0;
}
