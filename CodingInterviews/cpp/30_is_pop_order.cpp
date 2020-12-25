#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    bool isPopOrder(vector<int> pushV,vector<int> popV) {
        if (pushV.size() == 0 && popV.size() == 0) return true;
        if (pushV.size() != popV.size()) return false;
        
        stack<int> stk;
        unsigned i = 0, j = 0;  // i: pushV's index, j: popV's index
        while (i < pushV.size()) {
            stk.push(pushV[i ++]);
            while (!stk.empty() && stk.top() == popV[j]) {
                stk.pop();
                j ++ ;
            }
        }
        return stk.empty();
    }
};

int main() {
    vector<int> pushV{1, 2, 3, 4, 5}, popV{4, 5, 3, 2, 1};

    Solution s;
    bool ans = s.isPopOrder(pushV, popV);
    if (ans) cout << "true" << endl;
    else cout << "false" << endl;

    return 0;
}
