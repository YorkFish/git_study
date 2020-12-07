#include <stdio.h>
#include <string.h>
#include <stdbool.h>

// C 通常将结果参数放在前面
void process(char* result, const char* str, int length) {
    int j = 0;
    for (int i = 0; i < length; i++) {
        if (str[i] != '#') {
            result[j++] = str[i];
        }
        else if (j > 0) {
            j--;
        }
    }
    result[j] = '\0';
}

bool backspaceCompare(char * S, char * T) {
    int lenS = strlen(S);
    char resultS[lenS+1];
    process(resultS, S, lenS);

    int lenT = strlen(T);
    char resultT[lenT+1];
    process(resultT, T, lenT);

    return strcmp(resultS, resultT) == 0;
}

int main() {
    char S1[] = "ab#c";
    char T1[] = "ad#c";
    bool res1 = backspaceCompare(S1, T1);
    printf(">>> res1 = %d\n", res1);

    char S2[] = {'a', 'b', '#', '#', '\0'};
    char T2[] = {'a', 'b', '#', '#', '\0'};
    bool res2 = backspaceCompare(S2, T2);
    printf(">>> res2 = %d\n", res2);

    char* S3 = "a#c";
    char* T3 = "b";
    bool res3 = backspaceCompare(S3, T3);
    printf(">>> res3 = %d\n", res3);

    return 0;
}
