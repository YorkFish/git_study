#include <iostream>
#include <vector>
#include "helper.h"

using namespace std;

class Solution {
public:
    vector<int> printMatrix(vector<vector<int> > matrix) {
        vector<int> res;
        int rows = matrix.size();
        if (rows == 0) return res;
        int cols = matrix[0].size();
        if (cols == 0) return res;

        vector<vector<bool>> status(rows, vector<bool>(cols));
        int dx[] = {-1, 0, 1, 0}, dy[] = {0, 1, 0, -1};
        int row = 0, col = 0, d = 1;
        int times = rows * cols;
        while (times -- ) {
            res.push_back(matrix[row][col]);
            status[row][col] = true;
            int r = row + dx[d], c = col + dy[d];
            if (r < 0 || r >= rows || c < 0 || c >= cols || status[r][c]) {
                d = (d + 1) % 4;
                r = row + dx[d], c = col + dy[d];
            }
            row = r, col = c;
        }
        return res;
    }
};

int main() {
    vector<vector<int>> matrix{
        { 1,  2,  3,  4},
        { 5,  6,  7,  8},
        { 9, 10, 11, 12},
        {13, 14, 15, 16}
    };

    Solution s;
    vector<int> ans = s.printMatrix(matrix);
    print_array(ans);

    return 0;
}
