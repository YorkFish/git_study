#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int longestCommonSubsequence(char * text1, char * text2) {
    int len1 = strlen(text1);
    int len2 = strlen(text2);
    int** cache = malloc((len1+1) * sizeof(int*));
    for (int i = 0; i <= len1; i++) {
        cache[i] = malloc((len2+1) * sizeof(int));
    }

    int result;
    for (int m = 0; m <= len1; m++) {
        for (int n = 0; n <= len2; n++) {
            if (m == 0 || n == 0) {
                cache[m][n] = 0;
                continue;
            }

            if (text1[m-1] == text2[n-1]) {
                result = cache[m-1][n-1] + 1;
            }
            else {
                int discard1 = cache[m-1][n];
                int discard2 = cache[m][n-1];
                result = discard1 < discard2 ? discard2 : discard1;
            }
            cache[m][n] = result;
        }
    }

    result = cache[len1][len2];
    
    for (int i = 0; i <= len1; i++) {
        free(cache[i]);
    }
    free(cache);
    
    return result;
}

int main() {
    char s1[] = "abcde";
    char s2[] = "ace";
    int result = longestCommonSubsequence(s1, s2);
    printf(">>> result = %d\n", result);

    return 0;
}
