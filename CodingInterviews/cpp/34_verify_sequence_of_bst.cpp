#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool verifySequenceOfBST(vector<int> sequence) {
        return dfs(0, sequence.size() - 1, sequence);
    }
    
    // [left, right]
    bool dfs(int left, int right, vector<int> &seq) {
        if (right <= left) return true;  // 空结点视为 true
        int root = seq[right];
        int split = left;
        while (split < right && seq[split] < root) split ++ ;
        for (int i = split; i < right; i ++ )
            if (seq[i] < root)
                return false;
        return dfs(left, split - 1, seq) && dfs(split, right - 1, seq);
    }
};

int main() {
    vector<int> seq{4, 8, 6, 12, 16, 14, 10};

    Solution s;
    bool ans = s.verifySequenceOfBST(seq);
    if (ans) cout << "true" << endl;
    else cout << "false" << endl;

    return 0;
}
