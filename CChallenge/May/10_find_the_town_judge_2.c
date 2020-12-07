#include <stdio.h>

int findJudge(int N, int** trust, int trustSize, int* trustColSize){
    int trusts[1001] = {0};     // trusts[1]: 第一个人相信多少人
    int trusted[1001] = {0};    // trusted[1]: 第一个人被多少人相信
    for (int i = 0; i < trustSize; i ++ ) {
        trusts[trust[i][0]] ++ ;
        trusted[trust[i][1]] ++ ;
    }

    for (int i = 1; i <= N; i ++ ) {
        if (trusts[i] == 0 && trusted[i] == N - 1) return i;
    }
    return -1;
}

int main() {
    int N = 4;
    int t1[] = {1, 3};
    int t2[] = {1, 4};
    int t3[] = {2, 3};
    int t4[] = {2, 4};
    int t5[] = {4, 3};
    int* trust[] = {t1, t2, t3, t4, t5};
    int trustSize = 5;
    int trustColSize[] = {2, 2, 2, 2, 2};
    int ans = findJudge(N, trust, trustSize, trustColSize);
    printf("town judge is: %d\n", ans);

    return 0;
}
