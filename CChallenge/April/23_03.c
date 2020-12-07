#include <stdio.h>

int rangeBitwiseAnd(int m, int n) {
    int count = 0;
    while (m != n) {
        m >>= 1;
        n >>= 1;
        count++;
    }
    return m << count;
}

int main() {
    int m = 5, n = 7;
    // int m = 2147483647, n = 2147483647;
    int result = rangeBitwiseAnd(m, n);
    printf(">>> result = %d\n", result);
    
    return 0;
}
