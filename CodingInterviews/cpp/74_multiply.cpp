#include <iostream>
#include <vector>
#include "helper.h"

using namespace std;

class Solution {
public:
    vector<int> multiply(const vector<int>& A) {
        int n = A.size();
        vector<int> B(n);
        if (n == 0) return B;
        
        for (int i = 0, left = 1; i < n; i ++ ) {
            B[i] = left;
            left *= A[i];
        }
        for (int i = n - 1, right = 1; i >= 0; i -- ) {
            B[i] *= right;
            right *= A[i];
        }
        return B;
    }
};

int main() {
    vector<int> A{1, 2, 3, 4, 5};

    Solution s;
    vector<int> ans = s.multiply(A);
    print_array(ans);

    return 0;
}
