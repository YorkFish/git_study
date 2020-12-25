#include <iostream>

using namespace std;

class Solution {
public:
    int digitAtIndex(int n) {
        long long i = 1;    // 搜索到 i 位数
        long long s = 9;    // i 位数的个数
        long long base = 1; // 第一个 i 位数
        while (i * s < n) {
            n -= i * s;
            i ++ ;
            s *= 10;
            base *= 10;
        }
        int num = base + (n - 1) / i;
        int r = (n - 1) % i + 1;
        for (int j = 0; j < i - r; j ++ ) num /= 10;
        return num % 10;
    }
};

int main() {
    int n = 1000;

    Solution s;
    int ans = s.digitAtIndex(n);
    cout << ans << endl;

    return 0;
}
