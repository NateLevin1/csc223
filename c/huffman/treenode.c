#include "treenode.h"
#include <stdlib.h>
#include <stdio.h>

TreeNode* make_tree_node(char data) {
    TreeNode* new = malloc(sizeof(TreeNode));
    if (new == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    new->data = data;

    return new;
}