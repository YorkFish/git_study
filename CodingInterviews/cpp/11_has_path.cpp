#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool hasPath(vector<vector<char>> &matrix, string &str) {
        for (int i = 0; i < matrix.size(); i ++ ) {
            for (int j = 0; j < matrix[i].size(); j ++ ) {
                if (dfs(matrix, str, 0, i, j)) return true;
            }
        }
        return false;
    }

    // u: 对比到 str[u]
    // x, y: 对比到 matrix[x][y]
    bool dfs(vector<vector<char>> &matrix, string &str, int u, int x, int y) {
        if (str[u] != matrix[x][y]) return false;
        if (u == str.size() - 1) return true;
        int dx[] = {-1, 0, 1, 0}, dy[] = {0, 1, 0, -1};
        char t = matrix[x][y];
        matrix[x][y] = '#';
        for (int d = 0; d < 4; d ++ ) {
            int row = x + dx[d], col = y + dy[d];
            if (row >= 0 && row < matrix.size() && col >= 0 && col < matrix[row].size()) {
                if (dfs(matrix, str, u + 1, row, col)) return true;
            }
        }
        matrix[x][y] = t;
        return false;
    }
};

int main() {
    vector<vector<char>> matrix{
        {'A', 'B', 'C', 'E'},
        {'S', 'F', 'C', 'S'},
        {'A', 'D', 'E', 'E'}
    };
    // string str = "BCCE";
    string str = "ASAE";
    
    // vector<vector<char>> matrix{{'a'}};
    // string str = "a";
    Solution s;
    if (s.hasPath(matrix, str)) cout << "true" << endl;
    else cout << "false" << endl;
    
    return 0;
}
