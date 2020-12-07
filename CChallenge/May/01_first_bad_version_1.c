#include <stdio.h>
#include <stdbool.h>

// 自己写一个偷懒版的 isBadVersion()
bool isBadVersion(int version) {
    // [1, 2, 3, 4, 5, ..., 100000000, ...]
    // [G, G, G, G, G, ..., B, B, B, ...]
    return version >= 100000000;
}

// [first, last)
unsigned int binarySearch(unsigned int first, unsigned int last) {
    unsigned int mid = first + (last - first) / 2;
    if (isBadVersion(mid) && !isBadVersion(mid - 1)) return mid;
    if (!isBadVersion(mid)) return binarySearch(mid + 1, last);
    return binarySearch(first, mid);
}

int firstBadVersion(int n) {
    // signed integer overflow: 2147483647 + 1 cannot be represented in type 'int'
    return binarySearch(1, (unsigned int)n + 1);
}

int main() {
    int ans = firstBadVersion(2147483647);
    printf("first bad version: %d\n", ans);

    return 0;
}
