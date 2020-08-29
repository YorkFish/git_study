#include <stdio.h>
#include <string.h>

char * stringShift(char * s, int** shift, int shiftSize, int* shiftColSize) {
    // abcd -> shift right 1 -> dabc
    // abcd -> shift left 3 -> dabc
    // => shift right 1 == shift left (n-1)
    int len = strlen(s);
    for (int i = 0; i < shiftSize; i++) {
        int direction = shift[i][0];
        int amount = shift[i][1] % len;
        if (direction == 1) {
            amount = len - amount;
        }
        for (int j = 0; j < amount; j++) {
            char temp = s[0];
            for (int k = 0; k < len-1; k++) {
                s[k] = s[k+1];
            }
            s[len-1] = temp;
        }
    }
    return s;
}

int main() {
    char s[] = "abcdefg";
    int shift[][2] = {{1, 1}, {1, 1}, {0, 2}, {1, 3}};
    int* pShift[] = {shift[0], shift[1], shift[2], shift[3]};
    int shiftSize = 4;
    int shiftColSize[] = {2, 2, 2, 2};
    char* result = stringShift(s, pShift, shiftSize, shiftColSize);
    printf(">>> result = %s\n", result);

    return 0;
}
