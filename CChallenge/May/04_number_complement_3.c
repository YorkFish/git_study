#include <stdio.h>

int findComplement(int num){
    int pos;
    int mask = 1 << 30;
    for (int i = 30; i >= 0; i -- , mask >>= 1) {
        if ((mask & num) != 0) {
            pos = i;
            break;
        }
    }
    int totalMask = ((unsigned int)1 << (pos + 1)) - 1;
    return totalMask ^ num;
}

int main() {
    int num = 5;
    int ans = findComplement(num);
    printf("%d's complement is: %d\n", num, ans);

    return 0;
}
