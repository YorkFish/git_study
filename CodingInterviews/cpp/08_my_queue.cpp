#include <iostream>
#include <stack>

using namespace std;

class MyQueue {
public:
    stack<int> stk, cache;
    /** Initialize your data structure here. */
    MyQueue() {
        
    }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        stk.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        while (stk.size() > 1) cache.push(stk.top()), stk.pop();
        int res = stk.top();
        stk.pop();
        while (cache.size()) stk.push(cache.top()), cache.pop();
        return res;
    }
    
    /** Get the front element. */
    int peek() {
        while (stk.size() > 1) cache.push(stk.top()), stk.pop();
        int res = stk.top();
        while (cache.size()) stk.push(cache.top()), cache.pop();
        return res;
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return stk.empty();
    }
};

int main() {
    MyQueue obj = MyQueue();
    obj.push(1);
    obj.push(2);
    cout << obj.peek() << endl;
    cout << obj.pop() << endl;
    if (obj.empty()) cout << "true" << endl;
    else cout << "false" << endl;
    
    return 0;
}
