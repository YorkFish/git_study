#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define CAPACITY (100000+50000)

typedef struct {
    int data[CAPACITY];
    int size;
} FirstUnique;

void firstUniqueAdd(FirstUnique* obj, int value) {
    obj->data[obj->size] = value;  // obj->size 可以代表新增的位置编号
    obj->size++;
}

FirstUnique* firstUniqueCreate(int* nums, int numsSize) {
    FirstUnique* obj = calloc(1, sizeof(FirstUnique));
    obj->size = numsSize;
    for (int i = 0; i < numsSize; i++) {
        // obj->data[i] = nums[i];  // 改用 firstUniqueAdd
        firstUniqueAdd(obj, nums[i]);
    }
    return obj;
}

// 第一个只出现一次的数字是谁
int firstUniqueShowFirstUnique(FirstUnique* obj) {
    for (int i = 0; i < obj->size; i++) {
        bool isUnique = true;  // 假设 obj->data[i] 储存的数字只出现了一次
        for (int j = 0; j < obj->size; j++) {
            if (i != j && obj->data[i] == obj->data[j]) {
                isUnique = false;
                break;
            }
        }
        if (isUnique) {
            return obj->data[i];
        }
    }
    return -1;
}

void firstUniqueFree(FirstUnique* obj) {
    free(obj);
}

int main() {
    int nums[5] = {3, 9, 7, 1, 5};
    FirstUnique* obj = firstUniqueCreate(nums, 5);  // obj: {3, 9, 7, 1, 5}
    printf("%d\n", firstUniqueShowFirstUnique(obj));  // 3

    firstUniqueAdd(obj, 3);  // obj: {3, 9, 7, 1, 5, 3}
    printf("%d\n", firstUniqueShowFirstUnique(obj));  // 9
    
    firstUniqueAdd(obj, 9);  // obj: {3, 9, 7, 1, 5, 3, 9}
    printf("%d\n", firstUniqueShowFirstUnique(obj));  // 7
    
    firstUniqueFree(obj);

    return 0;
}
