#include <stdio.h>
#include <stdlib.h>
#include "linkedlist.h"

Node* make_node(int data) {
    Node* new = malloc(sizeof(Node));
    if (new == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    new->val = data;
    new->next = NULL;

    return new;
}

void insert_in_front(Node** list, Node** newnode) {
    (*newnode)->next = *list;
    *list = *newnode;
}

int list_length(Node* head) {
    int count = 0;
    Node* ptr = head;
    while (ptr != NULL) {
        count = count + 1;
        ptr = ptr->next;
    }
    return count;
}

char* print_list(Node* head) {
    char* result = malloc(1024);

    int index = 0;
    Node* node = head;
    while (node != NULL) {
        int num_len = snprintf(NULL, 0, "%d", node->val);
        snprintf(result + index, 8, "%d", node->val);
        index += num_len - 1;
        if (node->next != NULL) {
            result[++index] = ' ';
            result[++index] = '-';
            result[++index] = '>';
            result[++index] = ' ';
        }
        index++;

        node = node->next;
    }
    result[index] = '\0';

    return result;
}
