#include <stdio.h>
#include <string.h>

int firstUniqChar(char * s){
    int sSize = strlen(s);
    int count[26] = {0};
    for (int i = 0; i < sSize; i ++ ) {
        count[s[i] - 'a'] ++ ;
    }
    for (int i = 0; i < sSize; i ++ ) {
        if (count[s[i] - 'a'] == 1) {
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
