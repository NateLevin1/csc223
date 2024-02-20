#include <stdio.h>
#include <stdlib.h>
#include "clist.h"

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

char* print_list(Node* head) {
    char* result = malloc(1024);

    int index = 0;
    Node* node = head;
    if (node == NULL) {
        result[0] = '\0';
        return result;
    }
    while (node != head || index == 0) {
        int num_len = snprintf(NULL, 0, "%d", node->val);
        snprintf(result + index, 8, "%d", node->val);
        index += num_len - 1;
        if (node->next != head) {
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
