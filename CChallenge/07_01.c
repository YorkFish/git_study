#include <stdio.h>
#include <stdlib.h>

int cmpNum(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int countElements(int* arr, int arrSize) {
    qsort(arr, arrSize, sizeof(int), cmpNum);

    int sum = 0, cnt = 1;
    int pre = arr[0];
    for (int i = 1; i < arrSize; i++) {
        if (pre == arr[i]) {
            cnt++;
            continue;
        }
        if (pre + 1 == arr[i]) {
            sum += cnt;
        }
        cnt = 1;
        pre = arr[i];
    }
    return sum;
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
