#include <stdio.h>

int findJudge(int N, int** trust, int trustSize, int* trustColSize){
    int diff[1001] = {0};
    for (int i = 0; i < trustSize; i ++ ) {
        diff[trust[i][0]] -- ;  // 相信别人，扣一分
        diff[trust[i][1]] ++ ;  // 被人相信，加一分
    }

    for (int i = 1; i <= N; i ++ ) {
        if (diff[i] == N - 1) return i;  // 只有 town judge 才能得到 N-1 分
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
