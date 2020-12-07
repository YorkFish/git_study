#include <stdio.h>
#include <stdbool.h>

// 自己写一个偷懒版的 isBadVersion()
bool isBadVersion(int version) {
    // [1, 2, 3, 4, 5, ..., 100000000, ...]
    // [G, G, G, G, G, ..., B, B, B, ...]
    return version >= 100000000;
}

int firstBadVersion(int n) {
    // [first, last)
    unsigned int first = 1, last = (unsigned int)n + 1;
    while (first < last) {
        unsigned int mid = first + (last - first) / 2;
        if (isBadVersion(mid) && !isBadVersion(mid - 1)) return mid;
        if (!isBadVersion(mid)) first = mid + 1;
        else last = mid;
    }
    return -1;

}

int main() {
    int ans = firstBadVersion(2147483647);
    printf("first bad version: %d\n", ans);

    return 0;
}
