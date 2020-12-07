#include <stdio.h>

int findJudge(int N, int** trust, int trustSize, int* trustColSize){
    for (int i = 1; i <= N; i ++ ) {
        int trusts = 0;     // 第 i 个人相信多少人
        int trusted = 0;    // 第 i 个人被多少人相信
        for (int j = 0; j < trustSize; j ++ ) {
            if (trust[j][0] == i) trusts ++ ;
            if (trust[j][1] == i) trusted ++ ;
        }
        if (trusts == 0 && trusted == N - 1) return i;
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
