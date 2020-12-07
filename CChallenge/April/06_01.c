#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char* original;
    char* sorted;
} Pair;

int cmpChar(const void* a, const void* b) {
    return *(const char*)a - *(const char*)b;
}

int cmpPair(const void* a, const void* b) {
    const Pair* pa = (const Pair*)a;
    const Pair* pb = (const Pair*)b;

    return strcmp(pa->sorted, pb->sorted);
}

char *** groupAnagrams(char ** strs, int strsSize, int* returnSize, int** returnColumnSizes) {
    Pair* pairs = malloc(sizeof(Pair) * strsSize);
    for (int i = 0; i < strsSize; i++) {
        char* sorted_str = malloc(sizeof(char) * (strlen(strs[i]) + 1));
        strcpy(sorted_str, strs[i]);
        qsort(sorted_str, strlen(strs[i]), sizeof(char), cmpChar);
        pairs[i].original = strs[i];
        pairs[i].sorted = sorted_str;
    }
    qsort(pairs, strsSize, sizeof(Pair), cmpPair);

    char *** returnResult = NULL;  // []
    *returnSize = 0;
    *returnColumnSizes = NULL;  // []
    for (int i = 0; i < strsSize; i++) {
        if (i == 0 || strcmp(pairs[i].sorted, pairs[i-1].sorted) != 0) {  // case1
            int lastGroupIdx = *returnSize;
            returnResult = realloc(returnResult, sizeof(char**)*(*returnSize+1));
            returnResult[lastGroupIdx] = malloc(sizeof(char*) * 1);
            returnResult[lastGroupIdx][0] = pairs[i].original;

            (*returnSize)++;
            *returnColumnSizes = realloc(*returnColumnSizes, sizeof(int)*(*returnSize));
            (*returnColumnSizes)[lastGroupIdx] = 1;
        }
        else {  // case2
            int lastGroupIdx = *returnSize - 1;
            int lastGroupSize = (*returnColumnSizes)[lastGroupIdx];
            returnResult[lastGroupIdx] = 
                realloc(returnResult[lastGroupIdx], sizeof(char*)*(lastGroupSize+1));
            returnResult[lastGroupIdx][lastGroupSize] = pairs[i].original;  // "eat"
            (*returnColumnSizes)[lastGroupIdx] = lastGroupSize + 1;
        }
    }

    return returnResult;   
}

int main() {
    char* strs[] = {"ate", "eat", "tea", "nat", "tan", "bat"};
    int strsSize = 6;
    int returnSize = 0;
    int* returnColumnSizes = NULL;
    char*** s = groupAnagrams(strs, strsSize, &returnSize, &returnColumnSizes);

    for (int i = 0; i < returnSize; i++) {
        for (int j = 0; j < returnColumnSizes[i]; j++) {
            printf("s[%d][%d] = %s\n", i, j, s[i][j]);
        }
    }

    for (int i = 0; i < returnSize; i++) {
        free(s[i]);
    }
    free(s);

    return 0;
}
