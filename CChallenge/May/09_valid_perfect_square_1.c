#include <stdio.h>
#include <stdbool.h>

bool isPerfectSquare(int num){
    // 46341 * 46341 > 2,147,483,647
    unsigned int i = 1, s = 1;
    while (s < num) {
        i ++ ;
        s = i * i;
    }
    return s == num;
}

int main() {
    int num = 2147483647;
    bool ans = isPerfectSquare(num);
    if (ans) printf("%d is perfect square\n", num);
    else printf("%d is not perfect square\n", num);

    return 0;
}
