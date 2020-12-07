#include <stdio.h>

int findComplement(int num){
    int mask = num;
    for (int i = 0; i < 30; i ++ ) {
        mask = mask >> 1 | num;
    }
    return mask ^ num;
}

int main() {
    int num = 5;
    int ans = findComplement(num);
    printf("%d's complement is: %d\n", num, ans);

    return 0;
}
