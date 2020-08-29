#include <stdio.h>
#include <stdbool.h>

bool isHappy(int n) {
    int num = n;
    int sum, tmp;
    while (num != 1) {
        sum = 0;
        while (num > 0) {
            tmp = num % 10;
            sum += tmp * tmp;
            num /= 10;
        }
        if (sum == 1) {
            return true;
        }
        if (sum == n) {
            return false;
        }
        num = sum;
    }
    return true;
}

int main() {
    printf(">>> isHappy(19) = %d\n", isHappy(19));
    printf(">>> isHappy(20) = %d\n", isHappy(20));

    return 0;
}
