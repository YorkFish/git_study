#include <stdio.h>
#include <stdbool.h>
#include <limits.h>

bool isPerfectSquare(int num){
    int left = 1, right = INT_MAX;
    while (left < right) {
        long long mid = left + (right - left) / 2;
        if (mid * mid == num) return true;
        if (mid * mid < num) left = mid + 1;
        else right = mid;
    }
    return false;
}

int main() {
    // int num = 2147483647;
    int num = 16;
    bool ans = isPerfectSquare(num);
    if (ans) printf("%d is perfect square\n", num);
    else printf("%d is not perfect square\n", num);

    return 0;
}
