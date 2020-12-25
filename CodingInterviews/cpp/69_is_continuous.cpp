#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool isContinuous(vector<int> numbers) {
        if (numbers.empty()) return false;

        sort(numbers.begin(), numbers.end());
        int k = 0;
        while (numbers[k] == 0) k ++ ;
        for (int i = k + 1; i < numbers.size(); i ++ )
            if (numbers[i] == numbers[i - 1])
                return false;
        return numbers.back() - numbers[k] <= 4;
    }
};

int main() {
    vector<int> nums{1, 2, 3, 4, 6};

    Solution s;
    bool ans = s.isContinuous(nums);
    if (ans) cout << "true" << endl;
    else cout << "false" << endl;

    return 0;
}
