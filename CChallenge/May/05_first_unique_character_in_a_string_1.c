#include <stdio.h>
#include <stdbool.h>
#include <string.h>

int firstUniqChar(char * s){
    int sSize = strlen(s);
    for (int i = 0; i < sSize; i ++ ) {
        bool isUnique = true;
        for (int j = 0; j < sSize; j ++ ) {
            if (s[j] == s[i] && j != i) {
                isUnique = false;
                break;
            }
        }
        if (isUnique) {
            return i;
        }
    }
    return -1;
}

int main() {
    char s1[] = "leetcode";
    char s2[] = "loveleetcode";
    int ans1 = firstUniqChar(s1);
    int ans2 = firstUniqChar(s2);
    printf("ans1: %d\n", ans1);
    printf("ans2: %d\n", ans2);

    return 0;
}
