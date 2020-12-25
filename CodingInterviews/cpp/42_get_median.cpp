#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class Solution {
public:
    priority_queue<int> max_heap;
    priority_queue<int, vector<int>, greater<int>> min_heap;

    void insert(int num){
        max_heap.push(num);
        if (min_heap.size() && min_heap.top() < max_heap.top()) {
            int min_top = min_heap.top(), max_top = max_heap.top();
            min_heap.pop(), max_heap.pop();
            min_heap.push(max_top), max_heap.push(min_top);
        }
        if (min_heap.size() + 2 == max_heap.size()) {
            min_heap.push(max_heap.top());
            max_heap.pop();
        }
    }

    double getMedian(){
        if (min_heap.size() < max_heap.size()) return max_heap.top();
        return (min_heap.top() + max_heap.top()) / 2.0;
    }
};

int main() {
    vector<int> input{1, 2, 3, 4};

    Solution s;
    for (int num : input) {
        s.insert(num);
        cout << s.getMedian() << endl;
    }

    return 0;
}
