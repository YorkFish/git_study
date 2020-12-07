#include <stdio.h>

int findComplement(int num){
    unsigned int mask = ~0;
    while ((mask & num) != 0) mask <<= 1;
    mask = ~mask;
    return mask ^ num;
}

int main() {
    int num = 5;
    int ans = findComplement(num);
    printf("%d's complement is: %d\n", num, ans);

    return 0;
}
