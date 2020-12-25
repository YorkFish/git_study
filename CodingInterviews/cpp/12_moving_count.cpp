#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int get_single_sum(int num) {
        int sum = 0;
        while (num > 0) sum += num % 10, num /= 10;
        return sum;
    }

    int get_sum(pair<int, int> p) {
        return get_single_sum(p.first) + get_single_sum(p.second);
    }

    int movingCount(int threshold, int rows, int cols) {
        if (rows <= 0 || cols <= 0) return 0;
        
        int res = 0;
        vector<vector<bool>> status(rows, vector<bool>(cols));  // 默认值是 false
        queue<pair<int, int>> q;
        q.push({0, 0});
        int dx[] = {-1, 0, 1, 0}, dy[] = {0, 1, 0, -1};
        while (q.size() > 0) {
            pair<int, int> t = q.front();
            q.pop();
            if (status[t.first][t.second] || threshold < get_sum(t)) continue;

            res ++ ;
            status[t.first][t.second] = true;
            for (int d = 0; d < 4; d ++ ) {
                int x = t.first + dx[d], y = t.second + dy[d];
                if (x >= 0 && x < rows && y >= 0 && y < cols) q.push({x, y});
            }
        }
        return res;
    }
};

int main() {
    Solution s;
    cout << s.movingCount(18, 40, 40) << endl;
    
    return 0;
}
