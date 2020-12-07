#include <stdio.h>
#include <stdbool.h>

bool isFound(int xPlus1, int* arr, int arrSize) {
    bool isFound = false;
    for (int i = 0; i < arrSize; i++) {
        if (arr[i] == xPlus1) {
            isFound = true;
            break;
        }
    }
    return isFound;
}

int countElements(int* arr, int arrSize) {
    int count = 0;
    for (int i = 0; i < arrSize; i++) {
        if (isFound(arr[i]+1, arr, arrSize)) {
            count++;
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
