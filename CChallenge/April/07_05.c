#include <stdio.h>
#include <stdbool.h>

int countElements(int* arr, int arrSize) {
    // 0<=arr[i]<=1000 => 1<=arr[i]+1<=1001
    int countOfNumX[1002] = {0};
    for (int i = 0; i < arrSize; i++) {
        countOfNumX[arr[i]]++;
    }
    int count = 0;
    for (int x = 0; x <= 1000; x++) {
        if (countOfNumX[x+1]) {
            count += countOfNumX[x];
        }
    }
    return count;
}

int main() {
    int arr1[3] = {1, 2, 3};
    int res1 = countElements(arr1, 3);
    printf(">>> res1 = %d\n", res1);

    int arr2[8] = {1, 1, 3, 3, 5, 5, 7, 7};
    int res2 = countElements(arr2, 8);
    printf(">>> res2 = %d\n", res2);

    int arr3[4] = {1, 1, 2, 2};
    int res3 = countElements(arr3, 4);
    printf(">>> res3 = %d\n", res3);

    return 0;
}
