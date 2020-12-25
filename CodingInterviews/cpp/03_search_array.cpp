#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool searchArray(vector<vector<int>> array, int target) {
        if (array.empty() || array[0].empty()) return false;

        int row = 0, col = array[0].size() - 1, n = array.size();
        while (row < n && col >= 0) {
            if (array[row][col] == target) return true;
            if (target < array[row][col]) col -- ;
            else row ++ ;
        }
        return false;
    }
};

int main() {
    vector<vector<int>> array{
        {1, 2,  8,  9},
        {2, 4,  9, 12},
        {4, 7, 10, 13},
        {6, 8, 11, 15}
    };
    Solution s;
    bool ans = s.searchArray(array, 7);
    if (ans) cout << "true" << endl;
    else cout << "false" << endl;
    
    return 0;
}
