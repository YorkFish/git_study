#include <iostream>

using namespace std;

class Solution {
public:
    int add(int num1, int num2){
        while (num2) {
            int sum = num1 ^ num2;
            int carry = (num1 & num2) << 1;
            num1 = sum, num2 = carry;
        }
        return num1;
    }
};

int main() {
    int num1 = -9, num2 = 33;

    Solution s;
    int ans = s.add(num1, num2);
    cout << ans << endl;

    return 0;
}
