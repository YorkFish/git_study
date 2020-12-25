#include <iostream>

using namespace std;

class Solution {
public:
    int NumberOf1(int n) {
        unsigned num = n;
        int count = 0;
        while (num > 0) count += num & 1, num >>= 1;
        return count;
    }
};

int main() {
    Solution s;
    cout << s.NumberOf1(15) << endl;
    
    return 0;
}
