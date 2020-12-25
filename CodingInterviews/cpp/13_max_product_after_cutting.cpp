#include <iostream>

using namespace std;

class Solution {
public:
    int maxProductAfterCutting(int length) {
        if (length <= 3) return 1 * (length - 1);

        int res = 1;
        if (length % 3 == 1) length -= 4, res *= 4;
        if (length % 3 == 2) length -= 2, res *= 2;
        while (length > 0) length -= 3, res *= 3;
        return res;
    }
};

int main() {
    Solution s;
    cout << s.maxProductAfterCutting(58) << endl;
    
    return 0;
}
