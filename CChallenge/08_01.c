#include <stdio.h>

/**
 * Definition for single-linked list.
 */
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* middleNode(struct ListNode* head) {
    int length = 0;
    for (struct ListNode* curr = head; curr != NULL; curr = curr->next) {
        length++;
    }
    length /= 2;
    struct ListNode* curr = head;
    while (length > 0) {
        curr = curr->next;
        length--;
    }
    return curr;
}

int main() {
    struct ListNode n1, n2, n3, n4, n5, n6;
    n1.val = 1;
    n2.val = 2;
    n3.val = 3;
    n4.val = 4;
    n5.val = 5;
    n6.val = 6;
    n1.next = &n2;
    n2.next = &n3;
    n3.next = &n4;
    n4.next = &n5;
    // n5.next = NULL;
    n5.next = &n6;
    n6.next = NULL;

    struct ListNode* mid = middleNode(&n1);
    printf(">>> mid->val = %d\n", mid->val);

    return 0;
}
