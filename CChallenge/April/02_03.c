#include <stdio.h>
#include <stdbool.h>

int next_n(int n) {
    int sum = 0;
    while (n > 0) {
        int tmp = n % 10;
        sum += tmp * tmp;
        n /= 10;
    }
    return sum;
}

bool isHappy(int n) {
    int slow = n;
    int fast = n;
    do {
        slow = next_n(slow);
        fast = next_n(fast);
        fast = next_n(fast);
    } while (slow != fast);
    return fast == 1;
}

int main() {
    printf(">>> isHappy(19) = %d\n", isHappy(19));
    printf(">>> isHappy(20) = %d\n", isHappy(20));

    return 0;
}
