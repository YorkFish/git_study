#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

bool checkValidString(char * s) {
    int minCount = 0;  // 最少有几个 '('
    int maxCount = 0;  // 最多有几个 '('
    int length = strlen(s);
    for (int i = 0; i < length; i++) {
        if (s[i] == '(') {
            minCount++;
            maxCount++;
        }
        else if (s[i] == ')') {
            minCount--;
            maxCount--;
        }
        else if (s[i] == '*') {
            minCount--;
            maxCount++;
        }
        if (maxCount < 0) {  // minCount <= maxCount
            return false;
        }
        if (minCount < 0) {
            minCount = 0;
        }
    }
    return minCount == 0;
}

int main() {
    char s[] = "(((((()*)(*)*))())())(()())())))((**)))))(()())()";  // F
    bool result = checkValidString(s);
    printf(">>> result = %d\n", result);

    return 0;
}
