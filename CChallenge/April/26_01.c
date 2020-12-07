#include <stdio.h>
#include <string.h>

int lcs(char* text1, char* text2, int m, int n) {
    if (m == 0 || n == 0) return 0;

    if (text1[m-1] == text2[n-1]) {
        // greedy
        // text1: "abcd(e)" => ...(e)
        // text2: "ac(e)"   => ...(e)
        return lcs(text1, text2, m-1, n-1) + 1;
    }
    else {
        // text1: "abcf(e)"
        // text2: "acf"
        int discard1 = lcs(text1, text2, m-1, n);
        int discard2 = lcs(text1, text2, m, n-1);
        int max = discard1 < discard2 ? discard2 : discard1;
        return max;
    }
}

int longestCommonSubsequence(char * text1, char * text2) {
    int len1 = strlen(text1);
    int len2 = strlen(text2);
    // text1: "abcde"
    // text2: "ace"

    // text1 最后一个字元 => 1.   属于最长的共同子序列
    //                      2. 不属于最长的共同子序列

    // text2 最后一个字元 => 1.   属于最长的共同子序列
    //                      2. 不属于最长的共同子序列

    return lcs(text1, text2, len1, len2);
}

int main() {
    char s1[] = "abcde";
    char s2[] = "ace";
    int result = longestCommonSubsequence(s1, s2);
    printf(">>> result = %d\n", result);

    return 0;
}
