#include <iostream>
#include <unordered_map>
#include <queue>

using namespace std;

class Solution{
public:
    unordered_map<char, int> count;
    queue<char> q;

    //Insert one char from stringstream
    void insert(char ch){
        if ( ++ count[ch] > 1)
            while (q.size() && count[q.front()] > 1) q.pop();
        else
            q.push(ch);
    }
    //return the first appearence once char in current stringstream
    char firstAppearingOnce(){
        if (q.empty()) return '#';
        return q.front();
    }
};

int main() {
    string str = "google";

    Solution s;
    for (char ch : str) {
        s.insert(ch);
        cout << s.firstAppearingOnce() << endl;
    }

    return 0;
}
