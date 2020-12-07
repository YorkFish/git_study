#include <stdio.h>
#include <string.h>

char * removeKdigits(char * num, int k) {
    int numSize = strlen(num);
    if (numSize == k) return "0";

    int j = 0;
    int tmpK = k;
    for (int i = 0; i < numSize; i ++ ) {
        while (j > 0 && tmpK > 0 && num[i] < num[j - 1]) {
            j -- ;
            tmpK -- ;
        }
        num[j] = num[i];
        j ++ ;
    }
    if (j <= tmpK) {
        return "0";
    }
    else {
        num[j - tmpK] = '\0';
    }

    if (num[0] == '0') {
        int i = 0;
        while (num[i] == '0') {
            i ++ ;
        }
        if (i == numSize - k) {
            return "0";
        }
        for (int j = 0; j <= numSize - k - i; j ++ ) {
            num[j] = num[j + i];
        }
    }
    return num;
}

int main() {
    char num[] = "1432219";
    char* ans = removeKdigits(num, 3);
    printf("smallest number: %s\n", ans);

    return 0;
}
