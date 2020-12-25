#pragma once
// vs, gcc, clang, msbc
#ifndef __HELPER__
#define __HELPER__

#include <iostream>
#include <queue>
#include <vector>

using namespace std;

// Definition for singly-linked list
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

// Definition for singly-linked list with a random pointer
struct ListRandomNode {
    int val;
    ListRandomNode *next, *random;
    ListRandomNode(int x) : val(x), next(NULL), random(NULL) {}
};

// Definition for a binary tree node
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

void print_linked_list(ListNode* head);
void print_tree(TreeNode* root);
void print_array(vector<int>& array);
void print_matrix(vector<vector<int>>& matrix);

#endif  // __HELPER__
