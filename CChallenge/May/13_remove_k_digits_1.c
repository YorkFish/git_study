#include <stdio.h>
#include <string.h>

char * removeKdigits(char * num, int k) {
    int numSize = strlen(num);
    if (numSize == k) return "0";

    for (int t = 0; t < k; t ++ ) {
        for (int i = 0; i < numSize - t; i ++ ) {
            if (num[i] > num[i + 1]) {
                for (int j = i; j < numSize - t; j ++ ){
                    num[j] = num[j + 1];
                }
                break;
            }
        }
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
    char num[] = "10";
    char* ans = removeKdigits(num, 1);
    printf("smallest number: %s\n", ans);

    return 0;
}
