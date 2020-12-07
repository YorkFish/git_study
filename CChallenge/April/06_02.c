#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "uthash.h"  // 开源库，需要去 GitHub 上 clone

#define KEYLEN 128
typedef struct {
    char key[KEYLEN];
    int listSize;
    char **list;
    UT_hash_handle hh;  // makes this structure hashable
} Map;

int cmpFunc(const void *a, const void *b) { return *(char *)a - *(char *)b; }

char*** groupAnagrams(char** strs, int strsSize, int* returnSize, int** returnColumnSizes) {
    if (strsSize <= 0) return NULL;
    Map *map = NULL, *elem = NULL;
    char strBuf[KEYLEN];
    for (int i = 0; i < strsSize; i++) {
        int length=strlen(strs[i]);
        strncpy(strBuf, strs[i], KEYLEN);
        qsort(strBuf, length, sizeof(char), cmpFunc);
        HASH_FIND_STR(map, strBuf, elem);  // head,findstr,out, convenience forms of HASH_FIND
        if (!elem) {
            elem = malloc(sizeof(Map));
            strncpy(elem->key, strBuf, KEYLEN);
            elem->listSize = 1;
            elem->list = malloc(sizeof(char *));
            elem->list[0] = strs[i];
            HASH_ADD_STR(map, key, elem);  // head,strfield,add
        } else {
            elem->listSize++;
            elem->list = realloc(elem->list, elem->listSize * sizeof(char *));
            elem->list[elem->listSize - 1] = strs[i];
        }
    }

    *returnSize = HASH_COUNT(map);  // obtain a count of items in the hash
    *returnColumnSizes=(int *)malloc(*returnSize*sizeof(int));
    char ***result = malloc(*returnSize * sizeof(char **));
    int mapIndx = 0;
    Map *tmp;
    HASH_ITER(hh, map, elem, tmp) {  // hh,head,el,tmp
        (*returnColumnSizes)[mapIndx] = elem->listSize;
        result[mapIndx++] = elem->list;
    }
    return result;
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
