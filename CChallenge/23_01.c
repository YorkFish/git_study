#include <stdio.h>

int rangeBitwiseAnd(int m, int n) {
    if (m == n) return m;
    int res = m;
    for (int i = m+1; i < n; i++) {  // n=INT_MAX 时，防止因为 ++ 而溢出
        res &= i;
    }
    res &= n;  // n=INT_MAX 时，防止因为 ++ 而溢出
    return res;
}

int main() {
    int m = 5, n = 7;
    // int m = 2147483647, n = 2147483647;
    int result = rangeBitwiseAnd(m, n);
    printf(">>> result = %d\n", result);
    
    return 0;
}
