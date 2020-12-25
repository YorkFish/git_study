#include "helper.h"

void print_linked_list(ListNode* head) {
    ListNode* cur = head;
    while (cur) {
        cout << cur->val << "->";
        cur = cur->next;
    }
    cout << "NULL" << endl;
}

void print_tree(TreeNode* root) {
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        TreeNode* tmp = q.front();
        q.pop();
        if (tmp == nullptr) {
            cout << "NULL ";
        }
        else {
            cout << tmp->val << ' ';
            q.push(tmp->left);
            q.push(tmp->right);
        }
    }
    cout << endl;
}

void print_array(vector<int>& array) {
    for (unsigned i = 0; i < array.size(); i ++ ) cout << array[i] << ' ';
    cout << endl;
}

void print_matrix(vector<vector<int>>& matrix) {
    for (unsigned i = 0; i < matrix.size(); i ++ ) {
        for (unsigned j = 0; j < matrix[i].size(); j ++ ) {
            cout << matrix[i][j] << ' ';
        }
        cout << endl;
    }
}
