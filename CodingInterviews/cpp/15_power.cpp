#include <iostream>

using namespace std;

class Solution {
public:
    double Power(double base, int exponent) {
        double res = 1;
        for (long long k = abs((long long)exponent); k; k >>= 1) {
            if (k & 1) res *= base;
            base *= base;
        }
        if (exponent < 0) res = 1 / res;
        return res;
    }
};

int main() {
    Solution s;
    cout << s.Power(1.00000001, 999999997) << endl;
    
    return 0;
}
