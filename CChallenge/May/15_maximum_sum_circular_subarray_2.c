#include <stdio.h>

// 53. Maximum Subarray
int maxSubArray(int* nums, int numsSize) {
    int maxPreArray[numsSize];
    maxPreArray[0] = 0;
    for (int i = 1; i < numsSize; i ++ ) {
        int choose = maxPreArray[i - 1] + nums[i - 1];
        int notChoose = 0;
        maxPreArray[i] = choose < notChoose ? notChoose : choose;
    }

    int maxSubArr[numsSize + 1];
    maxSubArr[1] = nums[0];
    for (int i = 2; i <= numsSize; i ++ ) {
        int choose = maxPreArray[i - 1] + nums[i - 1];
        int notChoose = maxSubArr[i - 1];
        maxSubArr[i] = choose < notChoose ? notChoose : choose;
    }
    return maxSubArr[numsSize];
}

int maxSubArray2(int* nums, int numsSize) {
    int maxSubArr = nums[0];
    int maxPreArr = 0;
    for (int i = 1; i < numsSize; i ++ ) {
        int choose = maxPreArr + nums[i - 1];
        int notChoose = 0;
        maxPreArr = choose < notChoose ? notChoose : choose;

        int choose2 = maxPreArr + nums[i];
        int notChoose2 = maxSubArr;
        maxSubArr = choose2 < notChoose2 ? notChoose2 : choose2;
    }
    return maxSubArr;
}

int maxSubArray3(int* nums, int numsSize) {
    int sum = nums[0], max = nums[0];
    for (int i = 1; i < numsSize; i ++ ) {
        if (sum < 0) sum = nums[i];
        else sum += nums[i];
        if (max < sum) max = sum;
    }
    return max;
}

int maxSubarraySumCircular(int* A, int ASize) {
    int chooseMiddle = maxSubArray3(A, ASize);
    int total = 0;
    for (int i = 0; i < ASize; i ++ ) {
        total += A[i];
    }
    for (int i = 0; i < ASize; i ++ ) {
        A[i] *= -1;
    }

    int result = maxSubArray3(A, ASize);
    if (result != -total) {
        int notChooseMiddle = total + result;
        return chooseMiddle < notChooseMiddle ? notChooseMiddle : chooseMiddle;
    }
    else {
        return chooseMiddle;
    }
}

int main() {
    int nums[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int ans1 = maxSubArray3(nums, 9);
    printf("max(subarray) = %d\n", ans1);

    int A[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int ans2 = maxSubarraySumCircular(A, 9);
    printf("max(circular_subarray) = %d\n", ans2);

    return 0;
}
