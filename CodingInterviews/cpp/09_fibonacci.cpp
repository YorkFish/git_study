#include <iostream>

using namespace std;

class Solution {
public:
    int Fibonacci(int n) {
        int a = 0, b = 1;
        while (n -- ) {
            int t = a + b;
            a = b;
            b = t;
        }
        return a;
    }
};

int main() {
    Solution s;
    cout << s.Fibonacci(0) << endl;
    cout << s.Fibonacci(1) << endl;
    cout << s.Fibonacci(2) << endl;
    cout << s.Fibonacci(3) << endl;
    cout << s.Fibonacci(4) << endl;
    cout << s.Fibonacci(5) << endl;
    
    return 0;
}
