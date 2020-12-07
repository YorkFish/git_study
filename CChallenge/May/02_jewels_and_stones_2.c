#include <stdio.h>
#include <string.h>

int numJewelsInStones(char * J, char * S){
    int len_j = strlen(J), len_s = strlen(S);
    int countInJ[256] = {0};
    int count = 0;

    for (int i = 0; i < len_j; i ++ ) {
        countInJ[J[i]] = 1;
    }
    for (int i = 0; i < len_s; i ++ ) {
        if (countInJ[S[i]] == 1) {
            count ++ ;
        }
    }
    return count;
}

int main() {
    char *J = "aA", *S = "aAAbbbb";
    int ans = numJewelsInStones(J, S);
    printf("%d Jewel(s) in Stones\n", ans);

    return 0;
}
