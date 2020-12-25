#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int numberOf1Between1AndN_Solution(int n) {
        if (n == 0) return 0;
        vector<int> number;
        while (n) number.push_back(n % 10), n /= 10;

        int res = 0;
        for (int i = number.size() - 1; i >= 0; i -- ) {
            int left = 0, right = 0, t = 1;  // t: right 的位数
            for (int j = number.size() - 1; j > i; j -- )
                left = left * 10 + number[j];
            for (int j = i - 1; j >= 0; j -- )
                right = right * 10 + number[j], t *= 10;
            res += left * t;
            if (number[i] == 1) res += right + 1;
            else if (number[i] > 1) res += t;
        }
        return res;
    }
};

int main() {
    n = 20;

    Solution s;
    int ans = s.numberOf1Between1AndN_Solution(n);
    cout << ans << endl;

    return 0;
}
