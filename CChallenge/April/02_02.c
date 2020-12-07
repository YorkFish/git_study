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

int contains(int* history, int size, int n) {
    for (int i = 0; i < size; i++) {
        if (history[i] == n) {
            return true;
        }
    }
    return false;
}

bool isHappy(int n) {
    int history[1000] = {0};  // 19_9999_9999 => 9^2 * 9 + 1 = 730
    int size = 0;
    while (!contains(history, size, n)) {
        history[size] = n;
        size++;
        n = next_n(n);
    }
    return (n == 1);
}

int main() {
    printf(">>> isHappy(19) = %d\n", isHappy(19));
    printf(">>> isHappy(20) = %d\n", isHappy(20));

    return 0;
}
