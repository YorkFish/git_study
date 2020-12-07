#include <stdio.h>
#include <limits.h>

// TLE
int maxSubarraySumCircular(int* A, int ASize) {
    int max = INT_MIN;
    for (int i = 0; i < 2 * ASize; i ++ ) {
        int sum = 0;
        for (int j = i; j < ASize + i; j ++ ) {
            sum += A[j % ASize];
            if (max < sum) {
                max = sum;
            }
        }
    }
    return max;
}

int main() {
    int A[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int ans = maxSubarraySumCircular(A, 9);
    printf("max(circular_subarray) = %d\n", ans);

    return 0;
}
