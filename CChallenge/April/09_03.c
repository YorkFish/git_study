#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

char* process(const char* str) {
    int length = strlen(str);
    char* result = malloc(sizeof(char) * (length+1));
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
    return result;
}

bool backspaceCompare(char * S, char * T) {
    char* resultS = process(S);
    char* resultT = process(T);
    bool areEqual = (strcmp(resultS, resultT) == 0);
    free(resultS);
    free(resultT);
    return areEqual;
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
