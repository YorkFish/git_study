#include <stdio.h>
#include <stdbool.h>

bool isPerfectSquare(int num){
    // (i+1) * (i+1) = i^2 + 2i + 1
    unsigned int s = 1;  // i^2
    unsigned int d = 2;  // 2i
    while (s < num) {
        s = s + d + 1;
        d += 2;
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
