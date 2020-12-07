#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool canConstruct(char * ransomNote, char * magazine){
    int ransomNoteSize = strlen(ransomNote), magazineSize = strlen(magazine);
    for (int i = 0; i < ransomNoteSize; i ++ ) {
        bool isFound = false;
        for (int j = i; j < magazineSize; j ++ ) {
            if (magazine[j] == ransomNote[i]) {
                isFound = true;
                char t = magazine[j];
                magazine[j] = magazine[i];
                magazine[i] = t;
                break;
            }
        }
        if (!isFound) {
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
