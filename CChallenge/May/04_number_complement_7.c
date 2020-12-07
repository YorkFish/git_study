#include <stdio.h>

int findComplement(int num){
    int mask = num;
    for (int i = 1; i < 32; i <<= 1) {
        mask |= mask >> i;
    }
    return mask ^ num;
}

int main() {
    int num = 5;
    int ans = findComplement(num);
    printf("%d's complement is: %d\n", num, ans);

    return 0;
}
