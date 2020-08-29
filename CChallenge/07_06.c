#include <stdio.h>
#include <stdbool.h>

int countElements(int* arr, int arrSize) {
    int count = 0;
    for (int i = 0; i < arrSize; i++) {
        for (int j = 0; j < arrSize; j++) {
            if (arr[j] == arr[i] + 1) {
                count++;
                break;
            }
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
