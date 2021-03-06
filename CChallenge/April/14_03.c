#include <stdio.h>
#include <string.h>

char * stringShift(char * s, int** shift, int shiftSize, int* shiftColSize) {
    int len = strlen(s);
    int totalAmount = 0;
    for (int i = 0; i < shiftSize; i++) {
        int direction = shift[i][0];
        int amount = shift[i][1];
        if (direction == 0) {
            totalAmount += amount;
        }
        else {
            totalAmount -= amount;
        }
    }
    totalAmount %= len;
    if (totalAmount < 0) {
        totalAmount += len;  // totalAmount = len - (-totalAmount);
    }
    for (int j = 0; j < totalAmount; j++) {
        char temp = s[0];
        for (int k = 0; k < len-1; k++) {
            s[k] = s[k+1];
        }
        s[len-1] = temp;
    }
    return s;
}

int main() {
    char s[] = "abcdefg";
    int shift[][2] = {{1, 1}, {1, 1}, {0, 2}, {1, 15}};
    int* pShift[] = {shift[0], shift[1], shift[2], shift[3]};
    int shiftSize = 4;
    int shiftColSize[] = {2, 2, 2, 2};
    char* result = stringShift(s, pShift, shiftSize, shiftColSize);
    printf(">>> result = %s\n", result);

    return 0;
}
