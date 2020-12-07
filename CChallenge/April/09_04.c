#include <stdio.h>
#include <string.h>
#include <stdbool.h>

void process(char* str) {
    int length = strlen(str);
    int j = 0;
    for (int i = 0; i < length; i++) {
        if (str[i] != '#') {
            str[j++] = str[i];
        }
        else if (j > 0) {
            j--;
        }
    }
    str[j] = '\0';
}

bool backspaceCompare(char * S, char * T) {
    process(S);
    process(T);
    return strcmp(S, T) == 0;
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

    // char* S3 = "a#c";
    // char* T3 = "b";  // line16 会有问题
    // bool res3 = backspaceCompare(S3, T3);
    // printf(">>> res3 = %d\n", res3);

    return 0;
}
