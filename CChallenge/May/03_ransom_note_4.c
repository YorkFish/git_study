#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

int cmp(const void * a, const void * b) {
    return *(const char*)a - *(const char*)b;
}

bool canConstruct(char * ransomNote, char * magazine){
    int ransomNoteSize = strlen(ransomNote), magazineSize = strlen(magazine);
    if (magazineSize < ransomNoteSize) {
        return false;
    }
    
    qsort(ransomNote, ransomNoteSize, sizeof(char), cmp);
    qsort(magazine, magazineSize, sizeof(char), cmp);
    
    int i = 0, j = 0;
    while (i < ransomNoteSize && j < magazineSize) {
        if (ransomNote[i] == magazine[j]) {
            i ++ ;
            j ++ ;
        }
        else if (ransomNote[i] < magazine[j]) {
            return false;
        }
        else {
            j ++ ;
        }
    }
    return i == ransomNoteSize;
}

int main() {
    char ransomNote[] = "aa", magazine[] = "aab";
    if (canConstruct(ransomNote, magazine)) {
        printf("can construct\n");
    }
    else {
        printf("can not construct\n");
    }

    return 0;
}
