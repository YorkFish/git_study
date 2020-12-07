#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool canConstruct(char * ransomNote, char * magazine){
    int ransomNoteSize = strlen(ransomNote), magazineSize = strlen(magazine);
    int countDiff[26] = {0};
    for (int i = 0; i < magazineSize; i ++ ) {
        countDiff[magazine[i] - 'a'] ++ ;
    }
    for (int i = 0; i < ransomNoteSize; i ++ ) {
        countDiff[ransomNote[i] - 'a'] -- ;
        if (countDiff[ransomNote[i] - 'a'] < 0) {
            return false;
        }
    }
    return true;
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
