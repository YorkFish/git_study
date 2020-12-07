#include <stdio.h>

int rangeBitwiseAnd(int m, int n) {
    int res = 0;
    for (int i = 30; i >= 0; i--) {
        int dm = m & (1 << i);
        int dn = n & (1 << i);
        if (dm != dn) {
            break;
        }
        res += dm;
    }
    return res;
}

int main() {
    int m = 5, n = 7;
    // int m = 2147483647, n = 2147483647;
    int result = rangeBitwiseAnd(m, n);
    printf(">>> result = %d\n", result);
    
    return 0;
}
