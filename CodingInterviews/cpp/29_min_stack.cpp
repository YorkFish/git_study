#include <iostream>
#include <stack>

using namespace std;

class MinStack {
public:
    stack<int> stk, min_stk;

    /** initialize your data structure here. */
    MinStack() {
        
    }
    
    void push(int x) {
        stk.push(x);
        if (min_stk.empty() || x <= min_stk.top()) min_stk.push(x);
    }
    
    void pop() {
        if (min_stk.top() == stk.top()) min_stk.pop();
        stk.pop();
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        return min_stk.top();
    }
};

int main() {
    MinStack obj;
    obj.push(-1);
    obj.push(3);
    obj.push(-4);
    cout << obj.getMin() << endl;   // -4
    obj.pop();
    cout << obj.top() << endl;      // 3
    cout << obj.getMin() << endl;   // -1

    return 0;
}
