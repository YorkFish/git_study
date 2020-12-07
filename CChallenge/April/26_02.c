#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int lcs(char* text1, char* text2, int m, int n, int** cache) {
    if (m == 0 || n == 0) return 0;
    if (cache[m][n] != -1) {
        return cache[m][n];
    }

    int result;
    if (text1[m-1] == text2[n-1]) {
        result = lcs(text1, text2, m-1, n-1, cache) + 1;
    }
    else {
        int discard1 = lcs(text1, text2, m-1, n, cache);
        int discard2 = lcs(text1, text2, m, n-1, cache);
        result = discard1 < discard2 ? discard2 : discard1;
    }
    cache[m][n] = result;
    return result;
}

int longestCommonSubsequence(char * text1, char * text2) {
    int len1 = strlen(text1);
    int len2 = strlen(text2);

    // int cache[len1+1][len2+1]; => cache[1000][1000]
    int** cache = malloc((len1+1) * sizeof(int*));
    for (int i = 0; i <= len1; i++) {
        cache[i] = malloc((len2+1) * sizeof(int));
    }
    for (int i = 0; i <= len1; i++) {
        for (int j = 0; j <= len2; j++) {
            cache[i][j] = -1;
        }
    }

    int result = lcs(text1, text2, len1, len2, cache);
    
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
