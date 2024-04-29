#include "treenode.h"

typedef struct node {
    TreeNode* node;
    int weight;
    struct node* next;
} Node;

Node* make_pq_node(char data, int weight);
void sortedAppend(Node** head, Node* temp);
void print_pq(Node* head);