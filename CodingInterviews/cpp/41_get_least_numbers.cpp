#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include "helper.h"

using namespace std;

class Solution {
public:
    vector<int> getLeastNumbers_Solution(vector<int> input, int k) {
        priority_queue<int> heap;
        for (int num : input) {
            heap.push(num);
            if (k < heap.size()) heap.pop();
        }

        vector<int> res;
        while (heap.size()) res.push_back(heap.top()), heap.pop();
        reverse(res.begin(), res.end());
        return res;
    }
};

int main() {
    vector<int> input{1, 2, 3, 4, 5, 6, 7, 8};
    int k = 4;

    Solution s;
    vector<int> ans = s.getLeastNumbers_Solution(input, k);
    print_array(ans);

    return 0;
}
