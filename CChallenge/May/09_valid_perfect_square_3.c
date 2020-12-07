#include <stdio.h>
#include <stdbool.h>
#include <limits.h>

// [left, right)
bool rangedIsPerfectSquare(int left, int right, int target) {
    if (left == right) return false;

    long long mid = left + (right - left) / 2;
    if (mid * mid == target) return true;
    if (mid * mid < target) return rangedIsPerfectSquare(mid + 1, right, target);
    return rangedIsPerfectSquare(left, mid, target);
}

bool isPerfectSquare(int num){
    return rangedIsPerfectSquare(1, INT_MAX, num);
}

int main() {
    // int num = 2147483647;
    int num = 16;
    bool ans = isPerfectSquare(num);
    if (ans) printf("%d is perfect square\n", num);
    else printf("%d is not perfect square\n", num);

    return 0;
}
