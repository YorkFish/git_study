#include <stdio.h>
#include <string.h>

int numJewelsInStones(char * J, char * S){
    int count = 0;
    int len_j = strlen(J), len_s = strlen(S);
    for (int i = 0; i < len_s; i ++ ) {
        for (int k = 0; k < len_j; k ++ ) {
            if (S[i] == J[k]) {
                count ++ ;
            }
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
